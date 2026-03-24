---
title: The Arabian Labyrinth Technique
chef: Ryan Veeder
abstract: Create expansive text adventure locations using coordinate-based virtual space in Inform 7.
description: >
  Please write 250 words or less for Description
genres:
  - Hypertext
difficulty_pans: 4
yields: >
  Please write 50 words or less for yield.
github_link: (https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/arabian-labyrinth.md)
---

# The Arabian Labyrinth Technique \- a recipe for expansive locations in Inform 7

# **Ryan Veeder**

**Class of E-lit:** Text Adventure  
**Dish:** “The Arabian Labyrinth”  
**Required ingredients:** One Inform 7 compiler, one good reason (optional) to inflict this on your players   
**Preparation and cooking time:** 15 minutes 

**Number of servings and serving size:** 1 textual environment, functionally infinite in extent

**Rating: 🍳🍳🍳🍳 (four pans, extremely difficult) (unless you can copy and paste the example code)**

# **Background \- Creating Worlds with Inform 7**

*"O king of time and substance and cipher of the century\! In Babylonia didst thou attempt to make me lose my way in a labyrinth of brass, with many stairways, doors, and walls…"*  
— "The Two Kings and the Two Labyrinths"  
Okay, so, you might not believe me, but the text below is bona fide, well-formed code. It compiles and everything:

`Chuck's Pet Shop is a room.`  
`The puppy is an animal in Chuck's Pet Shop.`  
`The cash register is a closed openable container in Chuck's Pet Shop.`  
`The pile of money is in the cash register.`  
`The player carries a canvas sack. The canvas sack is a container.`

