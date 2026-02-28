#!/usr/bin/env python3
"""Validate recipe YAML front matter for Joy of Electronic Literature Recipes."""

import re
import sys
import glob
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

OFFICIAL_GENRES = {
    "Generative Poetry",
    "Hypertext",
    "VR",
    "Netprov",
    "Audio",
    "Augmented Reality",
    "Word Manipulation",
    "Performance/Experience",
    "Human-computer collaboration",
    "Machine reading",
}

URL_RE = re.compile(r"^https?://\S+$")

REQUIRED_FIELDS = [
    "title", "chef", "abstract", "description",
    "genres", "difficulty_pans", "yields", "github_link",
]

WORD_LIMITS = {
    "title": 10,
    "chef": 5,
    "abstract": 25,
    "description": 250,
    "yields": 50,
}


def word_count(text):
    return len(str(text).split())


def validate(path):
    errors = []
    text = Path(path).read_text(encoding="utf-8")

    if not text.startswith("---"):
        return ["Missing YAML front matter (file must start with ---)"]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return ["Malformed front matter: missing closing ---"]

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return [f"YAML parse error: {e}"]

    if not isinstance(meta, dict):
        return ["Front matter is not a YAML mapping"]

    # Required fields
    missing = [f for f in REQUIRED_FIELDS if f not in meta or meta[f] is None]
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")
        return errors  # Can't validate further without required fields

    # Word limits
    for field, limit in WORD_LIMITS.items():
        wc = word_count(meta[field])
        if wc > limit:
            errors.append(f"`{field}` is {wc} words (max {limit})")

    # genres: non-empty list, all values must be official genres
    genres = meta["genres"]
    if not isinstance(genres, list) or not genres:
        errors.append("`genres` must be a non-empty list")
    else:
        invalid = [g for g in genres if g not in OFFICIAL_GENRES]
        if invalid:
            errors.append(
                f"Unrecognized value(s) in `genres` — use `custom_genres` for free-text genres: {invalid}\n"
                f"  Official genres: {sorted(OFFICIAL_GENRES)}"
            )

    # difficulty_pans: integer, 1–4
    dp = meta["difficulty_pans"]
    if isinstance(dp, bool) or not isinstance(dp, int):
        errors.append(f"`difficulty_pans` must be an integer, got: {type(dp).__name__}")
    elif not (1 <= dp <= 4):
        errors.append(f"`difficulty_pans` must be 1–4, got: {dp}")

    # github_link: valid URL
    link = str(meta["github_link"])
    if not URL_RE.match(link):
        errors.append(f"`github_link` is not a valid URL: {link}")

    return errors


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = glob.glob("docs/recipes/*.md")

    # Skip template/private files (prefixed with _)
    files = [f for f in files if not Path(f).name.startswith("_")]

    if not files:
        print("No recipe files found.")
        sys.exit(0)

    failed = []
    for path in sorted(files):
        errors = validate(path)
        if errors:
            failed.append(path)
            print(f"FAIL  {path}")
            for e in errors:
                print(f"      • {e}")
        else:
            print(f"OK    {path}")

    print()
    if failed:
        print(f"{len(failed)} file(s) failed validation.")
        sys.exit(1)
    else:
        print(f"All {len(files)} recipe(s) valid.")


if __name__ == "__main__":
    main()
