#! /usr/bin/env python3
"""
Manage the preview version of the Firefox Privacy Notice, and the preambles
linking the current and preview versions.

Usage:
  python .github/scripts/firefox_pn_preambles.py --create
  python .github/scripts/firefox_pn_preambles.py --add
  python .github/scripts/firefox_pn_preambles.py --publish

--create: copy firefox_privacy_notice.md to firefox_privacy_notice_preview.md
          for all locales, overwriting existing files, and add the preamble
          to the preview.
--add: add the localized preamble to both files for each locale.
--publish: copy firefox_privacy_notice_preview.md to firefox_privacy_notice.md
           for all locales, overwriting existing files (without preambles).
"""

import argparse
import re
import sys
from pathlib import Path

# For each version: file name, plus URL and CSS class used in links pointing
# to it. Each version's file has a preamble linking to the other version.
NOTICES = {
    "current": {
        "file": "firefox_privacy_notice.md",
        "url": "https://www.mozilla.org/privacy/firefox/",
        "class": "link-current-pn",
        "link_to": "preview",
    },
    "preview": {
        "file": "firefox_privacy_notice_preview.md",
        "url": "https://www.mozilla.org/privacy/firefox/next",
        "class": "link-next-pn",
        "link_to": "current",
    },
}

# Localized text of links pointing to each version
PREAMBLES = {
    "cs": {
        "preview": "Aktualizujeme naše Oznámení o ochraně osobních údajů. Kliknutím sem zobrazíte novou verzi.",
        "current": "Pro zobrazení našeho aktuálního oznámení klikněte sem.",
    },
    "de": {
        "preview": "Wir aktualisieren unseren Datenschutzhinweis. Klicken Sie hier, um die neue Version anzuzeigen.",
        "current": "Zum Anzeigen unseres aktuellen Hinweises hier klicken.",
    },
    "en": {
        "preview": "We’re updating our Privacy Notice. Click here to see the new version.",
        "current": "To see our current notice, click here.",
    },
    "es-ES": {
        "preview": "Estamos actualizando nuestro Aviso de privacidad. Haga clic aquí para ver la nueva versión.",
        "current": "Para ver nuestro aviso corriente, haga clic aquí.",
    },
    "fr": {
        "preview": "Nous avons mis à jour notre Politique de confidentialité. Cliquez ici pour voir la nouvelle version.",
        "current": "Pour consulter notre politique actuelle, cliquez ici.",
    },
    "hu": {
        "preview": "Frissítjük az adatvédelmi nyilatkozatunkat. Kattintson ide az új verzió megtekintéséhez.",
        "current": "A jelenlegi nyilatkozat megtekintéséhez kattintson ide.",
    },
    "id": {
        "preview": "Kami memperbarui Pemberitahuan Privasi kami. Klik di sini untuk melihat versi barunya.",
        "current": "Untuk melihat pemberitahuan terbaru kami, klik di sini.",
    },
    "it": {
        "preview": "Stiamo aggiornando la nostra Informativa sulla privacy. Fai clic qui per vedere la nuova versione.",
        "current": "Per consultare la nostra attuale informativa, fai clic qui.",
    },
    "ja": {
        "preview": "プライバシーに関する通知を更新しました。新しいバージョンを表示するには、こちらをクリックしてください。",
        "current": "最新版の通知を表示するには、こちらをクリックします。",
    },
    "nl": {
        "preview": "We werken onze privacyverklaring bij. Klik hier om de nieuwe versie te bekijken.",
        "current": "Klik hier als u onze huidige verklaring wilt weergeven.",
    },
    "pl": {
        "preview": "Aktualizujemy nasze Zasady prywatności. Kliknij tutaj, aby zobaczyć nową wersję.",
        "current": "Aby zobaczyć aktualne Zasady, kliknij tutaj.",
    },
    "pt-BR": {
        "preview": "Estamos atualizando nosso Aviso de privacidade. Clique aqui para consultar a nova versão.",
        "current": "Clique aqui para acessar nosso aviso atual.",
    },
    "ru": {
        "preview": "Мы обновляем наше Уведомление о конфиденциальности. Нажмите здесь, чтобы ознакомиться с новой версией.",
        "current": "Для знакомства с нашим текущим уведомлением нажмите здесь.",
    },
    "zh-CN": {
        "preview": "我们正在更新《隐私声明》。点击此处查看新版本。",
        "current": "如需查看当前声明，请点击此处。",
    },
}

