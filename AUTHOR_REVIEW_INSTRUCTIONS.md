# Author Review Instructions

Thank you for contributing to the *Joy of Electronic Literature Recipes*! We're preparing your recipe for publication and need your help reviewing the content.

## What Needs Review

Your recipe has two parts:

1. **YAML Metadata** (at the top of your file) - This will appear in the printed book
2. **Recipe Content** (the main body) - The full recipe instructions and background

**Recipe Template Reference:** For a complete guide to recipe structure and sections, see [docs/RECIPE_TEMPLATE.md](docs/RECIPE_TEMPLATE.md) in the repository.

### YAML Fields That Will Appear in the Book

These fields are at the top of your recipe file between `---` markers:

- **title** - Your recipe title (max 10 words)
- **chef** - Your name(s) only, no titles (max 5 words)
- **abstract** - One sentence summary (max 25 words)
- **description** - A 250-word (max) summary of your recipe (see below)
- **genres** - Categories for your recipe
- **custom_genres** - Any additional genre tags
- **difficulty_pans** - Difficulty rating (1-4 pans)
- **yields** - What the reader experiences or the "output" (max 50 words)
- **github_link** - Link to your project/demo

### What You Need to Do

1. **Write a 250-word description and 50-word yields** of your recipe if you haven't already
   - These are in the `description` and `yields` fields in the YAML
   - For description: summarize your recipe, what it teaches
   - for yields: describe the output or what the cook will have once they complete the recipe
   - If you are editing in Github, preserve any line breaks and don't add blank lines in this section as it affects how the yaml is rendered

2. **Review all YAML fields** for accuracy
   - Check your name spelling
   - Verify the project link works
   - Confirm genres are correct
   - Ensure abstract and yields are accurate

3. **Review the full recipe content** (optional but encouraged)
   - Check that your recipe fits the format [docs/RECIPE_TEMPLATE.md](docs/RECIPE_TEMPLATE.md)
   - Review for typos or formatting issues
   - Ensure all steps are clear
   - Verify code examples work as intended

4. **Review images**
   - Images have already been migrated to GitHub
   - Check that they appear correctly in your recipe
   - Let us know if any are missing, incorrectly placed, or need captions updated
   - See your recipe on GitHub to view the images
---

## How to Submit Changes

Choose the method that works best for you:

### Option A: Google Doc Comments & Suggestions (Recommended)

**Step 1: Find Your Recipe**
1. Go to this Google Doc: https://docs.google.com/document/d/1SklmInCp-2j4YPgmRHsCtLDceiuClT2ZWR64z53leFg/edit?usp=sharing
2. Find your recipe tab
3. **Note:** You have "comment" access only - this allows us to track all changes and ensure nothing gets accidentally edited

**Step 2: Make Corrections by making Comments in the Google Doc**

For text changes (description, corrections, etc.):

**Step 3: Also, use Comments for Notes**

For questions or notes about images:

- **Highlight text** → Click "Add comment" (or Ctrl+Alt+M)
- Use comments to:
  - Ask questions about your recipe
  - Note where images should be moved or if any are missing
   - Request caption updates for images
  - Flag sections that need attention

**Example comment for image issues:**
> "This image should appear earlier, before the 'Background' section"
> "Missing screenshot of the final output"
> "Update caption to: Figure 1: The PoemChef interface with theme selector"

**Step 4: Done!**
We'll review your suggestions and comments, then transfer approved changes to GitHub.

---

### Option B: GitHub Pull Request (If You're Comfortable with Git)

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

## Reviewing Images

**Good news:** All images have already been migrated to GitHub for you!

### What to Check:

1. **View your recipe on GitHub** to see the images in context:
   - Go to: https://github.com/markcmarino/joy-of-electronic-literature-recipes/tree/master/docs/recipes
   - Find your recipe file and click to view it

2. **Check that images:**
   - Appear in the correct locations
   - Have appropriate captions
   - Are the right size/quality
   - Are not missing any from your original recipe

3. **If you notice issues**, add a comment in the Google Doc:
   ```
   IMAGE ISSUE:
   - Missing: screenshot of the final output
   - Wrong location: Figure 2 should appear before the "Directions" section
   - Caption update: Should read "Figure 1: The interface with controls"
   ```

We'll make any necessary adjustments to the images based on your feedback.

---

## Recipe Structure Reference

For detailed guidance on recipe structure, sections, and formatting, see the comprehensive **[Recipe Template](docs/RECIPE_TEMPLATE.md)**.

The template includes:
- All recommended sections (From the Chef, Background, Samples, Recipe, Ingredients, Directions, etc.)
- YAML field constraints and examples
- Code formatting guidelines
- Writing tips and best practices
- Examples of how to structure variations, related recipes, and citations

You don't need to follow the template exactly—it's a reference to help you understand the common structure and what sections are available to you.

---

## Questions?

If you have questions about the process of editing, contact Mark.
If you have questions about your revision, contact your editor.
For recipe structure guidance, see [docs/RECIPE_TEMPLATE.md](docs/RECIPE_TEMPLATE.md).

Thank you for your contribution to this cookbook!
