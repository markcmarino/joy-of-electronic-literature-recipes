---
title: Poemscape
chef: Christine Wilks
abstract: Create interactive animated poetry that dynamically responds to mouse movement and involves considering the relationships between text, color, spatial orientation and animation.
description: >
  A starter recipe for a poemscape - a multimodal interactive poem scene that plays in a web browser. The scene takes up the whole screen/viewport, which becomes a dynamic space for the reader/player to explore with their mouse. By stirring up words, colour and animation, the player experiences the particular significance of spatial orientation within the scene. The poemscape mobilizes conceptual metaphors, mapping a concept from a source domain (up, down in this instance) to a target domain. In the given sample code, the target domain is emotion: up maps to positive and down maps to negative emotional states, creating a moodscape. But you can easily adapt this recipe by changing the words to target different domains, to create other kinds of poemscapes. If you are, or as you become, more confident cooking with code, you can create many more variations of this dish by changing other variables, such as those affecting color, animation or orientation. A key feature of this recipe is that it uses a JavaScript event listener to monitor mouse movements, which in turn drive dynamic changes in the poemscape's text and visual features, therefore it teaches the techniques and creative potential of mapping from one domain to another both literally in code and conceptually.
genres:
  - Generative Poetry
difficulty_pans: 2
yields: >
  A working browser-based generative poem scene (or poemscape) that dynamically reacts to mouse movement and incorporates text, color, spatial orientation and animation. Readers gain a reusable code template for building their own generative poemscapes from customizable word arrays and other variables. No framework or server required.
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/poemscape.md
---

# **Poemscape: an interactive mix of color, space, text and motion**

by Christine Wilks, PhD

**Class of E-lit:** E-Poetry: animated interactive generative poem

**Dish:** a delicious mix of words, color, motion, spatial orientation and interactivity.

**Code language:** HTML (Hypertext Markup Language), CSS (Cascading Style Sheets)  and JavaScript.

**Required ingredients:** Computer, code editor, web browser (to see your code run and inspect it while it's running).

**Preparation and cooking time:** 20 minutes.

**Number of servings and serving size:** 1 interactive poemscape

**Rating:** 🍳🍳 two pans, medium

Landscape, cityscape, seascape, cloudscape, moonscape, soundscape, bodyscape... It's surprising how many things can be conceived as a type of '-scape' \- dreamscape, moodscape, wordscape, memescape, mediascape, pixelscape...

This is a recipe for a poemscape. The screen becomes a dynamic space for the reader/player to explore, discovering words, colour, animation and the significance of spatial orientation. In this instance, the poemscape is also a moodscape. It employs conceptual metaphors, which is "*understanding one domain of experience (that is typically abstract) in terms of another (that is typically concrete)*" (Kövecses, 2017). You can think of it as mapping a concept from a source domain to a target domain; for example, "a cold personality", "exploding with anger", "a beacon of hope".

**Sample before you cook:**
	Here's one I made earlier: [Poemscape - Joy of E-lit](https://codepen.io/crissxross/full/QwNbJbM)

# **Recipe: Poemscape**

The key ingredient of this recipe is interactivity \- think of it as the stirrer, mixing the other ingredients. The code adds an event listener that monitors pointer/mouse movements along the horizontal and vertical (*x* and *y*) axes of the screen or viewport. These movement events control the displayed text, the colors, and the animation, cooking up multimodal expressivity.

Depending on the textual content, movement on the vertical axis could convey spatial orientational metaphors, for example, "HAPPY IS UP; SAD IS DOWN", "CONSCIOUS IS UP; UNCONSCIOUS IS DOWN", "HIGH STATUS IS UP; LOW STATUS IS DOWN" (Lakoff and Johnson, 1980). Some claim that color affects us emotionally and while there is no predictable association between hue and specific emotional states, there is evidence that brighter, more saturated colors are more pleasurable than darker, desaturated colors (Valdez and Mehrabian, 1994). Artists have intuitively known this and it's colloquially supported by common phrases such as "bright and cheerful" or "dark and dreary". This recipe offers the opportunity to play with these associations and conceptual metaphors \- or, perhaps, challenge them \- to create a dynamic value-laden or affect-laden poemscape.

## **From the Chef**

I love language play, but non-verbal metaphors can have "a more sensual and emotive impact on viewers" (Forceville,  2008) than verbal ones. That's exciting because in elit, we can work with many modalities. I like to use color, shape, animation and interactivity in combination with text for poetic or narrative expressivity, especially when creating an affective environment or to enhance fictional characterization. Employing such multimodal techniques allows me to communicate more directly, often bypassing the need for descriptive words or passages. I find this particularly important when creating an interactive digital narrative. Eschewing two dimensional or three dimensional graphic realism, I often prefer to depict characters using visual abstraction. For example, in [Voices](https://writing-new-bodies.web.app), my interactive narrative about body image issues, I occasionally used an animated abstract shape to evoke the main character's feelings. Finding an apt conceptual metaphor is a great way to express a character's emotional or sensory state through a non-verbal mode, without resorting to mimesis. It's also a fun way to create e-poems.

## **Directions**

The basic recipe involves two contrasting arrays of words (or phrases) \- for example, an array of words with positive associations and another array with negative associations. The piece displays one animated word at a time and that word changes depending on the position of the pointer/mouse. Moving the pointer in the upper half of the viewport displays a word from the "positive" array and in the lower, from the "negative" array. Horizontal movement changes the index of the word array, thereby also changing the word displayed. Similarly, the background color and the color of the words change depending on the pointer position, as does the style of motion. The displayed word animates smoothly when positive, and jerkily when negative. The further up the pointer moves, the more saturated and lighter the colors become; the further down the pointer goes, the more desaturated and darker the colors become.

1. Choose a subject area or theme that lends itself to being expressed in polar opposites or as two distinct categories (e.g. the sample recipe uses positive and negative emotional states).
2. Create two lists of words, one for each polar opposite or category. The words could be nouns or words that express a state. It may be easier to start with single words, but you could use short phrases. Whichever, the two lists should be of equal length.
3. Replace the words in the program's arrays with your own words. Note: be careful to keep all the punctuation intact, each word in the array should be surrounded by straight quotation marks and separated by commas.
4. If the concept of negative vs. positive doesn't suit your theme, feel free to rename the variables in your code accordingly. For example, if your theme is temperature, you could rename your arrays of words to `wordsHot` and `wordsCold`, and your animations to `hotAnimation` and `coldAnimation`. (I find it helpful for code to be as self-explanatory as possible.)
5. Save the file as a .html file and open it in your browser.

## **Starter code**

Note: a line of text in the code preceded by // is an explanatory 'comment' for you, the human reader, the browser ignores these lines.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Poemscape</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      font-size: 15vw;
      display: grid;
      place-items: center;
      height: 100vh;
      margin: 0;
      overflow: hidden;
      user-select: none;
    }
  </style>
