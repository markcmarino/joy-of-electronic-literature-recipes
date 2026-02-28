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

## Completed Recipes (27 of ~25)

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

Note: "2.5 Montfort" (Cooking Computational Literature, line ~2258) is an essay/interlude,
not a standard recipe — omitted from recipe files.

---

## Remaining Recipes (pick up from line ~5234)

| Author | Approx. line | Title (from source) |
|--------|-------------|---------------------|
| Tisselli | 5234 | Degenerative |
| (unknown) | 5414 | Netprov recipe |
| (unknown) | 5591 | Less-Thought |

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
