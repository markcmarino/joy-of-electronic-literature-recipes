---
title: How to Bake a Citation Cake
chef: Stephanie Strickland and Ian Hatcher
abstract: Create randomly recombinant text from curated citations using HTML and JavaScript to explore information quality.
description: >
  Put 250 words or less here.
genres:
  - Generative Poetry
difficulty_pans: 1
yields: >
  Write 50 words or less for recipe yield
github_link: (https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/citation-cake.md)
---



# How to Bake a Citation Cake

**Stephanie Strickland**  
**Ian Hatcher**  
Instructor   
University of Colorado Boulder

**Class of E-lit:** Text Generator  
**Dish:** A rich confection, sample with caution  
**Required ingredients:** Computational device, citations, code editor  
**Preparation and cooking time:** Minutes to hours  
**Number of servings and serving size:** Can you eat a whole cake? Please share  
**Rating:** 🍳 One pan, depending on number of layers  
**From the chef:** *The success of your cake will depend on your skill in shopping online for ingredients.*

## **Background: Stocking the Kitchen**  
To what purpose might randomly recombinant text be put as our shelves groan beneath the weight of tasteless and mislabeled information? Creating a Citation Cake of course, one that will allow us to inquire into and taste-test its ingredients\! 

Citations are text quotes and/or images. They may be fresh or stale, perennially useful like baking powder, or even poisonous. Selection quality is paramount, because ingredients must not only intrigue separately but also blend properly. A math equation will not always work well with the last line of your favorite novel. However, there are many cooking traditions. 

Sourcing quality ingredients may involve going out of your way, to academia, to Wikipedia, to footnotes, or to your underappreciated local library of print sources. These days, many of us live in citational food deserts. Consider that fruitcakes last even longer when made with plastic fruits of the type used in photo shoots.

Citations should, as specified above, taste good on their own and play well with others. However, revealing their sources may change their flavor significantly. Did you raid a pantry of mouldering or preservative-soaked boxes? Did you seek out a local green market?

These are your cake making steps: 1\) gather one-line citations; 2\) separately note and save their source—best an individual author, but some group-produced citations, for instance a hurricane warning from 2023, prove reliable; 3\) combine them in a code-based mixer-oven. The JavaScript code below is both mixer and oven, a way to prepare and to test the ultimate deliciousness and reliability of your choice ingredients. 

It can be tricky to discover which sources or markets are better than others. Tradition and research both contribute. Some ingredients may be culturally suspect, but like MSG prove to be harmless upon investigation (Kean 2023). Your cake might include garish AI-generated layers, if it is intended to be more experimental than edible (Zalman 2017). Revealing your ingredient sources, after your layers have been assembled onscreen, could pique your appetite or cause you to lose it. You will want to discover which.

## **Sample Before You Cook:**

In our collaborative digital poems *House of Trust* (Strickland and Hatcher 2014), a new variation on the classic *House of Dust* as explained in the poem, and *Liberty Ring\!* (Strickland and Hatcher 2020), we gathered and sorted quotes and images that would complement or challenge one another. Refining the piece involved swapping out our choices to discover new and unforeseen recombinant possibilities.

# **Recipe: Citation Cake**

## **Directions: The File/s In Your Cake**

To start with, you’ll need a plain text html file. This file will contain your html, css, and JavaScript code all together. Name it something like cake.html.

[Or to download this code, see *Notes* at the end of the recipe.\]


1. Enter your html headers and css:
```html
<\!DOCTYPE html\>  
<html lang="en"\>  
<head\>  
  <meta charset="UTF-8"\>  
  <title\>Citation Cake\</title\>

  <style type="text/css"\>  
    textarea { width: 90%; height: 120px; }  
    textarea, p, hr { margin: 10px 0 25px; }  
    .hide-attrib .attrib { display: none; }  
  </style\>  
</head\>
```

2. Enter your body elements and ingredients. You’ll want to gather and label your own ingredients, but to get you started and show you how to format them, this recipe includes some examples, in brown below. Note that each citation here takes the form of one or more lines of text, with the last line being its attribution, and different citations are separated by a blank line.

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

3. Now start adding your JavaScript. We’ll need three utility functions to make our code work, and these come first. Note that comments, formatted here in green, are intended to clarify what does what, but you can leave them out if you like.

```javascript
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

4. We’ll finish off our code with the JavaScript to process and bake our cake:

```javascript
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

## **Notes**

The code for this recipe can be found at:  
[digitalobjects.net/resources/citation-cake/](https://digitalobjects.net/resources/citation-cake/)

## **Variations**

The two ‘bowls’ of ingredients in this recipe are labeled “better” and “worse” in the code above. As your layers will be sourced equally from both bowls, these labels are present only to make you think about your ingredients as you assemble them. You might change the labels to something more vivid, such as “Certifiably Fresh 5 Star” and “Possibly Past Its Expiration Date.”

## **Works Cited**

Kean, Sam. “The Rotten Science Behind the MSG Scare.” *Distillations Magazine*, 2023, sciencehistory.org/stories/magazine/the-rotten-science-behind-the-msg-scare.

Zalman, Sandra. “Eat, Live, Work,” in *\*Walls Paper\* 1972 by Gordon Matta-Clark*, Tate Research Publication, 2017, tate.org.uk/research/in-focus/walls-paper/eat-live-work.

Strickland, Stephanie and Ian Hatcher. *House of Trust*, 2014\. house-of-trust.org.

Strickland, Stephanie and Ian Hatcher. *Liberty Ring\!*, 2020\. stephaniestrickland.com/projects/liberty-ring.  
