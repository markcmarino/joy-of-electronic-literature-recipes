---
title: Full Words Ramble
chef: Daniel C. Howe, John Cayley
abstract: A browser text that continuously replaces its own words with rhymes and
  sound-alikes, rambling away from source prose before wandering back again.
description: Recipes for rambles (think of them like fruit crumbles, with an even greater range of fine-grained flavor palettes) usually have prose as their main ingredient and we’ve given you, here, a shortened version of the convoluted, rambling piece that we used to develop the recipe. It was Chef Howe who first started using functions from the RiTa library to find and replace words according to various criteria for similarity. Here, replacements can rhyme, ‘look-like’ (in terms of spelling) or ‘sound-like’ (in terms of phonemes). Replacements are chosen so as to occupy the same part of speech as the word being replaced. Rambles can be made to ramble forever, or else, at a certain point, to return. Returning rambles record a history of where they have been and then wander back in a shuffling order toward their textual starting point.
genres:
  - Word Manipulation
  - Generative Poetry
difficulty_pans: 2
yields: One or two paragraphs of fulsome, textured, browser-readable language; a ramble from word choice to word choice along all but numberless combinations of pathways.
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/full-words-ramble.md
---
# Full Words Ramble

Daniel C Howe
University of the Arts, London
daniel@rednoise.org

John Cayley
Brown University
[john\_cayley@brown.edu](mailto:john_cayley@brown.edu)

**Category:** Word-choice (paradigmatic) manipulator.  
**Class of E-lit:** Text modulator.  
**Required ingrdients:**

* one or two paragraphs of ambulatory prose

