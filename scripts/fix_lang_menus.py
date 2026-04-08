#!/usr/bin/env python3
"""Rewrite language switcher blocks to absolute URLs + correct aria-current."""
from __future__ import annotations

import re
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


def href_en(name: str) -> str:
    return "/" if name == "index.html" else f"/{name}"


def href_loc(name: str, loc: str) -> str:
    if name == "index.html":
        return f"/{loc}/"
    return f"/{loc}/{name}"


def menu_block(filename: str, current: str) -> str:
    specs = [
        ("EN", "en", None),
        ("PL", "pl", "pl"),
        ("PT", "pt", "pt-PT"),
        ("ES", "es", "es"),
        ("DE", "de", "de"),
    ]
    lines = ['          <div class="lang-menu" role="menu">']
    for label, loc_id, lang in specs:
        h = href_en(filename) if loc_id == "en" else href_loc(filename, loc_id)
        cur = ' aria-current="page"' if current == loc_id else ""
        lang_attr = f' lang="{lang}"' if lang else ""
        lines.append(f'            <a href="{h}"{cur}{lang_attr}>{label}</a>')
    lines.append("          </div>")
    return "\n".join(lines)


def fix_file(path: Path, filename: str, current_loc: str) -> None:
    text = path.read_text(encoding="utf-8")
    block = menu_block(filename, current_loc)
    text2 = re.sub(
        r'<div class="lang-menu" role="menu">.*?</div>',
        block,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if text2 == text:
        raise RuntimeError(f"no lang-menu replaced: {path}")
    path.write_text(text2, encoding="utf-8")


def main() -> None:
    for loc in LOCALES:
        for name in FILES:
            fix_file(ROOT / loc / name, name, loc)


if __name__ == "__main__":
    main()
