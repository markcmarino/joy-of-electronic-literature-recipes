---
title: Poemscape
chef: Christine Wilks
abstract: Create interactive animated poetry that responds to mouse movement through color, space, text, and motion.
description: >
  Landscape, cityscape, seascape, cloudscape, moonscape, soundscape, bodyscape—it's surprising how many things can be conceived as a type of '-scape.' This recipe creates a poemscape where the screen becomes a dynamic space for readers to explore, discovering words, color, animation, and the significance of spatial orientation. The poemscape is also a moodscape employing conceptual metaphors—understanding one domain of experience (typically abstract) in terms of another (typically concrete). Think "a cold personality," "exploding with anger," "a beacon of hope." The key ingredient is interactivity, functioning as the stirrer mixing other ingredients. Code adds an event listener monitoring pointer/mouse movements along horizontal and vertical axes, controlling displayed text, colors, and animation to create multimodal expressivity. Vertical movement can convey spatial orientational metaphors like "HAPPY IS UP; SAD IS DOWN" or "CONSCIOUS IS UP; UNCONSCIOUS IS DOWN." While color's emotional effects aren't predictable, brighter saturated colors tend to be more pleasurable than darker desaturated ones—colloquially supported by phrases like "bright and cheerful" or "dark and dreary." This recipe plays with these associations to create a dynamic value-laden or affect-laden poemscape.
genres:
  - Generative Poetry
difficulty_pans: 2
yields: >
  An interactive poemscape where one animated word displays at a time, changing based on pointer position, with color and motion responding to user movement.
github_link: https://codepen.io/crissxross/full/QwNbJbM
---

## Ingredients

- Computer
- Code editor (Visual Studio Code, Atom, etc.)
- Web browser (to see code run and inspect it while running)
- Two contrasting arrays of words or phrases (e.g., positive/negative, hot/cold, light/heavy)
- Understanding of HTML, CSS, and JavaScript (basic level)

## Method

### Conceptual Foundation

**Spatial Orientational Metaphors:**
- "HAPPY IS UP; SAD IS DOWN"
- "CONSCIOUS IS UP; UNCONSCIOUS IS DOWN"
- "HIGH STATUS IS UP; LOW STATUS IS DOWN" (Lakoff and Johnson, 15-16)

**Color and Emotion:**
While no predictable association exists between hue and specific emotional states, brighter, more saturated colors are generally more pleasurable than darker, desaturated colors (Valdez and Mehrabian, 405).

### How the Poemscape Works

The basic recipe involves:
1. Two contrasting arrays of words/phrases (positive and negative associations)
2. One animated word displays at a time, changing based on pointer/mouse position
3. Upper half of viewport: displays words from "positive" array
4. Lower half of viewport: displays words from "negative" array
5. Horizontal movement: changes word array index (changing displayed word)
6. Background color and word color: change based on pointer position
7. Animation style: smooth motion when positive, jerky when negative
8. Further up pointer moves: more saturated and lighter colors
9. Further down pointer moves: more desaturated and darker colors

### Directions

**Step 1: Choose Your Subject**

Select a theme that lends itself to polar opposites (e.g., positive/negative emotional states, hot/cold, loud/quiet).

**Step 2: Create Two Word Lists**

Create two lists of equal length, one for each polar opposite. Start with single words, but short phrases work too.

**Step 3: Replace Words in Arrays**

Replace the words in the program's arrays with your words. Be careful to keep all punctuation intact—each word should be surrounded by straight quotation marks and separated by commas.

**Step 4: Rename Variables (Optional)**

If negative/positive doesn't suit your theme, rename variables accordingly:
- Temperature theme: `wordsHot` and `wordsCold`, `hotAnimation` and `coldAnimation`
- Makes code more self-explanatory

**Step 5: Save and Test**

Save the file as `.html` and open it in your browser.

### Starter Code

**Note:** Lines preceded by `//` are comments for you (the human reader); the browser ignores these lines.

