---
title: How to Bake a Citation Cake
chef: Stephanie Strickland and Ian Hatcher
abstract: Create randomly recombinant text from curated citations using HTML and JavaScript to explore information quality.
description: >
  In an age when shelves groan beneath the weight of tasteless and mislabeled information, what purpose might randomly recombinant text serve? Creating a Citation Cake, of course—one that allows inquiry into and taste-testing of its ingredients. This recipe teaches how to gather one-line citations (text quotes and/or images, fresh or stale, perennially useful or even poisonous) and combine them using a simple HTML/CSS/JavaScript mixer-oven. The key is curation: ingredients must intrigue separately and blend properly, though a math equation won't always work well with a favorite novel's last line. Citations should taste good on their own and play well with others, yet revealing their sources may change their flavor significantly. The JavaScript code functions as both mixer and oven, randomly shuffling citations from two bowls (labeled "better" and "worse" to prompt thinking about ingredient quality) and displaying a specified number of layers. Users can toggle attribution visibility to see how context affects perception. This approach, demonstrated in collaborative digital poems like "House of Trust" and "Liberty Ring!," treats citations as raw materials for play, transforming static text into dynamic performative events that question the nature and provenance of information itself.
genres:
  - Generative Poetry
difficulty_pans: 1
yields: >
  A rich confection of randomly combined citations that can be rebaked infinitely, revealing new juxtapositions with each iteration.
github_link: https://stephaniestrickland.com/projects/liberty-ring
---

## Ingredients

- Computational device (computer, tablet, or phone)
- Citations (text quotes and/or images)
- Code editor (Visual Studio Code recommended, or any text editor)
- Web browser
- Skill in shopping online for quality ingredients

## Method

### Stocking the Kitchen

**Understanding Citations as Ingredients:**

Citations are text quotes and/or images. They may be:
- Fresh or stale
- Perennially useful (like baking powder)
- Even poisonous

**Selection quality is paramount** because ingredients must:
1. Intrigue separately
2. Blend properly with others

**Sourcing Quality Ingredients:**

May involve going out of your way to:
- Academia
- Wikipedia
- Footnotes
- Your underappreciated local library of print sources

Consider: Many of us live in citational food deserts. Fruitcakes last even longer when made with plastic fruits used in photo shoots.

**Revealing Sources:**

Revealing citation sources may change their flavor significantly:
- Did you raid a pantry of moldering or preservative-soaked boxes?
- Did you seek out a local green market?

### Creating Your Citation Cake

**The File Structure:**

Create a plain text HTML file containing HTML, CSS, and JavaScript code together. Name it something like `cake.html`.

**Step 1: Enter HTML Headers and CSS**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Citation Cake</title>

  <style type="text/css">
    textarea { width: 90%; height: 120px; }
    textarea, p, hr { margin: 10px 0 25px; }
    .hide-attrib .attrib { display: none; }
  </style>
</head>
```

**Step 2: Enter Body Elements and Ingredients**

Gather and label your own ingredients. Each citation takes the form of one or more lines of text, with the last line being its attribution. Different citations are separated by blank lines.

```html
<body>
  <h1>Citation Cake</h1>
  <div>
    <label for="bowl-A">Better ingredients:</label><br>
    <textarea id="bowl-A">
A republic, if you can keep it.
Benjamin Franklin's response to Elizabeth Willing Powel's question: "Well, Doctor, what have we got, a republic or a monarchy?"

The beginning is always today.
Mary Wollstonecraft

"Where are you going, and what do you wish?" The old moon asked the three.
Eugene Field
    </textarea>
  </div>

  <div>
    <label for="bowl-B">Worse ingredients:</label><br>
    <textarea id="bowl-B">
Biological laws tell us that certain divergent people will not mix or blend.
Calvin Coolidge in <i>Good Housekeeping</i>

The word "blueberry" has the letter b three times. Once at the start ("B" in blueberry). Once in the middle ("b" in blue). Once before the -erry ending ("b" in berry). Total: 3
ChatGPT

And then I see the disinfectant where it knocks it out in a minute. One minute. And is there a way we can do something like that, by injection inside or almost a cleaning?
Donald Trump
    </textarea>
  </div>

  <p>
    <label for="layers">Number of layers:</label>
    <input type="number" id="layers" name="layers" min="1" value="3" />
    <br>
    <label for="attrib">Show attribution:</label>
    <input type="checkbox" id="attrib" name="attrib" checked />
  </p>

  <p><button id="bake">Bake</button></p>
  <hr/>
  <div id="cake"></div>
