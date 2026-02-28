#!/usr/bin/env python3
"""
Generate a recipe-cards Markdown file (metadata only) for Pandoc → DOCX export.

Usage:
    python scripts/export_cards.py           # writes recipe_cards.md
    python scripts/export_cards.py out.md    # custom output path

Then convert to DOCX:
    pandoc recipe_cards.md -o recipe_cards.docx
"""

import glob
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pip install pyyaml")
    sys.exit(1)


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        meta = yaml.safe_load(parts[1])
        return meta if isinstance(meta, dict) else None
    except yaml.YAMLError:
        return None


def flatten_list(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value) if value else ""


def render_card(meta):
    genres = flatten_list(meta.get("genres", []))
    custom = flatten_list(meta.get("custom_genres", []))
    all_genres = ", ".join(filter(None, [genres, custom]))

    dp = meta.get("difficulty_pans", "?")
    pans = ("pan " * int(dp)).strip() if isinstance(dp, int) else str(dp)

    return "\n".join([
        f"# {meta.get('title', 'Untitled')}",
        "",
        f"**Chef:** {meta.get('chef', '')}  ",
        f"**Genres:** {all_genres}  ",
        f"**Difficulty:** {pans} ({dp}/4)",
        "",
        f"*{meta.get('abstract', '')}*",
        "",
        "**Description**",
        "",
        str(meta.get("description", "")).strip(),
        "",
        "**Yields**",
        "",
        str(meta.get("yields", "")).strip(),
        "",
        f"**GitHub:** {meta.get('github_link', '')}",
        "",
        "---",
        "",
    ])


def main():
    files = sorted(glob.glob("docs/recipes/*.md"))
    files = [f for f in files if not Path(f).name.startswith("_")]

    out = sys.argv[1] if len(sys.argv) > 1 else "recipe_cards.md"

    with open(out, "w", encoding="utf-8") as f:
        f.write("---\ntitle: Joy of Electronic Literature — Recipe Cards\n---\n\n")
        count = 0
        for path in files:
            meta = load(path)
            if meta:
                f.write(render_card(meta))
                count += 1

    print(f"Generated {out} with {count} recipe card(s).")
    print(f"Convert to DOCX with:")
    print(f"  pandoc {out} -o recipe_cards.docx")


if __name__ == "__main__":
    main()
