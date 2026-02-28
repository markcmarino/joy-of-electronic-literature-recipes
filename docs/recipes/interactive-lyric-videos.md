---
title: Interactive Lyric Videos with Stepworks
chef: Erik Loyer
abstract: Two recipes for creating syllable-accurate lyric videos performable live
  using Stepworks and Google Sheets, for single and multiple vocalists.
description: |
  Interactive Lyric Videos with Stepworks offers two recipes for creating lyric
  videos that can be performed live — syllable by syllable, one keypress at a
  time — turning language into a kind of drum.

  Stepworks is a free website that uses a Google Sheets spreadsheet as a "score"
  to choreograph text on screen. Each mouse click or keypress advances one row
  in the score, allowing the performer to drive the timing of the display in sync
  with music. The result creates a peculiar feedback loop: one feels simultaneously
  that they are "playing" and "being played by" the singer's words.

  Recipe 1 covers a single-vocalist lyric video: lyrics are split syllable by
  syllable into a spreadsheet, loaded into Stepworks, and performed live in time
  with the song. Recipe 2 extends this to multi-channel lyric videos, assigning
  each vocalist their own column and screen region — a technique that proved
  particularly effective for dense, multi-character vocal performances such as
  those from Hamilton, which generated millions of views when fans used Stepworks
  to create their own versions.

  The recipes draw on Loyer's interest in everything having a voice — a fascination
  born from reading Joyce and evolved through years of typographic animation work.
genres:
  - Performance/Experience
  - Word Manipulation
custom_genres:
  - Lyric video
  - Typographic animation
difficulty_pans: 2
yields: |
  One or two interactive lyric videos performable live in time with music,
  syllable by syllable, using a spreadsheet score and the Stepworks tool as a
  rhythmic text instrument.
github_link: https://step.works
---

## Background

Have you ever watched a lyric video on YouTube, where the words to a song appear
on screen in time with the music? Words can have such surprising, sudden effects
on us — and yet they have no physical presence when spoken or sung. The lyric
video appeals to the part of us that wants visible language to be conjured in
real time by a singer's voice.

Stepworks grew from that fascination, first explored in Loyer's 2007 piece
"Swing," in which a user's gestures caused lyrics to advance one syllable at a
time. Everything speaks — lyric videos can help us listen.

## About Stepworks

[Stepworks](https://step.works) is a free website for creating lyric videos and
rhythm-driven text experiences. Use **Stepworks Classic** (Google Sheets-based)
for these recipes. Find it by opening the website and scrolling to the Classic link.

## Recipe 1: Single-Channel Interactive Lyric Video

**Rating:** 🍳 one pan, easy | **Time:** 15–25 minutes | **Yields:** One lyric video

**Ingredients:** Computer, text editor, lyrics from a favorite single-vocalist song, Google Sheets, Stepworks

**Directions:**
1. Pick a favorite song with a single vocalist — not too long, one you can sing by heart. Copy the lyrics into your text editor.
2. Split the lyrics into syllables, one syllable per line. A syllable-splitter website can insert hyphens; then use find-and-replace to put each syllable on its own line.
3. Add `&` to the beginning of every syllable that continues a word (so it appends rather than replaces). Include spaces between words. Don't add `&` at the start of stanzas where you want text to refresh.
   ```
   Hel
   &lo,
   & won
   &der
   &ful
   & world
   ```
4. Open Google Sheets. Put the vocalist's name in bold at the top of column A. Paste the syllables into the rows below.
5. Give the spreadsheet a title. Share it as "Anyone with the link can view."
6. Copy the spreadsheet URL. Open `https://step.works/index.php/show/vocal-grid`, scroll to bottom, click "Load," paste the URL, click "Done."
7. Click the red "Click here" circle to begin. Click or press keys to step through syllables. Make changes in the spreadsheet and click "Refresh" to reload.
8. Put on the song and perform — click in time with the music.

**Notes:** Screen-capture your performance and edit it together with the song to create a shareable piece.

## Recipe 2: Multi-Channel Interactive Lyric Video

**Rating:** 🍳🍳 two pans, moderate | **Time:** 25–45 minutes | **Yields:** One lyric video

**Ingredients:** Computer, text editor, lyrics from a multi-vocalist song, Google Sheets, Stepworks

**Directions:**
1. Pick a song with two or more vocalists (musicals are a great source).
2. Split and syllabify the full lyrics as in Recipe 1.
3. Create one column per vocalist in Google Sheets. Put each vocalist's name in bold at the top of their column.
4. Paste all lyrics into column A first, then cut and paste each vocalist's lines into their respective column. Each row = one syllable; if two vocalists sing simultaneously, their syllables share a row in their respective columns.
5. Share, load into Stepworks, and perform as in Recipe 1.

**Notes:** For extremely dense pieces, consider assigning each row to a fixed duration (one beat) rather than one syllable, grouping multiple syllables under a single keypress. See: [step.works/index.php/create/delays](https://step.works/index.php/create/delays)

## Resources

- ["Swing" lyric video](https://erikloyer.com/index.php/projects/detail/swing)
- [Stepworks](https://step.works)
- [Vocal Grid template](https://step.works/index.php/show/vocal-grid)
- [Timing documentation](https://step.works/index.php/create/delays)
