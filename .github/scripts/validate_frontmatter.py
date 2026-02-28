#!/usr/bin/env python3
"""
Validate YAML front matter format in recipe files.

Ensures:
- No UTF-8 BOM before ---
- File starts with exactly --- on first line
- No leading whitespace or blank lines
- Proper closing --- exists
"""

import sys
import os

def validate_frontmatter_format(filepath):
    """Check if file starts correctly for MkDocs YAML parsing."""

    # Read as binary to check for BOM
    with open(filepath, 'rb') as f:
        first_bytes = f.read(3)
        if first_bytes.startswith(b'\xef\xbb\xbf'):
            return False, "UTF-8 BOM detected before ---"

    # Read as text to check structure
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        if len(lines) < 2:
            return False, "File too short to contain front matter"

        # First line must be exactly "---\n"
        if lines[0] != '---\n':
            if lines[0].startswith(' ') or lines[0].startswith('\t'):
                return False, "Leading whitespace before ---"
            if lines[0] == '\n':
                return False, "Blank line before ---"
            if not lines[0].startswith('---'):
                return False, "File does not start with ---"
            return False, f"First line malformed: {repr(lines[0])}"

        # Find closing ---
        closing_index = None
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == '---':
                closing_index = i
                break

        if closing_index is None:
            return False, "No closing --- found"

        # Check for CRLF line endings (should all be LF)
        content = ''.join(lines)
        if '\r\n' in content:
            return False, "CRLF line endings detected (should be LF only)"

    return True, "Front matter format OK"

def main():
    """Validate all recipe files."""
    recipe_dir = 'docs/recipes'

    if not os.path.exists(recipe_dir):
        print(f"❌ Recipe directory not found: {recipe_dir}")
        sys.exit(1)

    failed = []
    passed = []

    for filename in sorted(os.listdir(recipe_dir)):
        if filename.endswith('.md') and filename != '_template.md':
            filepath = os.path.join(recipe_dir, filename)
            ok, msg = validate_frontmatter_format(filepath)

            if ok:
                print(f"✅ {filename}")
                passed.append(filename)
            else:
                print(f"❌ {filename}: {msg}")
                failed.append((filename, msg))

    # Summary
    print()
    print(f"{'='*60}")
    print(f"✅ Passed: {len(passed)}")
    print(f"❌ Failed: {len(failed)}")
    print(f"{'='*60}")

    if failed:
        print("\nFailed files:")
        for filename, msg in failed:
            print(f"  • {filename}: {msg}")
        sys.exit(1)
    else:
        print("\n✅ All recipe files have valid front matter format!")
        sys.exit(0)

if __name__ == '__main__':
    main()
