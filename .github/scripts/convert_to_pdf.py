#! /usr/bin/env python3

import io
import json
import os
import markdown as md
from weasyprint import HTML
from pathlib import Path
from functions import findAllFiles


def convertMdToHTML(file_path):
    output = io.BytesIO()
    try:
        # Parse the Markdown file
        md.markdownFromFile(
            input=str(file_path),
            output=output,
            extensions=["markdown.extensions.attr_list", "markdown.extensions.toc", "tables"],
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
    with open(os.path.join(script_path, "pdf_sources.json")) as f:
        pdf_files = json.load(f)["files"]

    files_list = findAllFiles(root_path)

    for locale, filenames in files_list.items():
        for f in filenames:
            if f in pdf_files:
                locale_folder = os.path.join(root_path, locale)
                source_file = os.path.join(locale_folder, f)
                dest_file = os.path.join(locale_folder, "pdf", f"{f.rstrip('.md')}.pdf")

                # Create pdf folder if not available yet
                Path(os.path.join(locale_folder, "pdf")).mkdir(exist_ok=True)

                # Convert Markdown to HTML
                html_content = convertMdToHTML(source_file)
                # with open(f"{dest_file}.html", "w", encoding="utf-8") as f:
                #    f.write(html_content)

                # Convert HTML to PDF
                HTML(string=html_content).write_pdf(dest_file)


if __name__ == "__main__":
    main()
