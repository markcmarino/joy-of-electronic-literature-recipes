#!/usr/bin/env python3
"""
Detect and fix minified/inline YAML front matter in recipe files.
No external dependencies required.

Handles cases where:
- Opening delimiter is glued to content: --- title: ... chef: ...
- Closing delimiter is glued to body: github_link: ... --- ## Ingredients
- YAML keys/values are on wrong lines or compressed
"""

import os
import re
import sys

def detect_issues(filepath):
    """Detect front matter formatting issues."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    issues = []

    if not lines or not lines[0].startswith('---'):
        return []

    # Issue 1: Opening delimiter has content glued to it
    if len(lines[0].strip()) > 3:
        issues.append('opening_glued')

    # Issue 2: Look for closing delimiter glued to body
    for i, line in enumerate(lines[1:50], 1):  # Check first 50 lines
        if '---' in line and '##' in line:
            issues.append('closing_glued')
            break

    # Issue 3: Multiple YAML keys on one line
    for i, line in enumerate(lines[1:50], 1):
        if line.strip() == '---':
            break
        # Look for pattern like "key1: value1 key2: value2"
        if ':' in line:
            parts = line.split()
            colon_count = sum(1 for p in parts if ':' in p)
            if colon_count > 1:
                issues.append('multiple_keys_per_line')
                break

    return issues

def fix_frontmatter(filepath):
    """Fix minified front matter by ensuring proper structure."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    if not lines or not lines[0].startswith('---'):
        return False, "no_frontmatter"

    # Find front matter boundaries
    yaml_start = 0
    yaml_end = None

    # Fix opening delimiter if needed
    first_line = lines[0]
    if len(first_line.strip()) > 3:
        # Content glued to opening ---, e.g., "--- title: Something"
        remainder = first_line[3:].strip()
        lines[0] = '---'
        lines.insert(1, remainder)

    # Find closing delimiter
    for i in range(1, min(len(lines), 100)):
        line = lines[i]

        # Check if closing --- is glued to body
        if '---' in line and '##' in line:
            # e.g., "github_link: http://... --- ## Ingredients"
            parts = line.split('---', 1)
            yaml_part = parts[0].strip()
            body_part = parts[1].strip() if len(parts) > 1 else ''

            lines[i] = yaml_part
            lines.insert(i + 1, '---')
            if body_part:
                lines.insert(i + 2, body_part)
            yaml_end = i + 1
            break

        elif line.strip() == '---':
            yaml_end = i
            break

    if yaml_end is None:
        return False, "no_closing_delimiter"

    # Extract YAML block and body
    yaml_lines = lines[yaml_start + 1:yaml_end]
    body_lines = lines[yaml_end + 1:]

    # Process YAML lines to ensure proper formatting
    # (This is a simple approach - just ensure each key is on its own line)
    processed_yaml = []

    for line in yaml_lines:
        # Handle multiple keys on one line (simple case)
        # This is a basic split - may not handle all edge cases
        if line.count(':') > 1 and not line.strip().startswith('-'):
            # Try to split into multiple lines
            # This is crude but handles simple cases
            parts = re.split(r'(\w+:)', line)
            current = ''
            for part in parts:
                if part.endswith(':'):
                    if current:
                        processed_yaml.append(current.strip())
                    current = part
                else:
                    current += part
            if current:
                processed_yaml.append(current.strip())
        else:
            processed_yaml.append(line)

    # Rebuild content
    new_content_parts = ['---'] + processed_yaml + ['---', ''] + body_lines
    new_content = '\n'.join(new_content_parts)

    # Remove any extra blank lines at start of body
    new_content = re.sub(r'---\n\n+', '---\n\n', new_content)

    # Write back
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)

    return True, "fixed"

def main():
    """Process all recipe files."""
    recipe_dir = 'docs/recipes'

    if not os.path.exists(recipe_dir):
        print(f"❌ Recipe directory not found: {recipe_dir}")
        sys.exit(1)

    files_checked = 0
    files_with_issues = 0
    files_fixed = 0
    files_failed = 0

    print("Checking recipe files for minified front matter...\n")

    for filename in sorted(os.listdir(recipe_dir)):
        if filename.endswith('.md') and filename != '_template.md':
            filepath = os.path.join(recipe_dir, filename)
            files_checked += 1

            issues = detect_issues(filepath)

            if issues:
                files_with_issues += 1
                print(f"⚠️  {filename}: {', '.join(issues)}")

                success, result = fix_frontmatter(filepath)

                if success:
                    files_fixed += 1
                    print(f"   ✅ Fixed")
                else:
                    files_failed += 1
                    print(f"   ❌ Failed: {result}")
            else:
                print(f"✓  {filename}")

    # Summary
    print()
    print(f"{'='*60}")
    print(f"Files checked: {files_checked}")
    print(f"Files with issues: {files_with_issues}")
    print(f"Files fixed: {files_fixed}")
    print(f"Files failed: {files_failed}")
    print(f"{'='*60}")

    if files_fixed > 0:
        print(f"\n✅ Fixed {files_fixed} file(s) with minified front matter")
    else:
        print(f"\n✅ No minified front matter found - all files OK!")

    sys.exit(0 if files_failed == 0 else 1)

if __name__ == '__main__':
    main()
