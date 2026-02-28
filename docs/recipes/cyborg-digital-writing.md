---
title: A Cyborg Digital Writing Primer
chef: Leonardo Flores
abstract: Learn to create digital writing by hacking existing works or using AI to generate frameworks.
description: >
  Cyborg digital writing describes how human authors and their writing have become enmeshed with digital technologies, from spell checkers to generative AI. This primer offers two accessible approaches to producing digital literary works using HTML, CSS, and JavaScript. The first method involves hacking existing standalone digital works by downloading their source code, opening it in a text editor, and modifying the datasets and styling to create something new. The second method harnesses AI systems like ChatGPT or Claude to generate code frameworks based on natural language prompts, which can then be customized with your own content. Both approaches lower the barrier to creating generative, interactive, kinetic digital writing that goes beyond the limitations of the page. The primer emphasizes understanding the code you're working with, debugging techniques, proper attribution, and iterative development. Whether repurposing Nick Montfort's "Taroko Gorge" or prompting an AI to create a word-clicking interface, these methods invite writers to explore digital media's potential without requiring extensive programming expertise.
genres:
  - Generative Poetry
difficulty_pans: 1
yields: >
  HTML-based digital writing works that can be interactive, generative, or kinetic, ranging from simple word sequences to complex textual systems.
github_link: https://iloveepoetry.org/creative/sequence.html
---

## Ingredients

- Web browser with internet connection
- Text editor (Visual Studio Code recommended: https://code.visualstudio.com/)
- For hacking: an existing HTML-based digital work
- For AI generation: access to ChatGPT, Claude, or Gemini
- Basic familiarity with HTML, CSS, and JavaScript (helpful but not required)

## Method

### Approach 1: How to Hack a Digital Work

**Step 1: Select a Work**

Choose any standalone work using HTML (not using external libraries). Recommended works:
- Leonardo Flores' Generative Template: http://iloveepoetry.org/creative/floresgenerativetemplate.html
- Nick Montfort's "Taroko Gorge": https://nickm.com/taroko_gorge/original.html
- Nick Montfort's "The Two": https://nickm.com/2/the_two.html
- Alison Knowles & James Tenney's "A House of Dust" (reimplemented by Nick Montfort): https://nickm.com/memslam/a_house_of_dust.html
- Any works from Taper: https://taper.badquar.to/

**Step 2: Save the File**

Open the work in your browser and save it as an HTML file on your computer (smartphones and tablets not recommended).

**Step 3: Open in Editor**

Open the saved file with a code or text editor like Visual Studio Code.

**Step 4: Set Up Live Preview**

Open the same saved file in a browser. Whenever you make changes in the editor, save the file and reload the browser to see the changes.

**Step 5: Modify the Code**

Modify the code carefully, avoiding breaking it by missing commas, quotation marks, or semicolons. Take small steps in changing datasets.

**Step 6: Finalize**

When satisfied:
- Give your work a title
- Modify aspects displaying your title and name
- Adjust the stylesheet
- Rename the file
- Write an artist's statement in the source code documentation crediting the original work and any AI assistance

**Debugging Options:**
- Check if the code editor identifies problems with red line numbers
- Open developer tools in your browser to see error messages with line numbers
- Copy-paste code into an AI system and ask it to fix it
- Use undo (Control/Command + Z) to revert to a working version

### Approach 2: How to Use AI to Create a Digital Work

**Preparation**

Before prompting, conceptualize your framework. Example concept:
"A word appears centered on screen. When the user touches it, it changes to a different word, allowing you to write a sequence that completes a sentence, tells a story, or delivers a poem."

**Process**

1. Create a new document in your code editor with a simple lowercase name ending in `.html` (e.g., `sequence.html`)

2. Open ChatGPT (https://chat.openai.com/), Claude (https://claude.ai), or Gemini (https://gemini.google.com)

3. Prompt the AI to generate HTML code with a simple yet descriptive prompt

4. Copy-paste the generated code into your document

5. Save the document and open (or reload) in your browser to see results

6. If you want modifications, repeat steps 3-5

7. Once happy with the "engine," modify the code directly in your editor to say what you want

**Example Prompt:**
"Generate HTML code to produce a page in which there's a word centered on the screen. When the user clicks or touches the word, it changes to the next word in a sequence of 10 words. Use lorem ipsum text for the words."

**Customizing the Generated Code**

After AI generates the framework, find the dataset (often in a line like `const words = [...]`) and replace with your own words or phrases.

**Final Touches:**
- Change the title in `<title>Your Title</title>`
- Add documentation with copyright notice and credits
- Consider using the MIT license for open sharing

**Debugging Options:**
Same as Approach 1, plus:
- If code becomes too long for AI, focus on specific sections (script, CSS, header, etc.)
- Copy-paste only the sections you wish to modify

## Notes

### Understanding Cyborg Writing Terms

- **Cyborg writing**: Writing shaped by digital technologies (spell checkers, predictive keyboards, generative AI, text generation engines)
- **Digital writing**: Writing that embraces digital media's potential (generative, interactive, multimodal, kinetic, hypertextual works)
- **Electronic literature**: Literary digital writing, including practices beyond written text (sound poetry, video poetry)

### Development Tips

**Add features one at a time** and work iteratively until each functions as desired before adding another.

**Possible enhancements for the word sequence example:**
- Randomize the sequence of words
- Change font size with each click
- Alter word color or background color
- Make words appear in random locations
- Enable dragging words
- Make words move in random directions or bounce off edges
- Accumulate words so the whole phrase appears on screen
- Make words grow, shrink, or fade over time

### Attribution and Ethics

Always credit:
- The original work you're hacking (with URL)
- AI systems used for code generation or debugging
- Any code libraries or frameworks employed

### Further Reading

Example work created with this method: https://iloveepoetry.org/creative/sequence.html

For AI-generated code, document the process in HTML comments within your source code, including:
- Date of creation
- AI system used (e.g., "ChatGPT 4o")
- Your role as author/curator
- Copyright and licensing information
