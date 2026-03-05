---
title: Choice-Constrained Twine with Harlowe 3.x
chef: Anastasia Salter
abstract: An introduction to variables and conditional statements in Twine's Harlowe format, modeled on the landmark work Depression Quest.
description: >
  Please, write a description of 250 words or less.
genres:
  - Hypertext
difficulty_pans: 1
yields: >
  A Twine story with stat-tracking variables, a persistent header display, and
  conditional choice gates that unlock or restrict narrative paths based on the
  player's accumulated decisions.
github_link: https://github.com/AMSUCF/Interactive-Digital-Narratives/blob/main/GamingTwine.html
---

# Choice‑Constrained Twine with Harlowe 3.x

Anastasia Salter  
Professor of English  
University of Central Florida

**Class of E-lit:** Twine game/stories  
**Dish:** An introduction to variables and conditional statements in Twine (Harlowe 3.x)  
**Required ingredients:** Twine application available free from [www.twinery.org](http://www.twinery.org)  
**Preparation and cooking time:** 30-45 minutes  
**Number of servings and serving size:** one Twine game/story  
**Rating: 🍳** one pan, easy

**From the chef:** This beginner‑friendly recipe for working with Twine 2.X authoring software is intended as an introduction to two concepts critical to programming and electronic literature: variables and conditional statements. Twine was first released by Chris Klimas in 2009 and has been regularly updated and expanded upon by other contributors to the open‑source project, resulting in the current Twine 2.X authoring software that works both through the web and as a downloadable program. Twine is a tool for making hypertextual works, popular for interactive fiction and games, but open for experimentation. As a low-code tool, Twine allows for complex procedural elements, but it doesn’t require the user to have coding knowledge to create compelling narratives. Twine’s basic structures of links and passages encourage new storytellers to build branching works, but to control the reader’s progression through those branches the author must engage at the layer of code. Relatively simple systems of choice‑based interactions can enable significant, nuanced storytelling: for example, *Depression Quest* (Quinn et al.) stands out as a landmark Twine work that deliberately stops the user from progressing down the path of healthy decision‑making: throughout, the player can see the choices that are not available. A combination of status indicators and strike‑through highlighting draws the player’s attention to all the choices that are unavailable.

Most notably, the apparent “right” choice is constantly visible to the reader, but at the level of code, that choice is always an illusion. Take, for instance, this decision point early in the game:

```
<<if $motivation gte 9>>[[2. Reluctantly sit down at your desk and try and make yourself do something|startWork]]<<else>><html><FONT COLOR="#D1D1D11"><del>2. Reluctantly sit down at your desk and try and make yourself do something</FONT></del></html><<endif>>

<<if $motivation gte 5>>[[3: Turn on the TV, telling yourself you just need a quick half hour to unwind from work|watchTV]]<<else>><html><FONT COLOR="#D1D1D11"><del>3: Turn on the TV, telling yourself you just need a quick half hour to unwind from work</FONT></del></html><<endif>>
```

The next two choices are both available, as the links are functional. However, they require the player to be in a state in which they are accessible: the code “if $motivation gte 9” acts as a conditional statement, checking to see if the current motivation is greater than or equal to the value of nine. The next decision — the next best option — is structured similarly, but with a motivation lock of five.

[[4: Crawl into bed. You’re so stressed and overwhelmed you couldn’t possibly accomplish anything anyways.|gotoBed]]

The last decision — the worst decision, given the looming deadlines the character is facing — is always available, ensuring the player can always progress. One of the biggest challenges with this type of system is making sure that the player can progress as intended: that is to say, we need to avoid dead ends and paths that cannot possibly progress. The easiest way to ensure there is always a choice is to have a single option that isn’t behind a conditional statement — that path, in *Depression Quest*, is consistently the least desirable option, or the path of least resistance.

To build a system like this, we need to start by deciding what variables control the game’s progression and logic. *Depression Quest* sets up several in the first passage (historically named the “Start” passage in Twine one), tracking both significant moments as Boolean (true or false) variables and other values, such as motivation, as integers to allow for more nuanced changes throughout the game. Looking at the code, we can see that the player’s initial motivation is nine, enabling a full choice of decisions at the first major branching point:

```
{
(set: $curiosity to (random: 10,15))
(set: $ambition to (random: 10,15))
(set: $persistence to (random: 10,15))
(set: $kindness to 6)
(set: $charName to "Chara")
}
```

The syntax here reflects an earlier era of Twine, but the logical structures are the same as we will use to make our own version in Harlowe 3.X. Harlowe 3.X is, as of mid‑2025, the default story format of Twine 2.X and the one I most commonly teach due to its flexibility in styling and well‑designed structures for adding additional interactive elements such as this choice system. The format is maintained by Leon Arnott as an open‑source project and has gone through many iterations, each building the sophistication of the integration of built‑in interaction options and styling features (Arnott). In the most recent iterations, many of these are built into the graphical interface, so if you prefer not to type code, you can follow this recipe by selecting the options throughout from the drop‑down menus in the passage editor.

## **Mixing Your Own Choice‑Constrained Twine**

To start your conditional system, first open Twine 2.X and begin a new project. Unless you’ve made changes to your default settings, this story will already be in the Harlowe format. Harlowe recognizes special passage types through tags: to begin, create a passage called something like “Stats” to track your reader’s progression, and give it the tag *startup.* This passage contains the starting values of all the “stats,” or attributes assigned to the player. You can generate the initial stats randomly, as in this recipe’s numerical values below, or assign defaults, as with the character name and kindness values here. Think creatively about what you want to track — this is a way to build long‑term consequences for player choices. For example:

```
{

(set: $curiosity to (random: 10,15))

(set: $ambition to (random: 10,15))

(set: $persistence to (random: 10,15))

(set: $kindness to 6)

(set: $charName to "Chara")

}
```

A few things to note in this syntax: the { } contain the code and signal to Harlowe not to display line breaks for this processing task. This is a standard wrapper for functions in JavaScript, but here it simply indicates a block of code, not unlike the \<silently\> tags that surrounded the original *Depression Quest* code.

Next, we’ll add a persistent display like the one that notifies the reader of their current motivation at the bottom of every passage. Harlowe 3.X has two easy options for adding a persistent user interface: the *header* or the *footer.* Tagging a passage with one of these reserved tags will add a persistent extra set of content to every other passage — this is a great way to add any status information, inventory, or other features throughout a work.

For this recipe, create a passage tagged *header.* This will appear at the top of every passage by default. *Depression Quest* handled this with stylized images corresponding to the different possible values of the motivation variable; however, in Harlowe, it is easier to add more elaborate formatting right in the code with macros.

Here’s a simple example of displaying the same values set in the code in our *startup* passage:

```
(align:"=>")+(box:"=XX=")[(border:"dotted")+(border‑colour:purple)[''Name: (print: $charName)''

Curiosity: (print:$curiosity)

Ambition: (print:$ambition)

Persistence: (print:$persistence)

Kindness: (print:$kindness)]]
```

Notice there are a few other Harlowe 3.X macros at work in this recipe, which allow our stats to display more distinctly from the rest of the passage. The first macro, *align,* sets the text at an alignment indicated by the direction of the arrow (in this case, right); then, *box* creates an outline surrounding the text, and the two properties for *border* determine the display. The rest of the code simply prints the value in each variable — this will change as the reader progresses.

We can further add a passage that doesn’t include this display if we want to give the player an opportunity to add choices. For instance, if we add a passage named “Title,” it might contain a welcome statement and an input box for saving the character name:

```
Welcome to our story.

Name your character: (input‑box: bind $charName, "XXX=", 1, "Chara")

Your stats are:

*Curiosity: (print:$curiosity)*

*Ambition: (print:$ambition)*

*Persistence: (print:$persistence)*

*Kindness: (print:$kindness)*

[[You can’t re‑roll in life->Play]].
```

Currently, this allows the player to input a name for their character. You can use a similar structure for anything you’d like to make dependent on player input. To avoid displaying the stats on this page (before the reader has even selected a name), we simply wrap the previous code with a conditional statement that checks to make sure we’re on a passage after the “Title” before displaying the contents.

```
(if: (passage:)'s name is not "Title")\[...\]
```

Now, we have all the elements we need to add constrained choices akin to those in *Depression Quest.* Here’s an example of a branching choice suitable for this recipe, using some of the stats we’ve set so far.

```
You dig deeper, quietly asking around and observing their behavior. They’re hiding something, but is it malice or desperation?

(set: $curiosity to $curiosity + 1)
(set: $persistence to $persistence - 1)

Do you…

(if: $persistence > 11)[[[Confront them directly->Confront]]]
(if: $curiosity > 13)[[[Keep observing for more evidence->Observe]]]

[[Walk away, unsure of what to believe->WalkAway]]
```

Notice how this builds from the model of *Depression Quest* by including a final choice that has no stat requirements — this way, if the reader can reach this decision point from many directions, there’s always a path forward.

## **Works Cited**

Arnott, Leon. “Harlowe 3.3.8 Manual.” *Harlowe Twine 2*, 1 Jan. 2024, twine2.neocities.org (https://twine2.neocities.org/).

Quinn, Zoe, et al. “Depression Quest: An Interactive (Non)Fiction About Living With Depression.” *Depression Quest*, 2013, depressionquest.com (http://www.depressionquest.com/dqfinal.html).

## **Resources**

* The Harlowe manual by Leon Arnott: twine2.neocities.org (https://twine2.neocities.org/).

* The interactive fiction *Depression Quest*: depressionquest.com (http://www.depressionquest.com/dqfinal.html).

* Twine official website for downloads and documentation: twinery.org (https://twinery.org/).

* Sample code for this project from my class: https://github.com/AMSUCF/Interactive-Digital-Narratives/blob/main/GamingTwine.html (https://github.com/AMSUCF/Interactive-Digital-Narratives/blob/main/GamingTwine.html)