</body>
```

**Step 3: Add Utility Functions**

Three utility functions make the code work (comments in the code clarify what does what, but you can leave them out if you like):

```html
<script>

  // Split ingredients text into an array
  function splitIngredients(text) {
    return text.split(/(?:\r?\n){2,}/).map(chunk => chunk.trim()).filter(chunk => chunk);
  }

  // Format an ingredient (quote) and split off its attribution
  function formatIngredient(chunk) {
    const lines = chunk.split(/\r?\n/);
    if (lines.length < 2) return chunk;
    const lastLine = lines.pop();
    lines.push('<span class="attrib">- ' + lastLine + "<br><br></span>");
    return lines.join("<br>");
  }

  // Randomly reorder an array (with Fisher–Yates shuffle)
  function shuffle(a) {
    for (let i = a.length - 1; i > 0; i --) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }
```

**Step 4: Process and Bake**

Finish off the code with JavaScript to process and bake:

```html
  const bowlA = document.getElementById('bowl-A');
  const bowlB = document.getElementById('bowl-B');
  const bake  = document.getElementById('bake');
  const cake  = document.getElementById('cake');

  // Show or hide attribution when you click the checkbox
  document.getElementById('attrib').addEventListener('click', () => {
    cake.classList.toggle("hide-attrib");
  });

  // Run this code when you click "bake"
  bake.addEventListener('click', () => {

    // Get number of layers for the cake
    const layers = document.querySelector('#layers').value;

    // Get and process ingredients
    const a = splitIngredients(bowlA.value);
    const b = splitIngredients(bowlB.value);
    const ing = a.concat(b);

    // Make sure there are enough ingredients for a cake
    if (ing.length < layers) return cake.innerHTML = 'Too few ingredients!';

    // Mix the ingredients in random order
    shuffle(ing);

    // Assemble and display the cake
    const selected = ing.slice(0, layers);
    const formatted = selected.map(formatIngredient);
    cake.innerHTML = formatted.join("");
  });

</script>
</html>
```

### Using Your Citation Cake

1. Open the HTML file in a web browser
2. Enter your citations in the two text areas (better and worse ingredients)
3. Set the number of layers you want
4. Click "Bake" to generate a random combination
5. Toggle the "Show attribution" checkbox to reveal or hide sources
6. Click "Bake" again for a new random combination

## Notes

### Download the Code

The complete code for this recipe can be found at:
https://digitalobjects.net/resources/citation-cake/

### Variations

**Bowl Labels:**

The two bowls are labeled "better" and "worse" in the code to make you think about your ingredients as you assemble them. Since layers are sourced equally from both bowls, these labels are present only for reflection.

You might change the labels to something more vivid, such as:
- "Certifiably Fresh 5 Star"
- "Possibly Past Its Expiration Date"

### Cultural Context

**Some ingredients may be culturally suspect**, but like MSG prove harmless upon investigation (Kean 2023).

**Your cake might include garish AI-generated layers** if intended to be more experimental than edible (Zalman 2017).

**Revealing ingredient sources** after assembly could pique appetite or cause you to lose it. Discover which.

### Examples

**House of Trust** (Strickland and Hatcher, 2014)
https://house-of-trust.org

A new variation on the classic "House of Dust," gathering and sorting quotes and images that complement or challenge one another.

**Liberty Ring!** (Strickland and Hatcher, 2020)
https://stephaniestrickland.com/projects/liberty-ring

Demonstrates refined recombinant possibilities through carefully chosen citations.

### Works Cited

- Kean, Sam. "The Rotten Science Behind the MSG Scare." *Distillations Magazine*, 2023. sciencehistory.org/stories/magazine/the-rotten-science-behind-the-msg-scare
- Zalman, Sandra. "Eat, Live, Work," in *Walls Paper* 1972 by Gordon Matta-Clark, Tate Research Publication, 2017. tate.org.uk/research/in-focus/walls-paper/eat-live-work
- Strickland, Stephanie and Ian Hatcher. *House of Trust*, 2014. house-of-trust.org
- Strickland, Stephanie and Ian Hatcher. *Liberty Ring!*, 2020. stephaniestrickland.com/projects/liberty-ring

### Success Factor

"The success of your cake will depend on your skill in shopping online for ingredients."

Can you eat a whole cake? Please share.
