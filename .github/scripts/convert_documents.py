#! /usr/bin/env python3

import io
import json
import os
import markdown as md
from collections import defaultdict
from weasyprint import HTML
from pathlib import Path


def findAllFiles(path):
    """Create a list of all markdown files in path"""

    files = defaultdict(list)
    search_path = Path(path)
    file_paths = search_path.glob(f"*/*.md")

    for fp in file_paths:
        # Threat the first folder as locale code
        locale = str(fp.parent.relative_to(path))
        filename = str(fp.name)
        files[locale].append(filename)

    return files


def convertMdToHTML(file_path):
    output = io.BytesIO()
    try:
        # Parse the Markdown file
        """
        md.markdownFromFile(
            input=str(file_path),
            output=output,
            extensions=["markdown.extensions.attr_list",
                        "markdown.extensions.toc", OutlineExtension((("wrapper_cls", ""),))],
        )
        """
        md.markdownFromFile(
            input=str(file_path),
            output=output,
            extensions=["markdown.extensions.attr_list", "markdown.extensions.toc"],
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
        for f in filenames:
            if f in files_to_convert:
                locale_folder = os.path.join(root_path, locale)
                source_file = os.path.join(locale_folder, f)

                # Convert Markdown to HTML
                html_content = convertMdToHTML(source_file)

                # Save HTML file if necessary, creating html folder if necessary
                if f in html_files:
                    Path(os.path.join(locale_folder, "html")).mkdir(exist_ok=True)
                    html_dest_file = os.path.join(
                        locale_folder, "html", f"{f.rstrip('.md')}.html"
                    )
                    with open(html_dest_file, "w", encoding="utf-8") as f:
                        f.write(html_content)

                # Save PDF file if necessary, creating pdf folder if necessary
                if f in pdf_files:
                    Path(os.path.join(locale_folder, "pdf")).mkdir(exist_ok=True)
                    pdf_dest_file = os.path.join(
                        locale_folder, "pdf", f"{f.rstrip('.md')}.pdf"
                    )
                    # Convert HTML to PDF
                    HTML(string=html_content).write_pdf(pdf_dest_file)


if __name__ == "__main__":
    main()
