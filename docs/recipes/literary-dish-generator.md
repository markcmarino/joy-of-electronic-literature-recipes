---
title: Literary Dish Generator
chef: Margaret Rhee, Mark C. Marino
abstract: A beginner-friendly HTML generator that randomly combines word lists
  to produce literary dish names, teaching core mechanics of generative poetry.
description: >
  A starter recipe for text generation and generative poetry, tracing a lineage
  from Christopher Strachey's 1952 Love Letter Generator through Surrealism,
  Dada, and Oulipo to contemporary electronic literature.

  The Literary Dish Generator teaches the core mechanics of algorithmic poetry:
  building word arrays and combining them randomly to produce new textual
  combinations. Written in plain HTML and JavaScript, it runs in any web browser
  without installation or external libraries.

  The recipe uses "cyborg poetics" as its theoretical frame — the intersection
  of code and poetry explored by artists including Nick Montfort, Allison
  Parrish, and Stephanie Strickland. The generator produces literary dish names
  from three arrays (adjectives, literary forms, abstract nouns) and serves as
  a foundation for more complex generators, bots, and electronic poetry
  experiments. Extensions guide readers toward adding new grammatical elements,
  and related recipes point toward Mastodon bots and the Taroko Gorge poetry
  generator.
genres:
  - Generative Poetry
  - Word Manipulation
custom_genres:
  - Cyborg Poetics
  - Text Generator
  - Bot
difficulty_pans: 1
yields: >
  A working browser-based text generator that produces unique literary dish
  names each time it runs. Readers gain a reusable template for building their
  own generative poetry tools from customizable word arrays, with no framework
  or server required.
github_link: https://github.com/markcmarino/literary-dish-generator
---

## Background

Ever since Christopher Strachey served up his love letters generated from the
Manchester Mark 1 computer, programming poets have been using algorithms to
randomly produce content — from poetry to Tweets — using code. The recipes
adapt techniques passed down from previous cooking schools, such as the
Surrealists, the Dada movement, and the Ouvroir de Littérature Potentielle
(Oulipo): techniques that involve preparing poetry with algorithmic practices
and a healthy dash of chance or randomness.

An earlier practice of drawing lines of poetry out of a hat transformed into
drawing words and phrases from an array. And the practice has its popular
form: Mad Libs. As literary practices took new computational forms, artists
and scholars in electronic and experimental poetry have categorized the large
variety of poetic practices as cyborg poetics or e-poetry. The intersection
of machines and poetry includes "code poetry, hypertext poetry, poetry produced
via search engines and other digital poetry experiments. Poems using email or
tweets. Poems that envision collaboration between programmers and poets"
(Susan Vanderborg, 2012).

Artists and poets working within this genre include Nick Montfort, John Cayley,
Stephanie Strickland, Allison Parrish, and others.

In the case of generators, the poetry is often in the algorithm itself —
embodying the concept you might find in conceptual poetry or the constraint-based
processes of the Oulipo. E-poetry authors will at times publish the code as the
poem, like a treasured recipe written in a grandmother's own hand.

As programmer poet and scholar Neil Aitken cites, a spell or poem "is not a poem
itself but like a recipe or a set of instructions to transform the intangible
into the materially real." Code works similarly: the code itself is words, and
when compiled, the execution produces a result. The code must run.

## Sample Before You Cook

