# Recipe Transfer Notes

A handoff document for continuing the transfer of recipes from the source
Google Doc into this repository.

---

## Source File

`D:/Downloads/JOEL Recipes complete.txt`

This is a plain text export of the Google Doc "JOEL Recipes complete."
The file is ~417KB and must be read in chunks (limit 300–400 lines at a time)
using the Read tool with `offset` and `limit` parameters.

---

## How Recipes Are Structured in the Source File

Each recipe section begins with a header like:

```
2-Abrahams
Distant Feeling(s) - a recipe
Annie Abrahams
...
Class of E-lit: Performance, mindfulness, training
Dish: ...
Required ingredients: ...
Rating: 🍳 Easy
```

The `2-LastName` label is a section marker used in the source doc — ignore it.
Recipe content continues until the next `2-LastName` marker.

---

## YAML Fields to Fill

| Field | Constraint | Notes |
|-------|-----------|-------|
| `title` | Max 10 words | Usually the recipe title |
| `chef` | Max 5 words | Author name(s) only, no titles |
| `abstract` | 1 sentence, max 25 words | Write fresh from the content |
| `description` | Max 250 words | Synthesize from Background section |
| `genres` | Official list only | Map from "Class of E-lit" field |
| `custom_genres` | Optional, free text | Add if needed |
| `difficulty_pans` | Integer 1–4 | Count the 🍳 pan emojis in Rating |
| `yields` | Max 50 words | Write fresh from "Dish" + body |
| `github_link` | Valid URL | Use project/demo URL if no GitHub link |

### Official Genre Mappings from Source Doc

| "Class of E-lit" label in source | Use this official genre |
|-----------------------------------|------------------------|
| Text Generators / Text modulator | Generative Poetry |
| Human~computer collaboration | Human-computer collaboration |
| Machine reading | Machine reading |
| Audio AR / Audio | Audio |
| Augmented Reality / AR | Augmented Reality |
| Hypertext / Interactive Fiction / Twine | Hypertext |
| Performance / Telematic | Performance/Experience |
| E-Poetry / Word manipulation | Word Manipulation |
| Netprov | Netprov |

### github_link Placeholder Strategy

If no GitHub or project URL is given in the source, use the closest available
URL (demo link, project page, app URL). If truly none exists, use:
`https://github.com/placeholder` and flag it in the commit message.

---

## File Naming Convention

Slugs are lowercase, hyphenated, based on recipe title:

```
docs/recipes/distant-feelings.md
docs/recipes/minimal-algorithmic-editor.md
```

Skip `_template.md` — it is not a recipe.

---

## Completed Recipes (30 of 30) ✅

| File | Chef(s) |
|------|---------|
| `literary-dish-generator.md` | Rhee & Marino |
| `distant-feelings.md` | Abrahams |
| `minimal-algorithmic-editor.md` | Booten |
| `full-words-ramble.md` | Cayley-Howe |
| `radical-atmospheres.md` | Demirjian |
| `human-in-the-soup.md` | Klobucar |
| `unleashing-linking-powers.md` | Larsen |
| `interactive-lyric-videos.md` | Loyer |
| `kids-in-the-kitchen.md` | Skains |
| `chatting-in-the-funhouse.md` | McDaid |
| `ai-as-mirror.md` | Wang |
| `gastropoetic-generator.md` | Memmott & Rettberg |
| `jolly-apogee.md` | Morrissey |
| `labeling.md` | Parrish |
| `a-la-recherche-du-lieu-perdu.md` | Klimas |
| `choice-constrained-twine.md` | Salter |
| `mashed-soup.md` | Pintar |
| `arabian-labyrinth.md` | Veeder |
| `cyborg-digital-writing.md` | Flores |
| `online-survey-poems.md` | Saum-Pascual |
| `queering-bash.md` | Soon & Karagianni |
| `deformances.md` | Tschofen |
| `citation-cake.md` | Strickland & Hatcher |
| `modest-beginnings.md` | Vilaplana |
| `disappearing-recipe.md` | Gero |
| `poemscape.md` | Wilks |
| `soul-stew.md` | Torres |
| `degenerative.md` | Tisselli |
| `pr0c3ss1ng.md` | Wittig & Marino |
| `less-thought.md` | Johnston |

Note: "2.5 Montfort" (Cooking Computational Literature, line ~2258) is an essay/interlude,
not a standard recipe — omitted from recipe files.

---

