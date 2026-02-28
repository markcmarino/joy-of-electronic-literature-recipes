---
title: Choice-Constrained Twine with Harlowe 3.x
chef: Anastasia Salter
abstract: An introduction to variables and conditional statements in Twine's Harlowe format, modeled on the landmark work Depression Quest.
description: >
  "Choice-Constrained Twine with Harlowe 3.x" teaches two concepts critical to both
  programming and electronic literature: variables and conditional statements. Using
  Twine's Harlowe 3.x story format, Anastasia Salter walks through building a system
  in which some choices are always available, others require the player to meet a
  threshold in a tracked stat, and others are permanently visible but always struck
  through—tantalizing but unreachable.

  The recipe is modeled on Depression Quest (Quinn et al., 2013), a landmark Twine
  work that uses this mechanic to simulate the experience of depression: the "right"
  choices are always visible, but often locked behind motivation thresholds the player
  cannot reach. The recipe explains how to set up a startup passage with randomized
  and default stat values, a persistent header displaying those stats to the reader,
  and an optional title passage with a character-naming input box.

  Salter then demonstrates a branching choice passage where each option is gated by
  a different stat threshold, with one always-available fallback ensuring the player
  can never be truly stuck. The recipe uses Harlowe 3.x macros throughout—(set:),
  (if:), (print:), (align:), (box:), (border:)—and notes that many of these can be
  set via Twine's graphical interface without typing code. Sample code is provided
  throughout and linked in the resources.
genres:
  - Hypertext
difficulty_pans: 1
yields: >
  A Twine story with stat-tracking variables, a persistent header display, and
  conditional choice gates that unlock or restrict narrative paths based on the
  player's accumulated decisions.
github_link: https://github.com/AMSUCF/Interactive-Digital-Narratives/blob/main/GamingTwine.html
---

## Ingredients

- [Twine 2.x](https://www.twinery.org) (free, download or use online; Harlowe 3.x is the default story format)
- A narrative concept with trackable player attributes (motivation, curiosity, kindness, etc.)
- Optional: [Depression Quest](http://www.depressionquest.com/dqfinal.html) as a reference model
- Optional: [Harlowe 3.x Manual](https://twine2.neocities.org/) by Leon Arnott

## Method

**Step 1: Create a startup passage**

1. Create a new passage named "Stats" (or similar) and tag it `startup`. This passage runs before the story begins and sets initial variable values:
   ```
   {
   (set: $curiosity to (random: 10,15))
   (set: $ambition to (random: 10,15))
   (set: $persistence to (random: 10,15))
   (set: $kindness to 6)
   (set: $charName to "Chara")
   }
   ```
   The `{ }` wrapper tells Harlowe to process this as a code block without displaying line breaks.

**Step 2: Add a persistent header**

2. Create a passage tagged `header`. It will appear at the top of every passage. Use Harlowe macros to display current stat values:
   ```
   (align:"=>")+(box:"=XX=")[(border:"dotted")+(border-colour:purple)[''Name: (print: $charName)''
   Curiosity: (print:$curiosity)
   Ambition: (print:$ambition)
   Persistence: (print:$persistence)
   Kindness: (print:$kindness)]]
   ```
3. To suppress the header on a specific passage (e.g., the title screen), wrap the header code in:
   ```
   (if: (passage:)'s name is not "Title")[...]
   ```

**Step 3: Add a title/intro passage**

4. Create a passage named "Title" with a welcome message and an optional character name input:
   ```
   Welcome to our story.
   Name your character: (input-box: bind $charName, "XXX=", 1, "Chara")
   [[You can't re-roll in life->Play]].
   ```

**Step 4: Add constrained choices**

5. In story passages, update stats and gate choices with conditional statements:
   ```
   You dig deeper, quietly asking around and observing their behavior.
   (set: $curiosity to $curiosity + 1)
   (set: $persistence to $persistence - 1)
   Do you…
   (if: $persistence > 11)[[[Confront them directly->Confront]]]
   (if: $curiosity > 13)[[[Keep observing for more evidence->Observe]]]
   [[Walk away, unsure of what to believe->WalkAway]]
   ```
6. Always include at least one choice with no stat requirement to prevent dead ends. This unconditioned option is consistently the least desirable—as in Depression Quest, the path of least resistance is always open.

## Notes

- Depression Quest makes locked choices *visible* with strikethrough HTML (`<del>`) and light text color, so the player always knows what they cannot do. This is a design choice, not a technical requirement.
- Harlowe 3.x macros can also be set via Twine's graphical interface drop-down menus if you prefer not to type code.
- Boolean (true/false) variables track significant story events; integer variables track nuanced values that change incrementally.
- Full Harlowe 3.x documentation: [twine2.neocities.org](https://twine2.neocities.org/)
- Sample code from Salter's class: [GitHub](https://github.com/AMSUCF/Interactive-Digital-Narratives/blob/main/GamingTwine.html)
