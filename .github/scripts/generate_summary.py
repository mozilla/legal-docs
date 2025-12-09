#! /usr/bin/env python3

import os
import json


def main():
    script_path = os.path.dirname(__file__)
    root_path = os.path.abspath(os.path.join(script_path, os.pardir, os.pardir))

    with open(os.path.join(root_path, ".github", "stats.json")) as f:
        stats = json.load(f)

    with open(os.path.join(root_path, ".github", "templates", "index.html")) as f:
        html_template = f.read()

    body_localized = []
    body_not_localized = []
    for file_name, file_stats in stats.items():
        if file_stats["count"] > 0:
            body_localized.append(
                f"""
                <tr>
                    <td><a href="{file_stats["link"]}">{file_name}</a></td>
                    <td>{file_stats["last_update"]}</td>
                    <td>{file_stats["count"]}</td>
                    <td>{", ".join(file_stats["locales"])}</td>
                </tr>"""
            )
        else:
            body_not_localized.append(
                f"""
                <tr>
                    <td><a href="{file_stats["link"]}">{file_name}</a></td>
                    <td>{file_stats["last_update"]}</td>
                </tr>"""
            )

    html_template = html_template.replace(
        "%TABLEBODYLOCALIZED%", "\n".join(body_localized)
    ).replace("%TABLEBODYNOTLOCALIZED%", "\n".join(body_not_localized))

    os.makedirs(os.path.join(root_path, "docs"), exist_ok=True)
    with open(os.path.join(root_path, "docs", "index.html"), "w") as f:
        f.write(html_template)


if __name__ == "__main__":
    main()