DATE_PATTERN = re.compile(r"{:\s?datetime=")


def is_preamble(line):
    return any(notice["class"] in line for notice in NOTICES.values())


def read_lines(file_path):
    return file_path.read_text(encoding="utf-8").splitlines()


def write_lines(file_path, lines):
    file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def remove_preamble(lines):
    """Remove preamble lines, and the blank line following each of them."""

    new_lines = []
    skip_blank = False
    for line in lines:
        if is_preamble(line):
            # Drop the blank line before the preamble as well
            if new_lines and new_lines[-1].strip() == "":
                new_lines.pop()
            skip_blank = True
            continue
        if skip_blank:
            skip_blank = False
            if line.strip() != "":
                # Preserve separation from the following content
                new_lines.append("")
        new_lines.append(line)

    return new_lines


def add_preamble(file_path, class_name, href, text):
    lines = remove_preamble(read_lines(file_path))

    date_idx = next(
        (i for i, line in enumerate(lines) if DATE_PATTERN.search(line)), None
    )
    if date_idx is None:
        print(f"  WARNING: effective date not found in {file_path}")
        return False

    # Remove blank lines after the effective date, then insert the preamble
    # surrounded by blank lines.
    insert_at = date_idx + 1
    while insert_at < len(lines) and lines[insert_at].strip() == "":
        del lines[insert_at]
    lines[insert_at:insert_at] = [
        "",
        f'<a class="{class_name}" href="{href}">{text}</a>',
        "",
    ]
    write_lines(file_path, lines)

    return True


def copy_notices(root, source, dest):
    """Copy the source version over the dest version for all locales."""

    for source_path in sorted(root.glob(f"*/{NOTICES[source]['file']}")):
        dest_path = source_path.with_name(NOTICES[dest]["file"])
        # Don't carry over the preamble from the source
        write_lines(dest_path, remove_preamble(read_lines(source_path)))
        print(
            f"Copied {source_path.relative_to(root)} to {dest_path.relative_to(root)}"
        )


def add_preambles(root, versions=NOTICES.keys()):
    for locale, texts in PREAMBLES.items():
        for version in versions:
            notice = NOTICES[version]
            file_path = root / locale / notice["file"]
            if not file_path.exists():
                print(f"  Skipping missing file: {file_path.relative_to(root)}")
                continue
            target = notice["link_to"]
            if add_preamble(
                file_path,
                NOTICES[target]["class"],
                NOTICES[target]["url"],
                texts[target],
            ):
                print(f"Added preamble to {file_path.relative_to(root)}")


def main():
    parser = argparse.ArgumentParser(
        description="Manage the preview of the Firefox Privacy Notice and its preambles"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--create",
        "-create",
        action="store_true",
        help="Create the preview from the current notice for all locales, with preamble",
    )
    group.add_argument("--add", "-add", action="store_true", help="Add preambles")
    group.add_argument(
        "--publish",
        "-publish",
        action="store_true",
        help="Replace the current notice with the preview for all locales",
    )
    args = parser.parse_args()

    # Repository root is two levels above .github/scripts
    root = Path(__file__).resolve().parents[2]

    if args.create:
        copy_notices(root, "current", "preview")
        add_preambles(root, ["preview"])
    elif args.add:
        add_preambles(root)
    else:
        copy_notices(root, "preview", "current")

    return 0


if __name__ == "__main__":
    sys.exit(main())
