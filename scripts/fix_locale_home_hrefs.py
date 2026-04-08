#!/usr/bin/env python3
"""Point in-locale nav/brand/breadcrumbs to /{locale}/ without touching lang-switcher EN link."""
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


def patch(text: str, loc: str) -> str:
    p = f"/{loc}/"
    text = text.replace('<a class="brand" href="/"', f'<a class="brand" href="{p}"')
    text = text.replace('<li><a href="/" aria-current="page">Home</a></li>', f'<li><a href="{p}" aria-current="page">Home</a></li>')
    text = text.replace('<li><a href="/">Home</a></li>', f'<li><a href="{p}">Home</a></li>')
    text = text.replace('<a class="btn btn-ghost" href="/">Back to home</a>', f'<a class="btn btn-ghost" href="{p}">Back to home</a>')
    text = text.replace('<a class="related-link-card" href="/">', f'<a class="related-link-card" href="{p}">')
    text = text.replace('<div class="footer-links"><a href="/">Home</a></div>', f'<div class="footer-links"><a href="{p}">Home</a></div>')
    # Breadcrumbs + generic footer home (after nav-specific replacements)
    text = text.replace('<a href="/">Home</a>', f'<a href="{p}">Home</a>')
    text = text.replace('<a href="/">sugargoo spreadsheet</a>', f'<a href="{p}">sugargoo spreadsheet</a>')
    return text


def main() -> None:
    for loc in LOCALES:
        for name in FILES:
            path = ROOT / loc / name
            path.write_text(patch(path.read_text(encoding="utf-8"), loc), encoding="utf-8")
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