The language being used is Inform 7 (https://ganelson.github.io/inform-website/),  which was developed specifically for creating parser-based interactive fiction. Its syntax looks like natural English, which is a lot of fun, but please understand: Only a small subset of English sentences can be compiled as code by Inform. In much the way the player of text adventures must learn the weird pseudo-English syntax of the text parser (for the uninitiated, this postcard (https://pr-if.org/doc/play-if-card/play-if-card.html) covers the basics), the author using Inform 7 must learn its weird pseudo-English manner of describing virtual worlds.

Once you get a grip on that pseudo-English, though, the act of crafting these worlds is straightforward, satisfying, and extremely readable. Those six sentences above already constitute a playable game\! They will compile into a story where the player can type in commands like \>OPEN CASH REGISTER, \>TAKE MONEY, and \>PUT MONEY IN SACK. The parser and world model will change the dispositions of all these virtual objects in just the ways we expect. Plus, there are default responses to \>JUMP, \>LISTEN, \>TOUCH MONEY, and so on that will add to the illusion of an actual conversation-cum-narrative.

But that’s about the extent of the playability, so far. We probably want to embellish the story with descriptions (which display when the player tries to \>LOOK AT something) and storytelling logic and so on:

`The description of the puppy is “This dumb mutt is only getting in the way.”`

`Before going outside from Chuck’s Pet Shop:`  
	`if player does not enclose the pile of money:`  
		`say “Aren’t you forgetting something?” instead;`  
	`else if player does not carry the puppy:`  
		`say “You can’t afford to leave this puppy behind! She’s a witness!” instead.`

`After opening the cash register the first time, say “The till slides open. But what was that noise? A silent alarm?”`

Text in quotation marks  will be “said” or displayed to the player under the appropriate circumstances. It isn’t code. The “description” of an object, for example, is displayed when the player types something like \>LOOK AT OBJECT.

But this “`After opening the cash register the first time, say…”` stuff is code. It’s an instruction to the game along these lines: “After the player succeeds in opening the cash register, if it’s the first time the player has done this, display the following text.” (Of course, the compiler wouldn’t understand you if you put it in those terms.)

“`Before going outside from Chuck’s Pet Shop:`” is similarly an instruction about how to handle the player’s actions. It’s Inform 7’s way of saying, “When the player attempts the *going* action, and the direction the player is attempting to move is *outside*, and the location the player is in at the time is *Chuck’s Pet Shop,* follow this logic first—and if the applicable branch of that logic ends with the word ‘instead,’ don’t bother trying to resolve the action that triggered this rule.” “If” and “else” blocks are delineated by indentation.

The Inform 7 developers provide apps for MacOS, Windows, and Linux (https://github.com/ganelson/inform/releases/tag/v10.1.2) which can output text adventure games in “.zblorb” or “.gblorb” format (which players can open in an interpreter like Gargoyle (https://ccxvii.net/gargoyle/)) or as a webpage the author can upload somewhere. The web apps Playfic (https://playfic.com/) and Borogove (https://borogove.app/) will compile Inform 7 code and publish it online for you. (Here (https://playfic.com/games/Afterward/chucks-pet-shop) is a Playfic edition of the pet shop robbery tale described above.) I have heard that some authors are able to compile Inform 7 from the command line.

# **More Background \- Describing Space**

I love writing in Inform because, as excited as I am about telling stories with characters and events, I’m just as excited about creating worlds for players to explore. When I first played Infocom’s *The Lurking Horror*, I had little chance of solving any of its puzzles or advancing the plot, but I did get to feel like I was sneaking around in the bowels of GUE Tech. Doug Egan’s *Afflicted* was a joy to play because I really felt like I was inspecting the world’s most disgusting restaurant.

Many of my own games prioritize conveying the feeling of being in a place/situation: what it’s like to get caught in an Iowa blizzard (“Winter Storm Draco”) or explore the university hospital after hours (“The Ascent of the Gothic Tower”) or wander around a state park (“Ryan Veeder’s Authentic Fly Fishing”). Typically these stories also have plots, but that’s just a convention of the format.

A parser game typically represents its setting as a graph of location nodes. The moving-between-rooms part of gameplay typically looks something like this:

### **Garage**  
You are in the garage. The only exit is north.

\>GO NORTH

### **Hallway**  
Now you are in the hallway. Exits are south and down.

\>GO DOWN

### **Basement**  
Now you are in the basement. Et cetera.

Inform 7 has extremely simple syntax for creating this sort of space:

`The garage is a room. The hallway is north from the garage. The basement is down from the hallway.`  
This format works very well for representing rooms in a house, chambers in a cave (the archetypal parser game venue), streets in a city, even a dirt path across a field. But it's not as useful for putting the player in an “expanse,” a field with no paths, where players can wander in any direction. You can define a big grid of rooms, all connected to each other in every direction—but do you want to bother with room-connecting code like “`FieldG3 is south from FieldG2 and southeast from FieldF2 and east from FieldG2...”` for 30 or 300 rooms? Me neither.

## Recipe

**1\.** In the very short Jorge Luis Borges story “The Two Kings and the Two Labyrinths,” the king of Babylonia humiliates the king of Arabia by forcing him to wander a convoluted labyrinth that resembles the “maze of twisty passages, all alike” of classic text adventures. The king of Arabia gets his revenge by abducting the king of Babylonia so he can show him his own labyrinth, “which has no stairways to climb, nor walls to impede thy passage.” So saying, he abandons the king of Babylonia in the middle of the desert.

So I call the following method the “Arabian labyrinth technique.” We'll make it look like a player is traveling across an expanse while actually staying within a single Inform 7 location.

The simplest way to create such an effect goes like this.

`Desert is a room. “You are hopelessly lost.”`

`Check going while player is in Desert:`  
	`say “You trudge toward [the noun].”;`  
	`try looking instead.`

Inform treats the “NORTH” in “\>GO NORTH” as the object of—“the noun” of—a transitive “going” action. When we refer to the noun variable in brackets, the game substitutes the appropriate value and prints e.g. “You trudge toward the north.” Then we “try looking” to make the game print a description of the current location, as it does whenever the player “really” moves. Gameplay ends up looking like this:

### **Desert**  
You are hopelessly lost.

\>GO NORTHEAST

You trudge toward the northeast.

### **Desert**  
You are hopelessly lost.

As far as Inform’s world model is concerned, the going action fails, and the player remains in the Desert location; we simply tell the player that they are moving around and hope they believe us—after all, this is roughly the same way any text adventure creates the illusion of “real” movement\! For many purposes, that’s all you need.

### **2\.** But we can do better:

`Longitude is initially 0.`  
`Latitude is initially 0.`

We’ll use these coordinate variables to store the player’s position within the desert. This sort of location is not a “room” in the sense Inform 7 understands; this is a layer of abstraction on top of the default world model, a doubly virtual representation of space.

Tracking movement with these coordinates is simple (after we look up the difference between latitude and longitude for the umpteenth time):

`Check going while player is in Desert (this is the desert movement rule):`  
	`if the noun is a direction listed in the Table of Direction Values:`  
		`choose row with direction of the noun in Table of Direction Values;`  
		`now longitude is longitude plus delta-long entry;`  
		`now latitude is latitude plus delta-lat entry;`  
		`say “You trudge toward [the noun].”;`  
		`try looking instead.`

`Table of Direction Values`  
`direction    delta-long    delta-lat`  
`north        0             1`  
`northeast    1             1`  
`east         1             0`  
`southeast    1             -1`  
`south        0             -1`  
`southwest    -1            -1`  
`west         -1            0`  
`northwest    -1            1`

In my games I've used this technique to create impressions of wandering through Iowan woodland (“Ryan Veeder’s Authentic Fly Fishing”), across a windblown desert (“Letavermilia”), through a Florida swamp (“Crocodracula: What Happened to Calvin”), and over the surface of the moon (“The Little Match Girl 2: Annus Evertens”)—settings where I can create navigation puzzles of a different flavor from the mazes of oldschool IF.

Players of these games often surmise that these expanses are functionally infinite, but in fact I’ve always implemented borders to prevent you from getting absolutely helplessly lost. The borders can be visible:

`Before going while player is in Desert:`  
	`if (the noun is northwest or the noun is north or the noun is northeast) and latitude is 5:`  
		`say “The sandstorms become too thick to navigate in that direction.” instead.`

…or invisible:

`Before going while player is in Desert:`  
	`if the noun is east and longitude is 5:`  
		`say “You trudge toward [the noun].”;`  
		`try looking instead.`

In the above example, the player gets the same feedback they’d get by moving “normally,” but latitude and longitude remain the same, so they remain in the same second-order “location,” which is already an illusory notion masking the fact that we’ve never left the first-order Inform 7 “room.” How many levels of abstraction is that?

### **3\.** The illusion is spoiled somewhat if the player drops an inventory item (classic maze navigation technique), takes a virtual step to the northeast, and sees the dropped item is still there. For my purposes, I’ve always been able to get away with a solution along these lines:

`Before dropping something while player is in Desert:`  
	`say “(Insert here some excuse about littering.)” instead.`

By the same token, the illusion becomes more convincing when scenery seems to stay in place while the player “moves around.” We’ll need a bunch of rules for moving that scenery on and off the stage, so we may as well introduce a rulebook:

`Desert scenery rules is a rulebook.`

`A desert scenery rule (this is the bleached skull appearance rule):`  
	`if longitude is 1 and latitude is 1:`  
		`now the bleached skull is in the location;`  
	`else:`  
		`remove the bleached skull from play.`  
		  
`The bleached skull is a fixed in place thing.`  
`A desert scenery rule (this is the sandstorms appearance rule):`  
	`if latitude is 5:`  
		`now the sandstorms are in the location;`  
	`else:`  
		`remove the sandstorms from play.`

`Some sandstorms are a fixed in place thing.`

Then we insert “follow desert scenery rules;” right before “try looking instead” in the desert movement rule. Now, whenever we’re at coordinates (1,1), the skull is right next to us; otherwise, it’s not. (We might apply a similar method to make dropped inventory items “stay” at the coordinates where they’re dropped, if we were feeling less lazy than usual.) If we’re at latitude 50, we can see the sandstorms that impede further progress. With the right sort of faux-randomness, we can make skulls show up on 10% of tiles, or scatter rocks and sand dunes at whatever frequency suits our fancy.

### **4\.** The same method allows us to hide much more important things in our expanse:

`A desert scenery rule (this is the oasis appearance rule):`  
	`if latitude is -4 and longitude is 3:`  
		`now the oasis is in the location;`  
	`else:`  
		`remove the oasis from play.`  
		  
`The oasis is a fixed in place thing.`

How is the player supposed to find such a thing in a seemingly (or “literally”) infinite expanse? We might supply them with a treasure map:

`The player carries the scrap of paper. The description of the scrap of paper is “The numbers (-4, 3) are still barely legible.”`

…or a high-tech navigation device:

`The player carries the GPS. The description of the GPS is “This thing says your current coordinates are ([latitude],[longitude]).”`

…or some sort of oasis-seeking directional radar, which won’t fit in the word count they’re allotting me. 

Here (https://playfic.com/games/Afterward/arabian-labyrinth) is a Playfic project demonstrating all those techniques. But we don’t have to give the player any of these things\! If we like, we can let them wander hopelessly until they die.