## Remaining Recipes

**✅ ALL RECIPES COMPLETED!**

The transfer is complete. All 30 recipes from the source file have been successfully migrated to the repository.

---

## Workflow Per Session

1. Check `docs/recipes/` to confirm what's already done.
2. Read the source file in chunks starting from the first unprocessed recipe.
3. Create 4–5 recipe `.md` files.
4. Commit and push with message like:
   `Add batch N recipes: Name1, Name2, Name3`
5. Stop when context reaches ~75–80%, or after a clean batch boundary.

---

## Repository

- **Local path:** `C:/Users/mcmarino/joy-of-eliterature-recipes/`
- **GitHub:** `https://github.com/markcmarino/joy-of-electronic-literature-recipes`
- **Validation:** runs automatically on every PR via GitHub Actions
- **Python:** not installed locally — validation only runs on GitHub

---

## Current Status (February 2026)

### ✅ Completed Work

**Recipe Transfer & Verification:**
- All 30 recipes successfully transferred from source file to repository
- README table of contents created with alphabetical organization by chef last name
- Chef names verified against source file and corrected (7 errors fixed)

**YAML Frontmatter Quality Assurance:**
- Stripped UTF-8 BOM from all recipe files
- Normalized line endings (CRLF → LF) across all `.md`, `.yml`, `.py` files
- Converted YAML prose fields from literal (`|`) to folded (`>`) style for better data export
- Fixed minified YAML in `ai-as-mirror.md` (complete file rewrite)
- Added `.gitattributes` to enforce LF line endings going forward
- Created `validate_frontmatter.py` validation script
- Integrated frontmatter validation into GitHub Actions CI workflow

**Display & Presentation:**
- Created `docs/stylesheets/recipes.css` for vertical metadata display
- Updated `mkdocs.yml` to include custom CSS via `extra_css`
- CSS-only solution preserves YAML structure for document extraction
- Removed contributor sections from README (closing public submissions temporarily)

**Validation Infrastructure:**
- `.github/scripts/validate_frontmatter.py` - checks BOM, delimiters, line endings
- `.github/scripts/unminify_frontmatter_simple.py` - detects and fixes minified YAML
- `.github/workflows/validate-recipes.yml` - automated CI checks on PRs
- `scripts/validate_recipes.py` - content validation (existing)

---

## Next Steps: Document Generation from YAML

### Goal
Extract YAML frontmatter from all 30 recipe files to create formatted documents (likely for Google Docs or other publication formats).

### Current YAML Structure (Ready for Extraction)

All recipe files have clean, well-formed YAML frontmatter with these fields:

```yaml
---
title: Recipe Title Here
chef: Author Name(s)
abstract: One sentence, max 25 words
description: >
  Fuller description up to 250 words, using folded style.
  Multiple paragraphs supported with blank lines.
genres:
  - Official Genre Name
custom_genres:
  - Custom Genre (optional)
difficulty_pans: 1-4
yields: >
  What the reader experiences, up to 50 words.
github_link: https://project-url.com
---
```

### Extraction Options

**Option 1: Python Script for Bulk Export**
- Read all 30 recipe files in `docs/recipes/*.md`
- Parse YAML frontmatter using `pyyaml` library
- Export to CSV, JSON, or formatted text for import into Google Docs/Sheets
- Preserves all metadata fields for batch processing

**Option 2: Manual Google Docs Integration**
- Use MkDocs metadata display on published site
- Copy/paste from rendered pages (metadata will display vertically via CSS)
- Import into Google Docs template with consistent formatting

**Option 3: Direct Markdown → DOCX Conversion**
- Use Pandoc to convert `.md` files to `.docx` format
- Preserve YAML metadata as document properties or formatted header
- Batch process all 30 recipes at once

### Required Decisions

Before proceeding with document generation:

1. **Output Format:** What format do you need? (Google Docs, Word, PDF, CSV/database)
2. **Metadata Display:** How should YAML fields appear in the final documents?
3. **Body Content:** Include markdown body content or metadata only?
4. **Template:** Do you have a specific document template/style guide to match?
5. **Batch vs. Individual:** Generate one master document or 30 individual files?

### Files Ready for Extraction

All 30 recipe files have validated, clean YAML frontmatter:
- No BOM markers
- LF line endings only
- Proper `---` delimiters
- Folded style (`>`) for prose fields
- All required fields present

**Next action:** Determine output format and extraction method based on your publishing workflow.
