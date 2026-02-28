---
title: Full Words Ramble
chef: Daniel C. Howe, John Cayley
abstract: A browser text that continuously replaces its own words with rhymes and
  sound-alikes, rambling away from source prose before wandering back again.
description: >
  Full Words Ramble is a word-replacement poetry system built with the RiTa
  natural language processing library. The piece takes a prose text and,
  word by word, substitutes each word with a phonetically or orthographically
  similar word — a rhyme, a sound-alike, or a spelling-alike — constrained to
  the same part of speech. The text wanders incrementally away from its source,
  then returns: the system tracks a history of replacements and can reverse them,
  rambling back toward where it started.

  The recipe provides starter code for Observable, a live-coding notebook
  environment, making the result immediately shareable and tweakable in the
  browser. The essential functions are RiTa.rhymes(), RiTa.soundsLike(), and
  RiTa.spellsLike(), which return candidate replacement words from which one is
  selected at random. Common grammatical stop words are preserved to maintain
  readability. Short words (under 4 letters) are skipped.

  Chef Cayley recommends Observable as the ideal environment for preparation,
  cooking, and plating, as it creates a live, shareable experience. A
  fully-developed version, Preoccupations, was published in The New River.

  The key ingredient is Chef Howe's RiTa library, which provides the linguistic
  infrastructure — phoneme analysis, part-of-speech tagging, and similarity
  functions — that makes the ramble possible.
genres:
  - Word Manipulation
  - Generative Poetry
difficulty_pans: 2
yields: >
  A continuously evolving browser text that wanders from its source prose through
  word-by-word phonetic and orthographic substitution, then wanders back, readable
  live and shareable as an Observable notebook.
github_link: https://observablehq.com/@shadoof/full-words-ramble
---

## Background

Recipes for rambles — think of them like fruit crumbles, with an even greater
range of fine-grained flavor palettes — usually have prose as their main
ingredient. It was Chef Howe who first started using functions built into the
RiTa library to find and replace words according to various criteria for
similarity. Replacements can rhyme, look-like (in terms of spelling), or
sound-like (in terms of phonemes), and are chosen to occupy the same part of
speech as the word being replaced.

Rambles can be made to ramble forever, or at a certain point, to return.
Returning rambles record a history of where they have been and then wander back
in a shuffling order toward their textual starting point.

## Sample Before You Cook

- [ramble](https://thelaob.com/a0/ramble/) — the original piece by Daniel C. Howe & John Cayley, May 2021
- [Preoccupations](https://thenewriver.us/preoccupations/) — a fully-developed haute-cuisine version published in The New River
- [Live-code notebook on Observable](https://observablehq.com/@shadoof/full-words-ramble)

## Ingredients

- One or two paragraphs of ambulatory prose (your own)
- JavaScript
- HTML5
- CSS
- [RiTa library](https://github.com/dhowe/ritajs) (Chef Howe's NLP library)
- Observable (recommended) or another JavaScript environment

**Preparation time:** 1 hour to as long as you like

## Method

1. **Replace the prose.** Start by substituting your own text for the sample
   prose in `supplyText`.

2. **Set up the display.** The text appears on a web page inside an HTML div:
   ```html
   <div id="display" class="container"></div>
   ```

3. **Load RiTa.** In Observable: `RiTa = require("rita@2")` or use `import`.

4. **Prepare the text.** The `supplyText` is tokenized into a `words` array,
   parts of speech are tagged into a `partsOfSpeech` array, and HTML spans are
   created for each word by the `spanify` function.

5. **Customize the update function.** This is where word replacements happen.
   The code finds candidate replacements using `RiTa.rhymes()`,
   `RiTa.soundsLike()`, and `RiTa.spellsLike()`, picks one at random, and
   swaps it into the display. Everything else is visualization cream.

6. **Set `updating = true`** to let the text go off on its ramble.

## Starter Code

```javascript
const supplyText = "by the time the light has faded, as the last of the reddish
gold illumination comes to rest, then imperceptibly spreads out over the moss
and floor of the woods, you or I will have set out on several of yet more
circuits at every time and in all directions..."

const words = RiTa.tokenize(supplyText)
const partsOfSpeech = RiTa.pos(supplyText)

const update = () => {
  if (!updating) return;
  if (state.outgoing) {
    const r = Math.floor(Math.random() * words.length);
    for (let i = r; i < words.length + r; i++) {
      const idx = i % words.length;
      const word = words[idx].toLowerCase();
      const pos = partsOfSpeech[idx];
      if (word.length < 4) continue;
      if (stopWords.includes(word)) continue;
      const rhymes = RiTa.rhymes(word, { pos });
      const sounds = RiTa.soundsLike(word, { pos });
      const spells = RiTa.spellsLike(word, { pos });
      const similars = [...rhymes, ...sounds, ...spells];
      if (similars.length < 2) continue;
      const next = RiTa.random(similars);
      if (next.length < 4) continue;
      if (next.includes(word) || word.includes(next)) continue;
      words[idx] = next;
      state.history[idx].push(next);
      break;
    }
  }
  updateDOM(next, idx);
}
```

## Starter CSS

```css
.container { width: 80vw; }
.text { opacity: .3; transition: opacity .5s ease-in-out; }
.text.visible { opacity: 1; }
```

## Notes

The full notebook, including visualization and the returning ramble logic,
is available on Observable where you can see it working in real time and fork
it for your own use. JavaScript in the notebook may need slight adaptation for
use in other environments such as node.js.