- [Christopher Strachey's Love Letter Generator](https://www.gingerbeardman.com/loveletter/)
- [Stephanie Strickland & Nick Montfort — Duels and Duets](http://duels-duets.newbinarypress.com/)
- See also the recipes for *Taroko Gorge* and *The Limerick Diet* in this collection.

## Ingredients

- Computer or phone
- Creativity
- Code editor (a plain text editor will do in a pinch)
- Paper or spreadsheet (for planning your word lists)
- A web browser

**Preparation and cooking time:** 15 minutes
**Servings:** 1 generator

## From the Chefs

This particular recipe, like so many, was created out of constraint and
necessity. Around 2015, we fell in love with Twitterbots of the kind found in
abundance in the Electronic Literature Collection, Volume 3 — before the
election of 2016, when Twitterbots would become weapons of election disruption.
These were Twitterbots of the most aesthetic kind, like the magical realism bot
with its infinite array of Borgesian tweets.

We wanted to share that form here and had originally offered a Twitterbot recipe.
But since that platform has gotten X-ed out, we decided instead to start with a
recipe not dependent on any platform but the current web. If you're new to bots,
this Literary Dish Generator can serve as a starter for text generation — using
the basic elements found in all sorts of e-lit forms, from bots to poetry and
story generators. Treat it like a basic butter cookie or a starter crust to
learn the fundamentals.

## Method

**1.** On a sheet of paper or spreadsheet, make a table with five columns:

| adjective | literary form | of | abstract noun |
|-----------|--------------|-----|----------------|
| Spicy     | Haiku        | of  | Time           |
| Sweet     | Sonnet       | of  | Memory         |
| ...       | ...          | of  | ...            |

Dream up a list of any length of **adjectives**, **literary forms**, and
**abstract nouns**. (You can leave "of" alone.) Adjectives can come from words
that describe food. Literary forms can be as varied as you'd like. Abstract nouns
add depth, resonance, gravitas.

**2.** Copy or retype the starter code below into your code editor.

**3.** Save the file as a `.html` file and open it in a browser to see what it
does. Reload to see variations. Use a lowercase filename without spaces.

**4.** Replace the words in the program's arrays with your words from the columns:
adjective, literary form, and abstract noun.

> Keep the quotation marks, backticks, and commas exactly as they are. Each word
> is surrounded by double quote marks and separated by a comma. Smart quotes
> (the curly kind) will break the code — use straight quotes only.

**5. (Optional)** If you're feeling adventurous, change the grammar. Make new
arrays and add new variable names into this line:

```javascript
const dish = `${adjective} ${literaryform} of ${abstract}`;
```

This line constructs the dish name — it provides the grammar of the generator,
the pattern of words the generator will follow. When you add a new array, put
its variable name where it belongs in the template, with a `$` at the front
inside curly braces. You'll also need to add a line that picks randomly from
your new array:

```javascript
const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
```

**6.** Save and open in your browser.

## Starter Code: Literary Dish Generator

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Literary Dish Generator</title>
</head>
<body>
  <h1>Literary Dish Generator</h1>
  <button onclick="generateDish()">Generate Dish</button>
  <h2 id="dishDisplay"></h2>

  <script>
    // Arrays of words to use in dish names — replace these with your own
    const adjectives = ["Spicy", "Sweet", "Forbidden", "Tangy", "Diabolical", "Fancy", "Flaming"];
    const literaryforms = ["Haiku", "Sonnet", "Villanelle", "Novella", "Opera", "Novel", "Quarto"];
    const abstracts = ["Time", "Secrets", "Memory", "Loss", "Woe", "Ecstasy", "Regret"];

    function generateDish() {
      // Randomly pick words from the arrays
      const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
      const literaryform = literaryforms[Math.floor(Math.random() * literaryforms.length)];
      const abstract = abstracts[Math.floor(Math.random() * abstracts.length)];

      // Combine the words to create a dish
      // Note: the ` symbol is a backtick, to the left of 1 on your keyboard
      const dish = `${adjective} ${literaryform} of ${abstract}`;

      // Display the dish on the webpage
      document.getElementById('dishDisplay').innerText = dish;
    }
  </script>
</body>
</html>
```

## Notes

This recipe relies on two core elements:

**Randomness** — drawing randomly from arrays. This is the heart of text
generation, though you can always substitute a different selection system,
such as cycling through items in sequence.

**The Document Object Model (DOM)** — replacing elements on the page. This
deals with manipulating content in the browser, swapping new text in for old.

## Variations

Notice how this piece creates one line — the "dish" — from words across three
lists. To go further:

**Add a tagline.** First, add a new display element to the HTML:

```html
<h2 id="taglineDisplay"></h2>
```

Then construct your new phrase in the script:

```javascript
const tagline = `${literaryform} made ${adjective}`;
```

Finally, send it to the page:

```javascript
document.getElementById('taglineDisplay').innerText = tagline;
```

The `id` tells the HTML where to place the new text. Use a different `id` for
each display element.

Using this model, you can create your own grammars, build longer lists, and
generate freely.

## Related Recipes

**A Mastodon Bot** — Build a bot to post regularly on Mastodon using the Tracery
system at [Cheap Bots, Toot Sweet](https://cheapbotstootsweet.com/).

**Taroko Gorge** — Make a poetry generator with your own take on Nick Montfort's
popular work of infinite verse.

## Further Reading

- Ville Lampi (2017). "Looking behind the text-to-be-seen: Analysing Twitterbots as electronic literature."
- Matthew Kirschenbaum. "Machine Visions."
- Susan Vanderborg (2012). On cyborg poetics and e-poetry.