You can copy the starter code from Christine Wilks' GitHub repository:
https://github.com/crissxross/cx-lab/blob/main/joel/poemscape-joel.html

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

    // For better performance, calculate array length and viewport dimensions once
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

    // Pause animations initially - nothing happens until user's pointer moves
    posAnimation.pause();
    negAnimation.pause();

    // Listen for & track pointermove events
    document.addEventListener("pointermove", function (event) {
      // X and Y coordinates of pointer as percentage of viewport dimensions
      percentX = event.clientX / width;
      percentY = event.clientY / height;
      // Call update functions every time pointer moves
      updateWord();
      updateColor();
      updateAnimation();
    });

    // Define function that changes the words
    function updateWord() {
      // Assign index for word arrays based on pointer's horizontal position
      let negIndex = Math.floor(percentX * wordsNegLength);
      let posIndex = Math.floor(percentX * wordsPosLength);
      // Set text content based on pointer being in upper or lower half
      if (percentY < 0.5) {
        word.textContent = wordsPos[posIndex];
        word.style.color = `hsl(${hue-120} 100 40)`;
      } else {
        word.textContent = wordsNeg[negIndex];
        word.style.color = `hsl(${hue+120} ${saturation} 40)`;
      }
    }

    // Define function that changes the color
    function updateColor() {
      // Hue based on horizontal pointer position (x-axis)
      hue = percentX * 360;
      // Saturation and lightness based on vertical position (y-axis)
      // Subtracting from 100 inverts the percentage
      saturation = 100 - percentY * 100;
      lightness = 100 - percentY * 100;
      // Change background color of body element
      body.style.backgroundColor = `hsl(${hue} ${saturation} ${lightness})`;
    }

    // Define function that changes which animation plays
    function updateAnimation() {
      // Change animation based on pointer in upper or lower half
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

## Notes

### Color: HSL Model

The recipe uses the HSL (Hue, Saturation, Lightness) color model because it's nice to work with dynamically.

- **Hue:** Expressed as angle from 0 to 360 degrees around color wheel
- **Saturation & Lightness:** Defined as percentages
- Example: `HSL(120 50 50)` is a shade of green
- Code creates separate variables for each component to react independently to pointer movements
- X-axis alters hue; Y-axis alters saturation and lightness

For more information: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/hsl

### Animation: Web Animations API

This recipe uses Web Animations, defining and running animations in JavaScript code for better control over animation playback.

For more information: https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API

### Easing

Animation easing affects how motion accelerates and decelerates, making movement seem more natural (or intentionally unnatural).

Try other easings with this tool: https://easingwizard.com
Copy and paste easing equations into your code.

### X, Y Coordinate System

Starts with (0,0) at top left of viewport:
- Increase Y value to move down
- Decrease Y value to move up

## Variations

- Substitute words in arrays for phrases
- Each array could make up a sentence displayed one word at a time
- More advanced: involve more word arrays and incorporate text generator aspects
- Experiment with HSL color values (hue, saturation, lightness)
- Experiment with animation timing and easing
- Animate other properties: rotation, scale, opacity
- Change affective orientation by altering pointer event listener effects
- Experiment with polar oppositions and/or continuums
- Code works best in landscape orientation—how would you optimize for portrait?

## Resources

- Starter code in GitHub: https://github.com/crissxross/cx-lab/blob/main/joel/poemscape-joel.html
- CodePen version (fork it if you have free account): https://codepen.io/crissxross/pen/QwNbJbM
- MDN (Mozilla Developer Network) for HTML, CSS, JavaScript documentation: https://developer.mozilla.org/en-US/

## References

- Forceville, Charles. "Metaphor in Pictures and Multimodal Representations". *Cambridge Handbook of Metaphor and Thought*, editor: Raymond Gibbs Jr, Cambridge University Press, 2008, pp. 462-482.
- Kövecses, Zoltán. "Conceptual metaphor theory". *Routledge Handbook of Metaphor*, editors: Elena Semino and Zsófia Demjén, Routledge, 2017.
- Lakoff, George and Johnson, Mark. *Metaphors We Live By*. Chicago: University of Chicago Press, 1980.
- Valdez, Patricia and Mehrabian, Albert. "Effects of color on emotions". *Journal of experimental psychology: General*, 123(4), 1994, pp. 394-409.
- Wilks, Christine. "Voices", crissxross.net, 2024, https://writing-new-bodies.web.app/

## From the Chef

"I love language play, but I agree that non-verbal metaphors can have 'a more sensual and emotive impact on viewers' (Forceville, 24) than verbal ones. What attracts me to e-lit is that we can wield it all. I like to use color, shape, animation and interactivity in combination with text for poetic or narrative expressivity, especially when creating an affective environment or to enhance fictional characterization."
