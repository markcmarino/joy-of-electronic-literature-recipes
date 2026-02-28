#!/usr/bin/env python3
"""Export recipe front matter to CSV."""

import csv
import glob
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pip install pyyaml")
    sys.exit(1)

FIELDS = [
    "slug", "title", "chef", "abstract", "description",
    "genres", "custom_genres", "difficulty_pans", "yields", "github_link",
]


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        meta = yaml.safe_load(parts[1])
        if not isinstance(meta, dict):
            return None
        meta["slug"] = Path(path).stem
        # Flatten lists to semicolon-separated strings for CSV
        for key in ("genres", "custom_genres"):
            if isinstance(meta.get(key), list):
                meta[key] = "; ".join(meta[key])
        return meta
    except yaml.YAMLError:
        return None


def main():
    files = sorted(glob.glob("docs/recipes/*.md"))
    files = [f for f in files if not Path(f).name.startswith("_")]

    out = sys.argv[1] if len(sys.argv) > 1 else "recipes.csv"

    rows = [load(f) for f in files]
    rows = [r for r in rows if r]

    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} recipe(s) to {out}")


if __name__ == "__main__":
    main()
