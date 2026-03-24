# Recipe Images

This directory contains images for the Joy of Electronic Literature Recipes.

## Directory Structure

Organize images by recipe, using the same slug as the recipe filename:

```
docs/images/
├── distant-feelings/
│   ├── screenshot-session-2020-04-17.png
│   └── diagram.jpg
├── mashed-soup/
│   ├── figure-1-rules-order.png
│   └── figure-2-mashing-actions.png
├── literary-dish-generator/
│   └── interface-screenshot.png
└── ...
```

**Naming convention:**
- Use lowercase with hyphens
- Be descriptive: `screenshot-gameplay.png` not `img1.png`
- Include context if helpful: `figure-1-rules-order.png`

## How to Add Images to Your Recipe

### Step 1: Create Your Recipe's Image Folder

If your recipe is `docs/recipes/my-recipe.md`, create:
```
docs/images/my-recipe/
```

### Step 2: Add Your Images

Place your images in that folder:
```
docs/images/my-recipe/screenshot.png
docs/images/my-recipe/diagram.jpg
```

### Step 3: Reference Images in Your Recipe

In your recipe markdown file (`docs/recipes/my-recipe.md`), use relative paths:

```markdown
![Screenshot of the interface](../images/my-recipe/screenshot.png)

*Caption: Brief description of what the image shows*
```

**Important:** The path is `../images/` (up one level from `recipes/` to `docs/`, then into `images/`)

### Full Example

**File:** `docs/recipes/distant-feelings.md`

```markdown
## Samples before you cook

Here's a screenshot from a Distant Feelings session:

![Screenshot from Distant Feelings confinement #4 session](../images/distant-feelings/screenshot-session-2020-04-17.png)

*Screencapture: Distant Feelings confinement #4 session, April 17, 2020*
```

## Image Guidelines

### File Formats
- **Screenshots:** PNG (best for UI/text) or JPG (smaller file size)
- **Photos:** JPG
- **Diagrams:** PNG or SVG (SVG preferred for scalability)
- **Code snippets:** PNG

### File Sizes
- Keep images under 2MB when possible
- Resize large screenshots to reasonable dimensions (1200-1600px wide max)
- Optimize images before adding (use tools like TinyPNG, ImageOptim, or similar)

### Accessibility
Always include descriptive alt text in square brackets:

```markdown
![A participant's face during a Distant Feelings session showing closed eyes and peaceful expression](../images/distant-feelings/participant-closeup.png)
```

**Good alt text:**
- Describes what's in the image
- Conveys the information/emotion it represents
- Is concise but informative

**Bad alt text:**
- "Image 1"
- "Screenshot"
- Empty: `![](path/to/image.png)`

### Captions (Optional)

Add captions using italics after the image:

```markdown
![Screenshot description](../images/recipe-name/image.png)

*Figure 1: Caption text explaining the image in more detail*
```

## Adding Images via GitHub

### Option A: Web Interface (Easiest)

1. Navigate to: https://github.com/markcmarino/joy-of-electronic-literature-recipes/tree/master/docs/images
2. Click "Add file" → "Upload files"
3. Create your recipe folder if needed
4. Drag and drop images
5. Commit with message: "Add images for [Recipe Name]"

### Option B: Git Command Line

```bash
# Navigate to your local repository
cd joy-of-electronic-literature-recipes

# Create your recipe's image folder
mkdir -p docs/images/my-recipe

# Copy your images into that folder
cp ~/Desktop/screenshot.png docs/images/my-recipe/

# Add and commit
git add docs/images/my-recipe/
git commit -m "Add images for My Recipe"
git push origin master
```

### Option C: Pull Request (If Contributing)

1. Fork the repository
2. Clone your fork
3. Create a branch: `git checkout -b add-images-my-recipe`
4. Add images to `docs/images/my-recipe/`
5. Commit and push to your fork
6. Create a pull request

## Removing Old Image Placeholders

Some recipes may have old image placeholders like:

```markdown
![][image1]
![][image2]
```

Replace these with proper image markdown:

```markdown
![Description of first image](../images/recipe-name/image1.png)
![Description of second image](../images/recipe-name/image2.png)
```

## Questions?

If you're unsure about image formatting or have questions about adding images to your recipe, contact Mark or check the [Recipe Template](../RECIPE_TEMPLATE.md) for examples.
