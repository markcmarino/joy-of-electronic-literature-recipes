# Image Migration Guide

Quick reference for moving image-heavy recipes from Google Docs to GitHub.

---

## Method 1: Download as .docx + Manual Image Extract (No Tools Required)

### Step 1: Download from Google Docs
1. Open your recipe in Google Docs
2. File → Download → Microsoft Word (.docx)
3. Save to your Downloads folder

### Step 2: Extract Images from .docx
.docx files are actually ZIP archives containing your images:

1. **Navigate to your Downloads folder**
2. **Make a copy** of the .docx file (keep the original safe)
3. **Rename** the copy: `recipe-name.docx` → `recipe-name.zip`
4. **Extract/Unzip** the file (right-click → Extract All)
5. **Open the extracted folder** → find `word/media/` subfolder
6. **All your images are there!** (named like `image1.png`, `image2.jpg`, etc.)

### Step 3: Organize Images
1. **Create folder** in your local repo: `docs/images/recipe-slug/`
2. **Copy images** from `word/media/` to `docs/images/recipe-slug/`
3. **Rename images** to be descriptive:
   - `image1.png` → `screenshot-interface.png`
   - `image2.jpg` → `figure-1-workflow.jpg`

### Step 4: Download Text as Markdown
1. Go back to Google Docs
2. File → Download → Markdown (.md)
3. Save to Downloads

### Step 5: Fix Image References
1. **Open the .md file** in a text editor
2. **Find image references** like:
   ```markdown
   ![](images/image1.png)
   ```
3. **Replace with proper references:**
   ```markdown
   ![Screenshot of the interface](../images/recipe-slug/screenshot-interface.png)
   ```
   - Add descriptive alt text in `[]`
   - Fix path to `../images/recipe-slug/`
   - Use your renamed filename

### Step 6: Upload to GitHub
1. **Navigate to** your local repo: `C:\Users\mcmarino\joy-of-eliterature-recipes\`
2. **Copy the .md file** to `docs/recipes/recipe-slug.md`
3. **Add YAML frontmatter** at the top (copy from another recipe as template)
4. **Commit and push:**
   ```bash
   git add docs/recipes/recipe-slug.md docs/images/recipe-slug/
   git commit -m "Add [Recipe Name] with images"
   git push origin master
   ```

---

## Method 2: Using Pandoc (Faster - One-Time Setup)

### One-Time Setup:

**Install Pandoc:**
- Download from: https://pandoc.org/installing.html
- Or use Windows package manager: `winget install pandoc`

### For Each Recipe:

1. **Download as .docx** from Google Docs (File → Download → Microsoft Word)
2. **Open PowerShell** or Command Prompt
3. **Navigate to Downloads:**
   ```bash
   cd D:\Downloads
   ```
4. **Convert with image extraction:**
   ```bash
   pandoc recipe-name.docx -o recipe-name.md --extract-media=.
   ```
   This creates:
   - `recipe-name.md` (markdown file)
   - `media/` folder with all images

5. **Organize files:**
   ```bash
   # Move markdown to recipes
   copy recipe-name.md C:\Users\mcmarino\joy-of-eliterature-recipes\docs\recipes\recipe-slug.md

   # Move images
   mkdir C:\Users\mcmarino\joy-of-eliterature-recipes\docs\images\recipe-slug
   copy media\*.* C:\Users\mcmarino\joy-of-eliterature-recipes\docs\images\recipe-slug\
   ```

6. **Edit `recipe-slug.md`** to fix image paths:
   - Change: `![](media/image1.png)`
   - To: `![Description](../images/recipe-slug/image1.png)`

7. **Add YAML frontmatter** at the top

8. **Commit and push:**
   ```bash
   cd C:\Users\mcmarino\joy-of-eliterature-recipes
   git add docs/recipes/recipe-slug.md docs/images/recipe-slug/
   git commit -m "Add [Recipe Name] with images"
   git push origin master
   ```

---

## Method 3: Using GitHub Web Interface (No Local Git)

### Step 1: Extract Images (Same as Method 1, Steps 1-3)
1. Download .docx from Google Docs
2. Rename to .zip and extract
3. Get images from `word/media/`
4. Rename them descriptively

### Step 2: Upload Images via GitHub
1. **Go to:** https://github.com/markcmarino/joy-of-electronic-literature-recipes/tree/master/docs/images
2. **Click:** "Add file" → "Create new file"
3. **Type:** `recipe-slug/placeholder.md` (this creates the folder)
4. **Click:** "Commit new file"
5. **Navigate to:** the new `docs/images/recipe-slug/` folder
6. **Click:** "Add file" → "Upload files"
7. **Drag and drop** your renamed images
8. **Commit:** "Add images for [Recipe Name]"

### Step 3: Create Recipe File via GitHub
1. **Go to:** https://github.com/markcmarino/joy-of-electronic-literature-recipes/tree/master/docs/recipes
2. **Click:** "Add file" → "Create new file"
3. **Name it:** `recipe-slug.md`
4. **Copy/paste** content from your Google Doc markdown export
5. **Fix image references** to use `../images/recipe-slug/filename.png`
6. **Add YAML frontmatter** at the top
7. **Commit:** "Add [Recipe Name]"

---

## Quick Reference: Image Path Format

When in your recipe file (`docs/recipes/recipe-slug.md`), reference images like this:

```markdown
![Alt text describing the image](../images/recipe-slug/image-filename.png)

*Figure 1: Caption providing additional context*
```

**Path breakdown:**
- `..` = go up one level from `recipes/` to `docs/`
- `images/recipe-slug/` = navigate to your recipe's image folder
- `image-filename.png` = the actual image file

---

## Troubleshooting

### Images don't show up in GitHub preview:
- Check that path starts with `../images/` (not `images/`)
- Verify image filename matches exactly (case-sensitive)
- Ensure images are actually in `docs/images/recipe-slug/` folder

### Images look wrong when downloaded as .md:
- Google Docs markdown export sometimes mangles image references
- Safest to extract images from .docx manually (Method 1)

### Too many steps:
- After first recipe or two, the process becomes quick
- Pandoc (Method 2) is fastest after initial setup
- You can also just note which recipes need images and batch process later

---

## Recommended Workflow

**For 1-2 recipes:**
Use Method 1 (manual extract) - no tools needed, straightforward

**For 3+ recipes:**
Set up Pandoc (Method 2) - saves significant time

**If uncomfortable with command line:**
Use Method 3 (GitHub web interface) - all done in browser

---

## Tips

- **Rename images immediately** when you extract them (easier than remembering what image1.png was)
- **Keep original .docx** until you verify everything looks good on GitHub
- **Test with one recipe first** to get comfortable with the workflow
- **Alt text matters** - describe what's in each image for accessibility
- **File sizes** - if an image is over 2MB, resize it before uploading

---

## Still Stuck?

If you hit issues:
1. Check that file paths are correct (`../images/` not `images/`)
2. Verify filenames match exactly (including extensions)
3. Make sure images are committed to git (not just copied locally)
4. GitHub preview should show images if everything is correct
