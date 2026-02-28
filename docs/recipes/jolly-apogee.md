---
title: Jolly Apogee A Minimal Embodied Gesture Poem
chef: Judd Morrissey
abstract: A smartphone gesture poem activated by bodily movement, drawn from a large-scale performance merging embodied poetics and queer archive.
description: >
  "Jolly Apogee" is a minimal embodied gesture poem developed from the closing text of
  ATOM-r's large-scale performance The Operature, a work exploring the archive of Samuel
  Steward—Chicago writer, tattoo artist, and friend of Gertrude Stein—alongside the
  history of the anatomical theatre and embodied queer desire. Judd Morrissey built the
  poem in p5.js, designed to be activated on a smartphone: the reader holds the device
  in landscape mode, then moves their hand and arm with force in the direction indicated
  by an on-screen icon. The phone's accelerometer detects the gesture and advances the
  poem line by line, encouraging simultaneous reading aloud and physical movement
  through space.

  The recipe offers a body-writing workflow: participants write freely in response to a
  David Wojnarowicz image and the prompt "Reflect upon the history of your body as both
  forensics and banquet," then substitute their own lines into the poem's source array
  in the p5.js editor. A parallel exercise asks writers to reflect on the life of a body
  from another time.

  The recipe draws on the concept of the "transhistorical crush"—artists communicating
  across time through aesthetic and ethical alignment—as a framework for situating one's
  own body within a literary lineage. The poem is remixable and Morrissey invites anyone
  who creates a new version to share it, with the aim of hosting remix poems and
  performing them together at future ELO events.
genres:
  - Performance/Experience
  - Word Manipulation
difficulty_pans: 3
yields: >
  A remixable p5.js gesture poem performed with a smartphone, where bodily movement
  through space triggers lines of text—suitable for solo performance, workshop
  facilitation, or collaborative literary event.
github_link: https://tinyurl.com/Operature
---

## Ingredients

- A smartphone or tablet with accelerometer (iOS or Android)
- p5.js web editor account (free): https://editor.p5js.org/
- Source poem at: https://tinyurl.com/Operature
- Editable source code at: https://tinyurl.com/operEdit
- 20+ minutes for writing exercises
- A body

## Method

**Orientation: Device and Body Axes**

Familiarize yourself with the smartphone coordinate system:
- **X axis:** East–West (east is positive)
- **Y axis:** North–South (north is positive)
- **Z axis:** Up–Down, perpendicular to ground (up is positive)

Consider, in parallel, the planes of the human body: sagittal (left/right), coronal (front/back), transverse (top/bottom).

**Writing Exercises**

1. Contemplate the image *Self-Portrait* by David Wojnarowicz and his text: *"When I put my hands on your body your flesh I feel the history of the body."*
2. Write freely for 10+ minutes in response to the prompt: *Reflect upon the history of your body as both forensics and banquet.*
3. Write freely for 10+ minutes in response to the prompt: *Reflect upon the life of a body from another time (as both forensics and banquet).*
4. Consider: Who is your transhistorical crush? (Artists look at other artists across time, tangling language together to produce new sentences and distinct syntax.)

**Experiencing the Source Poem**

1. On your smartphone, navigate to: https://tinyurl.com/Operature
2. Hold the device in landscape mode.
3. After tapping the title button, move your hand and arm with some force in the direction the finger icon is pointing. The gesture must be strong enough to trigger the accelerometer threshold.
4. Continue gesturing to bring up new lines of the poem. Read aloud as you go.

**Remixing the Poem**

1. Open the editable source in the p5.js editor: https://tinyurl.com/operEdit
2. Log in or sign up, then save the code as your own copy.
3. Navigate to `poem.js` (tap the arrow next to `sketch.js` to access other files).
4. Replace the quoted lines in the array with lines from your writing exercises. As a constraint, consider leaving 20% of the original poem intact.
5. You may add or delete items in the array as needed; the structure remains the same.
6. Key variables in `sketch.js` are annotated for those who want to programmatically adjust the accelerometer threshold or other mechanics.
7. To test on your phone: File → Share → copy the fullscreen link and text or email it to yourself.

## Notes

- The poem was co-developed through ATOM-r (Anatomical Theatres of Mixed Reality), Morrissey's collaboration with performance artist Mark Jeffery.
- The Operature drew from the life and archive of Samuel Steward: a coded card catalogue of sexual encounters, writings, drawings, and biological samples spanning 50+ years.
- The generated p5.js sketch name "Jolly Apogee" is itself a kind of found poetry.
- If you create a remix, find Judd Morrissey and share it—he intends to host remix poems and perform them at future ELO events.
- Related performance documentation: https://vimeo.com/224378134