</head>
<body>
  <div class="word">?</div>

  <script>
    // Note: for simplicity, I'm using let throughout to define variables
    let body = document.querySelector("body");
    let word = document.querySelector(".word");

    // Arrays of words to use in the word div element, replace these
    let wordsPos = ["joy", "happy", "relaxed", "comfortable", "peaceful", "satisfied", "content", "calm", "serene", "tranquil", "quiet", "still"];
    let wordsNeg = ["sad", "angry", "anxious", "nervous", "tense", "worried", "stressed", "upset", "frustrated", "irritated", "annoyed", "agitated"];

    // For better performance, calculate the length of the arrays and the width & height of the viewport/window once, rather than on every update (see document.addEventListener below)
    let wordsPosLength = wordsPos.length;
    let wordsNegLength = wordsNeg.length;
    let width = window.innerWidth;
    let height = window.innerHeight;
    let percentX;
    let percentY;
    let hue;
    let saturation;
    let lightness;

    // Define the animations
    let posAnimation = word.animate(
      [{ transform: "translate(-40px, -40px)" }],
      {
        duration: 2000,
        easing: "ease-in-out",
        iterations: Infinity,
        direction: "alternate",
      }
    );
    let negAnimation = word.animate(
      [{ transform: "translate(30px, 15px)" }],
      {
        duration: 400,
        easing: "cubic-bezier(.3, -0.9, .5, 1.6)",
        iterations: Infinity,
        direction: "alternate",
      }
    );

    // Pause the animations initially, nothing should happen until the user's pointer moves
    posAnimation.pause();
    negAnimation.pause();

    // Instruct the browser to listen for & track pointermove events. This makes everything happen because it calls the update functions (i.e. tells those functions to run their code)
    document.addEventListener("pointermove", function (event) {
      // The X and Y coordinates of the pointer as a percentage of the viewport width and height.
      percentX = event.clientX / width;
      percentY = event.clientY / height;
      // Call the update functions every time the pointer moves
      updateWord();
      updateColor();
      updateAnimation();
    });

    // Define the function that changes the words
    function updateWord() {
      // Assign an index for the arrays of words based on pointer's horizontal position - round to whole numbers with Math.floor
      let negIndex = Math.floor(percentX * wordsNegLength);
      let posIndex = Math.floor(percentX * wordsPosLength);
      // Set the text content of the word div element based on the pointer being in the upper or lower half of the viewport
      // If percentY is less than 50%, the pointer is in the upper half of viewport
      if (percentY < 0.5) {
        word.textContent = wordsPos[posIndex];
        word.style.color = `hsl(${hue-120} 100 40)`;
      } else {
        word.textContent = wordsNeg[negIndex];
        word.style.color = `hsl(${hue+120} ${saturation} 40)`;
      }
    }

    // Define the function that changes the color
    function updateColor() {
      // hue based on horizontal pointer position, the x-axis
      hue = percentX * 360;
      // saturation and lightness based on vertical pointer position, the y-axis
      // Subtracting from 100 inverts the percentage
      saturation = 100 - percentY * 100;
      lightness = 100 - percentY * 100;
      // Change the background color of the body element
      body.style.backgroundColor = `hsl(${hue} ${saturation} ${lightness})`;
    }

    // Define the function that changes which animation plays
    function updateAnimation() {
      // Change the animation based on the pointer being in the upper or lower half of the viewport
      if (percentY < 0.5) {
        negAnimation.cancel();
        posAnimation.play();
      } else {
        posAnimation.cancel();
        negAnimation.play();
      }
    }
  </script>

