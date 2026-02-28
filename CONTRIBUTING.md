# Contributing a Recipe

1. Copy [`docs/recipes/_template.md`](docs/recipes/_template.md) to `docs/recipes/your-slug.md`.
2. Fill in all required YAML front matter fields (see below).
3. Write your recipe body in Markdown below the front matter — no structure enforced.
4. Open a Pull Request. Validation runs automatically; the PR will fail if any fields are missing or invalid.

---

## YAML Fields

| Field | Required | Constraint |
|-------|----------|------------|
| `title` | Yes | Max 10 words |
| `chef` | Yes | Max 5 words |
| `abstract` | Yes | 1 sentence, max 25 words |
| `description` | Yes | Max 250 words |
| `genres` | Yes | Non-empty list; values must be from the official list below |
| `custom_genres` | No | Free text, any values |
| `difficulty_pans` | Yes | Integer 1–4 |
| `yields` | Yes | 1–2 sentences, max 50 words |
| `github_link` | Yes | Valid URL |

---

## Official Genres

At least one entry in `genres` must be from this list exactly:

- Generative Poetry
- Hypertext
- VR
- Netprov
- Audio
- Augmented Reality
- Word Manipulation
- Performance/Experience
- Human-computer collaboration
- Machine reading

For anything else, use `custom_genres`.
