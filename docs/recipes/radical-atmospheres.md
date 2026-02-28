---
title: Radical Atmospheres
chef: Andrew Demirjian
abstract: A workflow for reorganizing archival source texts using regular expressions
  and NLP to generate poetic material for audio augmented reality experiences.
description: >
  Radical Atmospheres is a recipe for creating audio augmented reality (AAR)
  poetry from archival source texts, developed in connection with Demirjian's
  work on The Young Lords in East Harlem. Rather than producing a finished piece,
  the recipe produces insights and material — a spoonful of inspiration — by
  examining a source text from fresh computational angles.

  The recipe uses two techniques: alphabetical sentence sorting, which reorganizes
  a document by the first letter of each sentence to reveal unexpected patterns
  and sonic resonances; and Key Word in Context (KWIC) concordance searching,
  which shows every instance of a chosen word surrounded by its neighboring words.
  Both are implemented in p5.js using the RiTa library.

  Working with a source text out of its intended linear order surfaces poetic
  material buried in bureaucratic or archival prose. The resulting excerpts can
  be recorded as audio and deployed in a physical location using apps like Echoes,
  Dreamwaves, or Roundware, creating an audio AR piece tied to specific geography.

  The recipe draws on a tradition of computational text analysis in e-lit, from
  Stephanie Strickland and Nick Montfort's Sea and Spar Between to Jackson Mac
  Low's Ridiculous in Piccadilly, while extending into the physical space of
  audio augmented reality.
genres:
  - Audio
  - Augmented Reality
custom_genres:
  - Audio AR
  - Archival poetics
difficulty_pans: 1
yields: >
  A set of poetically reorganized text excerpts from a source document, ready
  for recording as audio and deploying in a physical location or virtual
  equivalent using audio augmented reality applications.
github_link: https://rw-app-spaces-speak.surge.sh/
---

## Background

Like a food truck serving up delicious bites to throngs of people at lunch time,
audio AR is about meeting people where they are. AR may be thought of as a new
generation of technologically advanced versions of a plaque or memorial. This
connection to physical space can create a gravitational pull for e-lit writers
to explore archival materials and oral histories that connect to a specific place.
Listening to audio AR pieces can create an uncanny feeling of presence/absence,
as voices from the past mix with the current moment in the same location.

## From the Chef

This recipe does not produce a finished dish, but is intended to produce insights
or a spoonful of inspiration that can be turned into an al fresco meal. By
examining a text outside of its intended use — in this case, as a report to a
mayor — this methodology can help you find patterns that may not be readily
apparent when reading linearly for semantic content. Performing these different
ways of slicing and dicing helps me get a sense of distinctive flavors buried
within a text.

## Sample Before You Cook

- Sheila Heti, *Alphabetical Diaries*
- Stephanie Strickland & Nick Montfort, [Sea and Spar Between](https://nickm.com/montfort_strickland/sea_and_spar_between/)
- Andrew Demirjian, [Radical Atmospheres](https://rw-app-spaces-speak.surge.sh/)

## Ingredients

- Computer
- Phone with headphones or earbuds (for AAR playback)
- Code editor
- p5.js
- RiTa library
- A source text of 4,000+ words (as a `.txt` file)

**Preparation time:** 20 minutes (code) + variable recording time

## Method

1. Locate a source text of interest — preferably one with a meaningful connection
   to a physical location where the final audio will reside. Over 4,000 words
   will yield best results.
2. Save the text as a `.txt` file.
3. Upload the `.txt` file to a p5.js sketch using the `+` icon in the upper
   left corner of the p5 web editor.
4. Add the RiTa CDN link to your `index.html`:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/rita"></script>
   ```
5. Replace the filename in `loadStrings` with your `.txt` file name.
6. Run the code and look at the console. Your alphabetically sorted sentences
   appear there. Copy and paste into a new document to review — print it out
   and step away from the kitchen to a cozy place to focus.
7. Notice patterns. Are there groups of sentences starting with the same words?
   What words could be erased to open wider readings? How might you combine
   groups of patterns?
8. For any word that's particularly evocative, use the KWIC search to see every
   instance in context. Update the `word` variable in the code.

## Starter Code

```javascript
let txt, word;
let sorted;
let opts;

function preload() {
  txt = loadStrings('Report to the Mayor.txt');
}

function setup() {
  createCanvas(1000, 4000);
  textFont("Times New Roman", 10);

  let allwords = txt.join("\n");
  let sent = RiTa.sentences(allwords);
  let alphaSent = sent.sort();

  for (i = 0; i < alphaSent.length; i++) {
    console.log(alphaSent[i], '\n');
  }

  opts = { ignoreCase: true, ignorePunctuation: true, ignoreStopWords: false };
  RiTa.concordance(txt.join("\n"), opts);
  word = "Roldan"; // replace with your search term
}

function draw() {
  let kwic = RiTa.kwic(word, 8); // 8 words before and after
  // display logic omitted for brevity — see full code in p5 editor
  noLoop();
}
```

## Notes: Turning Text to Audio

1. After finding compelling excerpts, record yourself reading the text — or use
   a text-to-speech application, shaping delivery with commas and line breaks.
2. For voice quality, try a voice changer like elevenlabs.io — but take time to
   craft the voice carefully. AI voices geared toward corporate contexts can
   sound off-putting for poetic material.
3. For oral histories with existing audio, use Adobe Premiere to transcribe and
   search for your selected excerpts, then export phrases individually.
4. Upload audio files to an AAR app (Echoes, Dreamwaves, Roundware) and listen
   in your desired location.

## Variations

- Export each audio phrase individually and trigger them at random within a
  location using Roundware for an element of chance.
- Use `RiTa.phones()` to analyze sonic content of the source text, finding
  assonance or consonance. Try `RiTa.alliterations()` and `RiTa.rhymes()`.

## Further Reading

- Caroline Bergvall, Laynie Browne, et al., eds. *I'll Drown My Book: Conceptual Writing by Women*
- Susan Howe, *The Midnight*
- William Uricchio, "The Markers, Memories and Meanings Behind Today's AR"
