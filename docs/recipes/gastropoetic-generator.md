---
title: Gastropoetic Generator
chef: Talan Memmott, Scott Rettberg
abstract: A limerick-form poetry generator that produces menus for real in-person feasts, blending constraint-based poetics with culinary performance.
description: |
  "Gastropoetic Generator" arises from Talan Memmott and Scott Rettberg's collaborative
  projects The Limerick Diet (2019) and Quarantine Quatrains (2020), in which
  constraint-based poetry generation produced not only aesthetically pleasing verse but
  actually edible meals. The generator uses the AABBA limerick form as a structural
  scaffold for producing randomized menus, drawing from arrays of locally sourced
  ingredients, cooking methods, sauces, and seasonings. The resulting output functions
  simultaneously as a poem, a menu, and a performance score.

  The recipe provides a working JavaScript template that readers can copy, modify with
  their own vocabulary and rhymes, and open in any browser. The generator accommodates
  dietary restrictions as variables and includes substitution logic for unavailable
  ingredients. Memmott and Rettberg emphasize that the constraint-driven approach is
  generative rather than restrictive: each generated menu is different, chefs interpret
  the same recipe differently, and the gap between poetic and culinary execution becomes
  a site of creative play.

  The project scales from intimate live-cooking performances for eight diners to
  distributed events where participants around the world prepare the same algorithmically
  generated menu simultaneously. A key principle from Quarantine Quatrains: cooking
  itself is a generative experience, and chefs interpret recipes just as readers
  interpret poems.
genres:
  - Generative Poetry
  - Performance/Experience
difficulty_pans: 2
yields: |
  A working JavaScript limerick generator that outputs a randomized menu serving 1–8
  diners, suitable for live cooking performances, distributed feasts, or classroom
  demonstrations of constraint-based poetics.
github_link: https://github.com/placeholder
---

## Ingredients

- A code or text editor (Sublime, BBEdit, VS Code, or any basic editor)
- A web browser (to run the HTML generator)
- Locally sourced or seasonal ingredients as your vocabulary source
- Arrays of: proteins, cooking methods, vegetables, sauces, seasonings, rhyme sets
- Optional: streaming setup for live performance; social networks for distributed events

## Method

1. **Plan your poetic structure.** On paper or in a spreadsheet, map out limerick components: lines 1, 2, and 5 use three anapests each; lines 3 and 4 are shorter. Design a slot-style structure where nouns, verbs, and adjectives can be substituted within a template, and plan rhyming ingredients accordingly.

2. **Build your culinary vocabulary.** Focus on locally sourced, seasonal ingredients. Create arrays for:
   - Protein
   - Cooking method
   - Vegetable
   - Sauce
   - Seasonings
   Also create separate arrays for omnivore, vegetarian, and pescatarian options.

3. **Copy the starter code** (provided in the recipe appendix) into a text editor. Replace the sample arrays with your own locally sourced vocabulary and rhymes. Ensure end-words rhyme across your `rh` arrays.

4. **Don't fear false rhymes.** As in The Limerick Diet, limericks can take shortcuts on scansion ("mushrooms" can rhyme with "zoom zoom"). Comic effect and quality cuisine take priority over poetic mastery.

5. **Provide substitutions.** Include fallback ingredients for when primary choices aren't available (e.g., "Filet Mignon > Ground Beef > Kidney Beans").

6. **Test rigorously.** Save your file as `.html` and open it in a browser. Reload many times to check that all generated combinations are edible. Cook representative sample meals to confirm.

7. **Generate a menu and shop.** For live performance, generate the menu in real time with diners present, allowing multiple reloads to select the final dishes. Then shop and cook accordingly.

8. **Implement the performance layer.** Plan your format: live cooking show, distributed simultaneous cooking, or classroom exercise. Turn on cameras and begin cooking.

## Notes

- The starter code is based on The Limerick Diet and produces a main course limerick. Extend to multiple courses by adding more generator modules.
- **For intimate gatherings:** Generate in real time during cooking; stream with live commentary; serve up to 8 diners; emphasize artisanal presentation.
- **For distributed events:** Generate menus in advance; allow participants to cook at home simultaneously across time zones; encourage social media documentation.
- **Advanced modifications:** Add wine pairing algorithms, shopping list generators, post-meal review generators, or use more complex poetic forms (sonnets, sestinas) for more elaborate dishes.
- Consider culture-specific adaptations: haiku-based sushi, sonnet-structured pasta, ghazal-inspired curry spice combinations.
- Related works: *The Limerick Diet* (2019), *Quarantine Quatrains* (2020) by Memmott and Rettberg.
