#! /usr/bin/env python3

import io
import json
import os
import markdown as md
from bs4 import BeautifulSoup, Tag, NavigableString
from functions import findAllFiles
from html import escape
from pathlib import Path
from textwrap import dedent
from weasyprint import HTML


BLOCK_ELEMENTS = {
    "blockquote",
    "dd",
    "div",
    "dl",
    "dt",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "li",
    "ol",
    "p",
    "pre",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "ul",
}

VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


def _open_tag(tag):
    attrs = ""
    for key, val in tag.attrs.items():
        if isinstance(val, list):
            val = " ".join(val)
        attrs += f' {key}="{escape(str(val))}"'
    return f"<{tag.name}{attrs}>"


def _format(node, depth=0):
    pad = "  " * depth

    if isinstance(node, NavigableString):
        return node.strip()

    if node.name in VOID_ELEMENTS:
        return f"{pad}{_open_tag(node)}"

    has_block_child = any(
        isinstance(c, Tag) and c.name in BLOCK_ELEMENTS for c in node.children
    )

    if has_block_child:
        parts = []
        for child in node.children:
            if isinstance(child, NavigableString):
                text = child.strip()
                if text:
                    parts.append("  " * (depth + 1) + text)
            else:
                result = _format(child, depth + 1)
                if result:
                    parts.append(result)
        inner = "\n".join(parts)
        return f"{pad}{_open_tag(node)}\n{inner}\n{pad}</{node.name}>"
    else:
        inner = "".join(str(c) for c in node.children).strip()
        if not inner:
            return f"{pad}{_open_tag(node)}</{node.name}>"
        return f"{pad}{_open_tag(node)}{inner}</{node.name}>"


def format_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    parts = []
    for child in soup.children:
        if isinstance(child, NavigableString):
            text = child.strip()
            if text:
                parts.append(text)
        elif isinstance(child, Tag):
            result = _format(child)
            if result:
                parts.append(result)
    return "\n".join(parts)


def convertMdToHTML(file_path):
    output = io.BytesIO()
    try:
        # Parse the Markdown file
        md.markdownFromFile(
            input=str(file_path),
            output=output,
            extensions=[
                "markdown.extensions.attr_list",
                "markdown.extensions.toc",
                "tables",
            ],
        )
        content = output.getvalue().decode("utf-8")
    except OSError:
        content = None
    finally:
        output.close()

    return content


def main():
    script_path = os.path.dirname(__file__)
    root_path = os.path.abspath(os.path.join(script_path, os.pardir, os.pardir))

    # Get list of documents to convert
    with open(os.path.join(script_path, "convert_sources.json")) as f:
        json_data = json.load(f)
        pdf_files = json_data["pdf"]
        html_files = json_data["html"]
        files_to_convert = list(set(pdf_files + html_files))

    files_list = findAllFiles(root_path)

    for locale, filenames in files_list.items():
        for filename in filenames:
            if filename in files_to_convert:
                locale_folder = os.path.join(root_path, locale)
                source_file = os.path.join(locale_folder, filename)

                # Convert Markdown to HTML
                html_content = convertMdToHTML(source_file)

                # Save HTML file if requested, creating `html` folder if missing
                if filename in html_files:
                    Path(os.path.join(locale_folder, "html")).mkdir(exist_ok=True)
                    html_dest_file = os.path.join(
                        locale_folder, "html", f"{filename.rstrip('.md')}.html"
                    )
                    with open(html_dest_file, "w", encoding="utf-8") as output_file:
                        output_file.write(format_html(html_content))

                # Save PDF file if requested, creating `pdf` folder if missing
                if filename in pdf_files:
                    Path(os.path.join(locale_folder, "pdf")).mkdir(exist_ok=True)
                    pdf_dest_file = os.path.join(
                        locale_folder, "pdf", f"{filename.rstrip('.md')}.pdf"
                    )
                    # If the HTML includes <table> elements, add some basic CSS
                    # for readability.
                    if "<table>" in html_content:
                        css = """
                            <style>
                            table {
                                width: 100%;
                                border-collapse: collapse;
                                border: 1px solid #CCC;
                            }
                            th, td {
                                border: 1px solid #CCC;
                                padding: 8px;
                            }
                            
                            th {
                                background-color: #EEE;
                            }
                            </style>
                        """
                        html_content = dedent(css) + html_content
                    # Convert HTML to PDF
                    HTML(string=html_content).write_pdf(pdf_dest_file)


if __name__ == "__main__":
    main()
