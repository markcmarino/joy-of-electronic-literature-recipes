# Author Review Instructions

Thank you for contributing to the *Joy of Electronic Literature Recipes*! We're preparing your recipe for publication and need your help reviewing the content.

## What Needs Review

Your recipe has two parts:

1. **YAML Metadata** (at the top of your file) - This will appear in the published book
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
   - These are in the `description` and 'yields' fields in the YAML
   - Summarize your recipe, what it teaches, and what it yields
   - If you are editing in Github, preserve any line breaks and don't add blank lines in this section as it affects how the yaml is rendered

2. **Review all YAML fields** for accuracy
   - Check your name spelling
   - Verify the project link works
   - Confirm genres are correct
   - Ensure abstract and yields are accurate

3. **Review the full recipe content** (optional but encouraged)
   - Check for typos or formatting issues
   - Ensure all steps are clear
   - Verify code examples work as intended

4. **review images** 
   - Upload images to `docs/images/your-recipe-slug/` folder
   - Reference them in your recipe with relative paths
   - See the "Adding Images" section below for instructions
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
1. Go to this Google Doc: https://docs.google.com/document/d/1SklmInCp-2j4YPgmRHsCtLDceiuClT2ZWR64z53leFg/edit?usp=sharing
2. Find your recipe tab
3. Add a comment for your Descriptions/Yield and leave a comment on any text or other content that needs correcting.

**Step 2: Add Your Changes**

Add comments or suggested edits directly in the Google Doc for:

- **Your 250-word description** (write it in full)
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

## Adding Images to Your Recipe

If your recipe originally included images (screenshots, diagrams, photos), you can add them back:

### Via GitHub (Easiest for Non-Technical Authors)

1. **Navigate to the images folder:**
   - Go to: https://github.com/markcmarino/joy-of-electronic-literature-recipes/tree/master/docs/images
   - Click "Add file" → "Create new file"
   - In the name field, type: `your-recipe-slug/placeholder.md` (this creates the folder)
   - Click "Commit new file"

2. **Upload your images:**
   - Navigate to your newly created folder: `docs/images/your-recipe-slug/`
   - Click "Add file" → "Upload files"
   - Drag and drop your images
   - Commit with message: "Add images for [Your Recipe Name]"

3. **Update your recipe markdown:**
   - Edit your recipe file in `docs/recipes/your-recipe-slug.md`
   - Add image references where they should appear:
   ```markdown
   ![Description of image](../images/your-recipe-slug/image-filename.png)

   *Caption: Brief description of the image*
   ```

### Via Google Doc (Even Easier)

If you're using the Google Doc for edits:
1. Insert your images in the Google Doc where they should appear
2. Add a note indicating the image filename and alt text
3. We'll handle uploading them to GitHub and adding the proper references

### Image Guidelines

- **Alt text:** Always describe what's in the image (the text in square brackets)
- **File names:** Use descriptive names: `screenshot-interface.png` not `image1.png`
- **File size:** Keep images under 2MB when possible
- **Formats:** PNG for screenshots/diagrams, JPG for photos

**Example in your recipe:**

```markdown
## Background

Here's what the interface looks like:

![Screenshot showing the main text manipulation interface](../images/my-recipe/interface-screenshot.png)

*Figure 1: The main interface with text controls on the left*

As you can see in Figure 1, the interface provides...
```

For complete image guidelines, see: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/images/README.md

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
