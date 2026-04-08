#!/usr/bin/env python3
"""Copy refreshed EN HTML into locale folders: paths, lang, scoped absolute URLs."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "index.html",
    "guides.html",
    "news.html",
    "contact.html",
    "spreadsheet.html",
    "sugargoo-spreadsheet-qc.html",
    "sugargoo-spreadsheet-dead-links.html",
    "sugargoo-spreadsheet-shipping-weight.html",
]

LOCALES = ("pl", "es", "de", "pt")
LANG_ATTR = {"pl": "pl", "es": "es", "de": "de", "pt": "pt-PT"}


def scope_urls(html: str, folder: str) -> str:
    """Scope https://sugargooospreadsheet.com/... to /{folder}/... without touching other locales."""
    tokens = {}
    for loc in LOCALES:
        key = f"__LOC_{loc.upper()}__"
        needle = f"https://sugargooospreadsheet.com/{loc}/"
        if needle in html:
            html = html.replace(needle, key)
            tokens[key] = needle
    html = html.replace(
        "https://sugargooospreadsheet.com/",
        f"https://sugargooospreadsheet.com/{folder}/",
    )
    for key, val in tokens.items():
        html = html.replace(key, val)
    return html


def patch(html: str, folder: str) -> str:
    out = html.replace('lang="en"', f'lang="{LANG_ATTR[folder]}"', 1)
    out = out.replace('href="images/', 'href="../images/')
    out = out.replace("href='images/", "href='../images/")
    out = out.replace('href="styles.css', 'href="../styles.css')
    return scope_urls(out, folder)


def main() -> None:
    for name in FILES:
        src = (ROOT / name).read_text(encoding="utf-8")
        for folder in LOCALES:
            out = patch(src, folder)
            dest = ROOT / folder / name
            dest.write_text(out, encoding="utf-8")
            print("wrote", dest.relative_to(ROOT))


if __name__ == "__main__":
    main()
