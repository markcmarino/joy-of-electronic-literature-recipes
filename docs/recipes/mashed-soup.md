---
title: Mashed Soup An Inform Tasting and Recipe
chef: Judith Pintar
abstract: A step-by-step Inform recipe for building a parser-based interactive story set in a kitchen, using custom actions and world modeling.
description: |
  "Mashed Soup" is both a playable parser-based interactive story and a step-by-step
  recipe for building one in Inform, the natural-language programming language for
  interactive fiction created by Graham Nelson. Unlike hypertext or choice-based
  platforms, parser IF uses text commands to build a simulated world: players type
  actions ("mash potato," "examine apron") and the system responds based on the state
  of the world model.

  The recipe begins with a "tasting"—a transcript of gameplay showing what the finished
  work looks like—then walks through the construction of each element: a kitchen room,
  a masher tool, three mash-able ingredients, a scenery container hiding the broth, and
  a player character carrying a chef's apron and grandmother's recipe card. The emotional
  core of Mashed Soup is grief and comfort: the player is having a hard day and makes
  their grandmother's soup to feel better, discovering family memories in object
  descriptions along the way.

  The technical core is a custom "mashing" action, explained through all six of Inform's
  rule types: before, instead, check, carry out, after, and report. The "mild" version
  ends when the potato is mashed; the "spicy" version adds actions for remembering,
  warming, and a final narrative resolution triggered by "warm my solitude."

  Pintar provides tasks at each step with prompts to adapt the recipe to the designer-
  chef's own kitchen, ingredients, and story.
genres:
  - Hypertext
difficulty_pans: 2
yields: |
  A parser-based interactive fiction in which player-cooks make soup by mashing
  ingredients in order, revealing a narrative of grief and family memory through
  object descriptions, custom actions, and a final emotional resolution.
github_link: https://mm45nx3c.play.borogove.io/
---

## Ingredients

- [Inform 7](https://ganelson.github.io/inform-website/) (free desktop application) — OR —
- [Borogove](https://borogove.app/) (free online Inform compiler, no installation needed)
- A kitchen setting and its objects (real or imagined)
- A personal or fictional narrative to weave through object descriptions
- Optional: [intfiction.org](https://intfiction.org/) community for support and education channel

## Method

**Play the sample first:** [https://mm45nx3c.play.borogove.io/](https://mm45nx3c.play.borogove.io/)

**Step 1: Create the Kitchen (Room)**

Rooms are the locations of your world. Each needs a name and description:
```
Cozy Kitchen is a room. "You are standing in the center of your cozy kitchen. A hotplate in front of you warms a pot of broth that you hope will become a savory soup."
```

**Step 2: Add a Cooking Tool (Thing)**

Things need a name, location, an initial appearance (shown in room description), and a long description (shown when examined):
```
a masher is in cozy kitchen. "Near at hand is a masher, clearly a tool engineered for perfect mashing."
The description of masher is "This wooden-handled masher is at least half a century old. It is still in great shape."
Understand "mashing tool" and "tool for mashing" as masher.
```

**Step 3: Add Ingredients and Containers**

Ingredients without initial appearances are listed automatically at the end of the room description. Scenery containers can "hide" what they contain:
```
buttery potato is in cozy kitchen.
The description of buttery potato is "A well-buttered potato is waiting to be mashed."
a small pot is a scenery container in cozy kitchen.
vegetable broth is in small pot.
```

**Step 4: Set Up the Player Character**

The player is created automatically; customize their description and give them starting items:
```
The description of the player is "You're having a hard day. When you were little your grandmother made soup to cheer you up. You figure it's worth a try."
The player is wearing a chef's apron.
The player is carrying a worn index card.
Understand "recipe" as worn index card.
```

Use `[one of]...[or]...[stopping]` in descriptions to give alternate responses on repeated examination.

**Step 5: Define a Custom Action (Mashing)**

Inform doesn't have a built-in mashing action. Define one:
```
A thing can be mashed or unmashed. A thing is usually unmashed.
Mashing is an action applying to one thing.
Understand "mash [something]" as mashing.
```

Then write rules for it (Inform processes these in strict order):
- **Before:** Check preconditions (e.g., must be holding the masher)
- **Instead:** Block or redirect specific cases (e.g., wrong order of ingredients)
- **Check:** Stop action if already mashed
- **Carry out:** Change the object's state from unmashed to mashed
- **After:** Update descriptions based on what has been mashed
- **Report:** Print the action narrative ("Mash! Mash! Mash!")

**Step 6: End the Story**

Trigger the ending with `end the story finally`:
```
Instead of warming solitude:
   if broth is unmashed:
       say "You're not sure what it means, but you should finish the soup first.";
   else:
       say "You run your finger across the final line in the recipe...";
       end the story finally saying "You serve yourself a bowl of Mashed Soup for One. It warms you through and through."
```

## Notes

- The "mild" version ends after mashing all three ingredients into the pot. The "spicy" version adds `remember`, `warm`, and modified `eat` actions for a fuller narrative arc.
- Inform compiles locally (desktop) or online at [Borogove](https://borogove.app/). For errors, check punctuation first—it is the most common source of Inform compiler errors.
- Expand the world by adding adjacent rooms: `Dark Pantry is east of Cozy Kitchen.`
- Full Inform documentation and community: [intfiction.org](https://intfiction.org/)
- Education-specific discussion: [intfiction.org/c/general/education/58](https://intfiction.org/c/general/education/58)
