#! /usr/bin/env python3

import io
import json
import os
import markdown as md
from functions import findAllFiles
from pathlib import Path
from textwrap import dedent
from weasyprint import HTML


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
                        output_file.write(html_content)

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
