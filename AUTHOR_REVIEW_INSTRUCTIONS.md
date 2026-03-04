# Author Review Instructions

Thank you for contributing to the *Joy of Electronic Literature Recipes*! We're preparing your recipe for publication and need your help reviewing the content.

## What Needs Review

Your recipe has two parts:

1. **YAML Metadata** (at the top of your file) - This will appear in the published book
2. **Recipe Content** (the main body) - The full recipe instructions and background

### YAML Fields That Will Appear in the Book

These fields are at the top of your recipe file between `---` markers:

- **title** - Your recipe title (max 10 words)
- **chef** - Your name(s) only, no titles (max 5 words)
- **abstract** - One sentence summary (max 25 words)
- **description** - A 250-word summary of your recipe (see below)
- **genres** - Categories for your recipe
- **custom_genres** - Any additional genre tags
- **difficulty_pans** - Difficulty rating (1-4 pans)
- **yields** - What the reader experiences (max 50 words)
- **github_link** - Link to your project/demo

### What You Need to Do

1. **Write a 250-word description** of your recipe if you haven't already
   - This is the `description` field in the YAML
   - Summarize what your recipe teaches and its context
   - See your current description in your recipe file for reference

2. **Review all YAML fields** for accuracy
   - Check your name spelling
   - Verify the project link works
   - Confirm genres are correct
   - Ensure abstract and yields are accurate

3. **Review the full recipe content** (optional but encouraged)
   - Check for typos or formatting issues
   - Ensure all steps are clear
   - Verify code examples work as intended

---

## How to Submit Changes

Choose the method that works best for you:

### Option A: GitHub Pull Request (If You're Comfortable with GitHub)

**Step 1: Fork and Clone**
1. Go to: https://github.com/markcmarino/joy-of-electronic-literature-recipes
2. Click the "Fork" button (top right)
3. Clone your fork to your computer:
   ```bash
   git clone https://github.com/YOUR-USERNAME/joy-of-electronic-literature-recipes.git
   cd joy-of-electronic-literature-recipes
   ```

**Step 2: Find and Edit Your Recipe**
1. Your recipe is in: `docs/recipes/your-recipe-name.md`
2. Open it in any text editor
3. Edit the YAML fields at the top (between the `---` markers)
4. Make any changes to the recipe content below

**Step 3: Submit Changes**
1. Commit your changes:
   ```bash
   git add docs/recipes/your-recipe-name.md
   git commit -m "Update [Your Recipe Name]: review YAML and description"
   git push origin master
   ```

2. Create a Pull Request:
   - Go to your fork on GitHub
   - Click "Pull requests" → "New pull request"
   - Click "Create pull request"
   - Add title: "Author review: [Your Recipe Name]"
   - Add description of what you changed
   - Click "Create pull request"

**Step 4: Done!**
We'll review your changes and merge them into the book.

---

### Option B: Google Doc Notes (If GitHub Seems Complicated)

**Step 1: Find Your Recipe**
1. Go to this Google Doc: [LINK TO BE PROVIDED]
2. Find your recipe section (organized alphabetically by last name)

**Step 2: Add Your Changes**

Add comments or suggested edits directly in the Google Doc for:

- **Your 250-word description** (write it in full if not already there)
- **Corrections to any YAML fields** (title, chef name, abstract, yields, genres, link)
- **Any content corrections** (typos, missing steps, broken code examples)

Use Google Docs comment feature:
- Highlight text → Click "Add comment" → Type your suggested change

**Step 3: Done!**
We'll transfer your changes to GitHub and update your recipe.

---

## Tips for Writing Your 250-Word Description

Your description should cover:

1. **What your recipe is** (the creative work or technique)
2. **What it teaches** (skills, concepts, tools)
3. **Why it matters** (artistic/literary context)
4. **How it works** (brief overview of the approach)

**Example structure:**
> "[Recipe title]" is [what it is - 1 sentence]. The recipe teaches [key skills/concepts - 1-2 sentences]. [Context about why/how - 2-3 sentences]. The approach involves [brief method overview - 2-3 sentences]. [Optional: variations, outcomes, or next steps - 1-2 sentences].

**Keep it concise!** The full background and details go in the recipe body (below the YAML). The description is just a summary for readers browsing the book.

---

## Example YAML Block

Here's what the top of your file looks like:

```yaml
---
title: Your Recipe Title Here
chef: Your Name
abstract: One clear sentence about what this recipe does and teaches.
description: >
  A 250-word summary that explains what the recipe is, what it teaches,
  the context and background, and how the approach works. This will appear
  in the published book, so make it informative but concise. You can write
  multiple paragraphs by leaving blank lines between them.

  Like this second paragraph, which provides additional context or details.
genres:
  - Hypertext
  - Generative Poetry
custom_genres:
  - Experimental Forms
difficulty_pans: 2
yields: >
  A brief description of what the reader will experience or create when
  they follow this recipe.
github_link: https://your-project-url.com
---
```

Everything after the closing `---` is your full recipe content.

---

## Questions?

If you have questions about:
- **GitHub process**: [contact email/info]
- **Content questions**: [contact email/info]
- **YAML field meanings**: See the field descriptions at the top of this document

Thank you for your contribution to this cookbook!
