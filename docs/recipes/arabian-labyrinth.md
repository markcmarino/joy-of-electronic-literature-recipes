---
title: The Arabian Labyrinth Technique
chef: Ryan Veeder
abstract: Create expansive text adventure locations using coordinate-based virtual space in Inform 7.
description: |
  This technique allows authors to create the illusion of vast, explorable spaces in parser-based interactive fiction without defining hundreds of individual rooms. Instead of creating a massive grid of interconnected locations, the Arabian Labyrinth technique uses a single Inform 7 room with coordinate tracking to simulate wandering through expanses like deserts, forests, or moonscapes. Named after Jorge Luis Borges' story about a king who abandons his enemy in the desert, this method creates a labyrinth "which has no stairways to climb, nor walls to impede thy passage." The technique involves tracking player position with latitude and longitude variables, using tables to handle directional movement, and implementing scenery rules to make objects and landmarks appear at specific coordinates. This creates navigation puzzles distinct from traditional maze-based interactive fiction, allowing for impressions of wandering through woodland, windblown deserts, swamps, or even lunar surfaces while maintaining the technical simplicity of a single location.
genres:
  - Hypertext
difficulty_pans: 4
yields: |
  A functionally infinite explorable space that feels like a real expanse, with discoverable landmarks, items, and boundaries that can be visible or invisible.
github_link: https://playfic.com/games/Afterward/arabian-labyrinth
---

## Ingredients

- Inform 7 compiler (available for MacOS, Windows, Linux)
- Text editor or Inform 7 IDE
- Web apps like Playfic or Borogove (optional, for online compilation)
- Basic understanding of Inform 7's pseudo-English syntax
- One good reason (optional) to inflict this on your players

## Method

### Understanding Inform 7 Basics

Inform 7 uses natural-English-like syntax for creating parser-based interactive fiction. A simple game might look like:

```
Chuck's Pet Shop is a room.
The puppy is an animal in Chuck's Pet Shop.
The cash register is a closed openable container in Chuck's Pet Shop.
```

This compiles into a playable game where players can type commands like `OPEN CASH REGISTER` and `TAKE MONEY`.

### The Arabian Labyrinth Technique

**Step 1: Create the Basic Illusion**

```
Desert is a room. "You are hopelessly lost."

Check going while player is in Desert:
    say "You trudge toward [the noun].";
    try looking instead.
```

This makes it look like the player is moving, but they remain in the same location.

**Step 2: Add Coordinate Tracking**

```
Longitude is initially 0.
Latitude is initially 0.

Check going while player is in Desert (this is the desert movement rule):
    if the noun is a direction listed in the Table of Direction Values:
        choose row with direction of the noun in Table of Direction Values;
        now longitude is longitude plus delta-long entry;
        now latitude is latitude plus delta-lat entry;
        say "You trudge toward [the noun].";
        try looking instead.

Table of Direction Values
direction    delta-long    delta-lat
north        0             1
northeast    1             1
east         1             0
southeast    1             -1
south        0             -1
southwest    -1            -1
west         -1            0
northwest    -1            1
```

**Step 3: Implement Borders**

Visible borders:
```
Before going while player is in Desert:
    if (the noun is northwest or the noun is north or the noun is northeast) and latitude is 5:
        say "The sandstorms become too thick to navigate in that direction." instead.
```

Invisible borders create seamless boundaries without alerting the player.

**Step 4: Add Dynamic Scenery**

```
Desert scenery rules is a rulebook.

A desert scenery rule (this is the bleached skull appearance rule):
    if longitude is 1 and latitude is 1:
        now the bleached skull is in the location;
    else:
        remove the bleached skull from play.

The bleached skull is a fixed in place thing.
```

Insert `follow desert scenery rules;` before `try looking instead` in the desert movement rule to make objects appear at specific coordinates.

**Step 5: Hide Important Locations**

```
A desert scenery rule (this is the oasis appearance rule):
    if latitude is -4 and longitude is 3:
        now the oasis is in the location;
    else:
        remove the oasis from play.

The oasis is a fixed in place thing.
```

Provide navigation aids like:
- Treasure maps: `The description of the scrap of paper is "The numbers (-4, 3) are still barely legible."`
- GPS devices: `The description of the GPS is "This thing says your current coordinates are ([latitude],[longitude])."`

## Notes

### Preventing Item Dropping

The illusion breaks if players drop items and see them persist when they "move." You can prevent this:

```
Before dropping something while player is in Desert:
    say "(Insert here some excuse about littering.)" instead.
```

Alternatively, implement rules to make dropped items "stay" at their coordinates.

### Publishing Your Work

Inform 7 can output games as:
- `.zblorb` or `.gblorb` files (playable in interpreters like Gargoyle)
- Web pages you can upload anywhere
- Projects on Playfic or Borogove for online play

### Examples

See the full working example at [Playfic: Arabian Labyrinth](https://playfic.com/games/Afterward/arabian-labyrinth)

Veeder has used this technique in works like:
- "Ryan Veeder's Authentic Fly Fishing" (Iowan woodland)
- "Letavermilia" (windblown desert)
- "Crocodracula: What Happened to Calvin" (Florida swamp)
- "The Little Match Girl 2: Annus Evertens" (moon surface)

### Further Reading

- Borges, Jorge Luis. "The Two Kings and the Two Labyrinths"
- Inform 7 documentation: https://ganelson.github.io/inform-website/
- Playfic: https://playfic.com/
- Borogove: https://borogove.app/