</body>
</html>


```

## **Notes**

* **Color:** there are a number of ways to specify color in CSS and JavaScript. This recipe uses the HSL color model \- which stands for hue, saturation and lightness \- because it's a nice model to work with dynamically. For example, `hsl(120 50 50)` is a shade of green. The code above creates separate variables for hue, saturation and lightness so that they can react to pointer/mouse movements independently. So the x-axis alters the hue, while y-axis alters the saturation and lightness.
* **Hue, Saturation, Lightness:** hue is expressed as an angle from 0 to 360 degrees around the color wheel; saturation and lightness are defined as percentages. For more information, see [hsl() - CSS \| MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/hsl).
* **Animation:** there are also a number of ways to code animation; for example, you can define simple animations in CSS. However, this recipe uses Web Animations, where you define and run the animations in the JavaScript code. This means you can control animation playback from your code. For more information, see [Using the Web Animations API  - Web APIs \| MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)
* **Easing:** animation *easing* affects how the motion accelerates and decelerates, making the movement seem more natural (or not). If you want to try other animation easings, here's a good online tool where you can try them out: [Easing Wizard - CSS Easing Editor and Generator](https://easingwizard.com). You can then copy and paste the easing equations into your code.
* **x, y coordinate system:** starts with 0,0 at top left of the viewport \- so if you want something to move down on the vertical axis you must increase the *y* value and decrease *y* if you want it to move up.

## **Variations**

* Substitute the words in the arrays for phrases.
* Each array could make up a sentence that's displayed one word at a time.
* A more advanced variation could involve more word arrays and incorporate aspects of the [Literary Dish Generator](literary-dish-generator.md) recipe.
* Experiment with the HSL color values (hue, saturation & lightness).
* Experiment with the animation timing and easing and/or animate other properties, such as rotation, scale, and/or opacity.
* Change the affective orientation of the piece by altering the effects of the pointer event listener.
* Experiment with the polar oppositions and/or continuums within the recipe \- e.g. the words in the array(s) could express positions along a continuum and the color changes could be more polarized.
* As the code stands, the recipe works best in landscape orientation. How would you optimize it for portrait orientation, what would you change or adapt?

## **Related Recipes**

- [Literary Dish Generator](literary-dish-generator.md)

## **Resources**

* Here's the Poemscape starter code in my Github repository: https://github.com/crissxross/cx-lab/blob/main/joel/poemscape-joel.html
* Or if you have a free CodePen account (see https://codepen.io/about), you could make a copy of the code (fork it) from my CodePen version here: https://codepen.io/crissxross/pen/QwNbJbM
* For documentation about anything to do with HTML, CSS or JavaScript, MDN (Mozilla Developer Network) is a good open-source resource: https://developer.mozilla.org/en-US/

## **References**

Forceville, Charles. *"Metaphor in Pictures and Multimodal Representations". Cambridge Handbook of Metaphor and Thought*, editor: Raymond Gibbs Jr, Cambridge University Press, 2008, pp. 462-482.

Kövecses, Zoltán.*“Conceptual metaphor theory”*. *Routledge Handbook of Metaphor*, editors: Elena Semino and Zsófia Demjén, Routledge, 2017\.

Lakoff, George and Johnson, Mark. *Metaphors We Live By*. Chicago: University of Chicago Press, 1980\.

Valdez, Patricia and Mehrabian, Albert. *“Effects of color on emotions”.* *Journal of experimental psychology: General*, 123(4), 1994, pp. 394-409.

Wilks, Christine. “Voices”, *crissxross.net,* 2024, https://writing-new-bodies.web.app/

