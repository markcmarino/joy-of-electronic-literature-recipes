# Joy of Electronic Literature Recipes — Contributor Guide

Thank you for contributing to the *Joy of Electronic Literature Recipes* — a
collaborative cookbook documenting works of electronic literature as shareable,
structured recipes.

This guide walks you through everything you need to submit your recipe.

---

## What Is a Recipe?

Each recipe documents an electronic literature work — yours or one you know well.
It has two parts:

1. **A short metadata card** (structured fields we validate automatically)
2. **A free-form body** in Markdown (ingredients, method, notes — write as much
   or as little as you like, in whatever structure makes sense for the work)

---

## What You'll Need

- A **GitHub account** (free at [github.com](https://github.com))
- Basic comfort editing a text file (no coding required)

---

## Step-by-Step Submission

### 1. Fork the repository

Go to the project repository on GitHub and click **Fork** (top right). This
creates your own copy to work in.

### 2. Create your recipe file

Inside your fork, navigate to `docs/recipes/`. You'll see `_template.md` there.

Click the **+** button to create a new file in the same folder. Name it using a
short, lowercase, hyphenated slug based on your work's title:

```
docs/recipes/my-work-title.md
```

### 3. Copy the template

Open `_template.md`, copy its entire contents, and paste them into your new
file. Then fill in your details (see field guide below).

### 4. Write your recipe body

Below the closing `---` of the front matter, write freely in Markdown. You might
include sections like **Ingredients**, **Method**, and **Notes** — but these are
suggestions, not requirements. Write whatever best captures the work.

### 5. Submit a Pull Request

When you're ready, open a **Pull Request** from your fork back to the main
repository. An automated check will run immediately and flag any issues with
your metadata. If everything passes, your recipe will be reviewed and merged.

---

## Metadata Field Guide

At the top of your recipe file you'll find a block of structured fields between
`---` markers. Here's what each one means:

---

**`title`** *(required, max 10 words)*

The title of the electronic literature work.

```yaml
title: Taroko Gorge
```

---

**`chef`** *(required, max 5 words)*

Your name, or the name you'd like credited.

```yaml
chef: Nick Montfort
```

---

**`abstract`** *(required — 1 sentence, max 25 words)*

One sentence that captures what the work is or does.

```yaml
abstract: A generative poem that endlessly produces descriptions of a Taiwanese
  gorge using looping, substitutable language.
```

---

**`description`** *(required, max 250 words)*

A fuller description: what the work is, how it works, what makes it interesting.
Write in plain prose. The `|` symbol lets you write across multiple lines.

```yaml
description: |
  Taroko Gorge is a poetry generator written in JavaScript by Nick Montfort
  in 2009. It produces an endless stream of verse by recombining a small set
  of words and syntactic templates inspired by the landscape of Taroko Gorge
  National Park in Taiwan...
```

---

**`genres`** *(required — list, values must match official genres exactly)*

One or more genres from the official list below. Values must match exactly —
spelling, capitalisation, and all.

```yaml
genres:
  - Generative Poetry
```

If your work crosses genres, list all that apply:

```yaml
genres:
  - Generative Poetry
  - Hypertext
```

**Official genres (copy exactly):**

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

---

**`custom_genres`** *(optional — free text)*

If none of the official genres quite fits, add your own here. You can use both.

```yaml
custom_genres:
  - Landscape Writing
  - Constraint-based
```

---

**`difficulty_pans`** *(required — whole number, 1 to 4)*

How difficult is this work to create or recreate? Rate it 1 (accessible) to 4
(highly technical or resource-intensive). Think of it like a cooking difficulty
rating — one pan vs. four.

```yaml
difficulty_pans: 2
```

---

**`yields`** *(required — 1 to 2 sentences, max 50 words)*

What does a reader or participant get from this work? What is the experience?

```yaml
yields: |
  An endlessly running browser poem, readable in any web browser, that produces
  new stanzas with each page refresh or continuously as the page runs.
```

---

**`github_link`** *(required — must be a valid URL)*

A link to the work's GitHub repository, project page, or wherever it lives online.

```yaml
github_link: https://github.com/nickm/taroko-gorge
```

---

## A Complete Example

```yaml
---
title: Taroko Gorge
chef: Nick Montfort
abstract: A generative poem producing endless descriptions of a Taiwanese gorge
  through looping, substitutable language structures.
description: |
  Taroko Gorge is a poetry generator written in JavaScript by Nick Montfort
  in 2009. It produces an endless stream of verse by recombining a small
  vocabulary of words and syntactic templates drawn from the landscape of
  Taroko Gorge National Park in Taiwan. The work runs in any web browser
  and requires no interaction — it simply generates, continuously.

  The piece has inspired numerous remixes and translations, making it one of
  the most generative (in both senses) works in the electronic literature canon.
genres:
  - Generative Poetry
difficulty_pans: 1
yields: |
  An endlessly running browser poem that produces new stanzas automatically,
  accessible to any reader with a web browser.
github_link: https://github.com/nickm/taroko-gorge
---

## Ingredients

- JavaScript (vanilla, no libraries)
- A small vocabulary of nouns, verbs, and prepositions
- A web browser

## Method

1. Open the page in a browser.
2. Read. Or don't — it will keep going either way.

## Notes

Remixing Taroko Gorge became a genre of its own. Consider exploring works like
*Tofu Gorge*, *Tokyo Garage*, and *Gorge* to see how others reworked the template.
```

---

## Troubleshooting

**My Pull Request failed validation.**
Read the error messages carefully — each one names the field and what's wrong
(word count too high, unrecognised genre, missing field, etc.). Fix the issue in
your file, commit the change, and the check will re-run automatically.

**My genre isn't on the official list.**
Add it to `custom_genres` instead. You can use both `genres` and `custom_genres`
at the same time.

**I'm not sure how to use GitHub.**
GitHub's own guide is a good starting point:
[docs.github.com/get-started](https://docs.github.com/en/get-started)

---

Questions? Open an issue on the repository or get in touch directly.

We look forward to reading your recipe.