* selected functional ingredients from the contemporary web stack:

  * JavaScript

  * HTML5

  * CSS

  * a JavaScript Natural Language Processing (NPL) library; we recommend Chef Howe’s [RiTa](https://github.com/dhowe/ritajs) (https://github.com/dhowe/ritajs), which we use in this recipe.

**Preparation and cooking time:** from one hour-or-so to how-long-have-you-got.  
**Number of servings and serving size:** one or two paragraphs, with near infinite variations.  
**Rating:** two or three pans 🍳🍳(🍳) from moderate to go-to-town.

## **Background:**

Delicious with ambulatory prose.  
Recipes for rambles (think of them like fruit crumbles, with an even greater range of fine-grained flavor palettes) usually have prose as their main ingredient and we’ve given you, here, a shortened version of the convoluted, rambling piece that we used to develop the recipe. It was Chef Howe who first started using a number of functions built into the RiTa library to find and replace words according to various criteria for similarity. Here, replacements can rhyme, ‘look-like’ (in terms of spelling) or ‘sound-like’ (in terms of phonemes). Replacements are chosen so as to occupy the same part of speech as the word being replaced. Rambles can be made to ramble forever, or else, at a certain point, to return. Returning rambles record a history of where they have been and then wander back in a shuffling order toward their textual starting point.

## **Sample before you cook:**

Based on ‘[ramble](https://thelaob.com/a0/ramble/)’ (https://thelaob.com/a0/ramble/) by Daniel C. Howe & John Cayley, May 2021

**From the chefs:** Chef Cayley advises that preparation, cooking and even plating in an online, no-installation live-coding environment like [Observable](https://observablehq.com/) (https://observablehq.com) can be an elevating, shareable experience.

## **Directions:**

We provide you with some off-the-shelf starter code and CSS here, preprepared and ready for your culinary customization. As you get used to cooking up your own rambles you should experiment with some fundamental recombination and remixing of the starter code. The code here is mostly taken from an online live-coding notebook where you can see it actually working in real time: [https://observablehq.com/@shadoof/full-words-ramble](https://observablehq.com/@shadoof/full-words-ramble). You can also make changes to the notebook code in real time. The JavaScript in the notebook may need slight adaptation for use in other environments, such as node.js for example.

1. Start by replacing our prose with your own in supplyText.

2. We’re going to show the wandering, changing text on a web page, so we have to have an HTML div with id=display and class=container. It would should look like this:   
   \<div id="display" class="container"\>\</div\>.

3. Chef Howe’s RiTa Library gets folded into the mixture with (see below in the live-code notebook): RiTa \= require("rita@2") or use: import..

4. The supplyText has to be prepped:

   1. its words should be put into an array,

   2. their partsOfSpeech should be slotted into a corresponding array, and

   3. HTML spans (for the display div) are created for all possible words by the function spanify.

5. Now, copy or fork and have a look at the main word-choice updating code in the update function. This is where the word replacements are done. There are comments in the code and it is very tweakable to taste.

6. The function updateDOM (DOM \= HTML's Document Object Model) actually changes the display in the div we set up earlier.

7. In this starter code, so long as the variable updating is set to true, the text goes off on its ramble.

8. Everything else in – or referred to in – the starter code below is just cream, chiefly visualization cream. You can explore this cream in the [live-code notebook](https://observablehq.com/@shadoof/full-words-ramble) (https://observablehq.com/@shadoof/full-words-ramble), and you can see a fully-developed, haute-cuisine version of a ramble that our Chefs published as [*Preoccupations*](https://thenewriver.us/preoccupations/) (https://thenewriver.us/preoccupations/) in *The New River*.

## **Starter Code:**

const supplyText \= "by the time the light has faded, as the last of the reddish gold illumination comes to rest, then imperceptibly spreads out over the moss and floor of the woods, you or I will have set out on several of yet more circuits at every time and in all directions, before or after this or that circadian, usually diurnal, event on mildly rambling familiar walks, as if these exertions might be journeys of adventure whereas always our gestures, guided by paths, are also more like traces of universal daily ritual, merely passing through and by and over the moss, under the limbs of the evergreens, beside the lake, within the sound of its lapping waves, annihilated, gone, quite gone, now simply gone and, in being or walking in these ways, giving up all living light for settled, hearth held fire in its place, returned"

const words \= RiTa.tokenize(supplyText) // split into words  
const partsOfSpeech \= RiTa.pos(supplyText) // pos for each word  
const debugging \= false // optional, changes visualization

// assigns each word to its own span with unique id  
const spanify \= (data, selector) \=\> {  
  let tokens \= Array.isArray(data) ? data : RiTa.tokenize(data);  
  let reducer \= (acc, w, i) \=\> {  
    acc \+= \`\<span id='w${i}' class='text'\>${w}\`;  
    if (\!RiTa.isPunct(tokens\[i \+ 1\])) acc \+= ' ';  
    return (acc \+= \`\</span\>\`);  
  };  
  let spans \= tokens.reduce(reducer, '');  
  let ele \= selector;  
  if (typeof ele \=== 'string') {  
    ele \= document.querySelector(selector);  
  }  
  ele.innerHTML \= spans;  
}

// choose a random word to replace  
const update \= () \=\> {  
  if (\!updating) return;

  let next, pos, idx, word;

  // ramble on  
  if (state.outgoing) {  
    const r \= Math.floor(Math.random() \* words.length);

    // loop from a random spot  
    for (let i \= r; i \< words.length \+ r; i++) {  
      idx \= i % words.length;  
      word \= words\[idx\].toLowerCase();  
      pos \= partsOfSpeech\[idx\];

      if (word.length \< 4\) continue; // len \>= 4

      // preserve some grammatical words  
      if (stopWords.includes(word)) continue;

      // find related words  
      const rhymes \= RiTa.rhymes(word, { pos });  
      const sounds \= RiTa.soundsLike(word, { pos });  
      const spells \= RiTa.spellsLike(word, { pos });  
      const similars \= \[...rhymes, ...sounds, ...spells\];

      // only words with 2 or more similars  
      if (similars.length \< 2\) continue;

      // pick a random similar  
      next \= RiTa.random(similars);

      if (next.length \< 4\) {  
        continue; // skip if not \>= 4 letters long  
      }

      if (next.includes(word) || word.includes(next)) {  
        continue; // skip substrings  
      }

      if (ignores.includes(next)) continue; // skip ignored words

      if (/\[A-Z\]/.test(words\[idx\]\[0\])) {  
        next \= RiTa.capitalize(next); // keep capitals  
      }

      words\[idx\] \= next; // do replacement  
      state.history\[idx\].push(next); // add to history  
      break; // done  
    }  
  } else {  
    // ramble back  
    const data \= restore();  
    if (\!data) return;  
    \[next, idx, pos, word\] \= Object.values(data);  
  }

  updateDOM(next, idx);  
  const num \= updateState();  
  console.log(\`${num}) ${word} \-\> ${next} \[${pos}\]\`);  
}

const updateDOM \= (next, idx) \=\> {  
  // update the one span that has changed  
  const ele \= document.querySelector(\`\#w${idx}\`);  
  ele.innerText \= next \+ (RiTa.isPunct(words\[idx \+ 1\]) ? '' : ' ');

  // highlight updates as they happen  
  if (debugging) {  
    ele.style.backgroundColor \=  
      state.history\[idx\]\[0\] \=== next  
        ? '\#fff' // original  
        : state.outgoing  
        ? '\#fbb' // outgoing  
        : '\#bbf'; // incoming  
  }  
}

## **Starter CSS:**

\<style\>  
.container {  
 width: 80vw;  
}

.none {  
 display: none;  
}

.readerWindow {  
 width: 70vw;  
 text-align: center;  
}

.text {  
 opacity: .3;  
 transition: opacity .5s ease-in-out;  
}

.text.visible {  
 opacity: 1;  
}  
\</style\>

