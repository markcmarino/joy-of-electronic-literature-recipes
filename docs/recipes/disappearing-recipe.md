---
title: Dis/Appearing Recipe
chef: Katy Ilonka Gero
abstract: Create erasure poetry that computationally removes or transforms words to reveal new meanings within existing texts.
description: >
  Within each text lurks many more. Erasure poetry removes certain words from existing texts to create new texts with what remains. From Doris Cross's reworked dictionary pages in the 1960s-70s to Jen Bervin's "Nets" (creating poems from Shakespeare's sonnets) and Tracy K. Smith's "Declaration" (derived from the American Declaration of Independence), erasure has a solid footing in literature. How you erase affects aesthetics—striking out with pen, obscuring with marker, painting/collaging over words, physically cutting them out, or simply removing them and retyping. Computation affords new approaches: algorithmic selection of words to remove, animated removal in particular ways, or even running erasure backwards by letting words reappear over time. This recipe creates HTML/JavaScript tools that slowly disappear words, allowing a single text to be experienced in many different ways. The author's interest began with using erasure to help revise poems, pausing at interesting serendipitous moments. It's hard to see familiar texts anew, but erasure gives us new eyes. The recipe includes variations for blackout poetry, appearing poems (reverse erasure), and text transformation (replacing words rather than removing them).
genres:
  - Generative Poetry
difficulty_pans: 2
yields: >
  An HTML page where text slowly erases word by word, creating endless moments of serendipitous poetry along the way.
github_link: https://www.katygero.com/dis-appear/
---

## Ingredients

- A source text (your own poem, or other words you want to play with)
- A plain HTML file
- Text editor
- Web browser

## Method

### Step 1: Set Up Your HTML Structure

Put your source text into a div, with a button beneath to trigger the erasure:

```html
<body>
  <div class='main'>
    <div class='text'>
      Place your source text here.<br>
      It could be your own poem,<br>
      Or some other words you like,<br>
      Or want to play with.
    </div>
    <button onClick="disappear()">disappear</button>
  </div>
</body>
```

### Step 2: Wrap Each Word in a Span

Write JavaScript that wraps every word in the source text with a span and unique id—this allows easy selection of any word by its id:

```javascript
// wrap every word in a span with a unique id
var text = document.getElementById('text').innerText;
var lines = text.split('\n');
var count = 0;
var newtext = '';
// iterate over the lines
for(var i = 0; i < lines.length ; i++){
  var words = lines[i].split(' ');
  // iterate over words in the line
  for(var j=0, sizej = words.length; j<sizej; j++){
    count++;
    newtext += ' <span id="' + count + '">' + words[j] + '</span>';
  }
  newtext += '<br>';
}
document.getElementById('text').innerHTML = newtext;
```

### Step 3: Create Disappearing Function

Write a function that selects a random word and assigns it a special class which makes the word fade away:

```javascript
function disappearWord(){
  var rand = Math.floor((Math.random() * count) + 1);
  var span = document.getElementById(rand);
  span.className = 'forget';
  var word = span.innerHTML;
  console.log(word);
}
```

### Step 4: Write CSS for Fading

Write CSS that makes words fade. Feel free to play around—words can disappear quickly, slowly, change color, etc.:

```css
@keyframes bt {
  0% {opacity: 1;}
  50% {opacity: .5;}
  100% {opacity: 0;}
}
.forget {
  animation: bt 5s infinite;
  animation-iteration-count: 1;
  animation-fill-mode: forwards;
}
```

### Step 5: Create a Timer

Create a timer that runs the `disappearWord()` function every second. Feel free to adjust this interval depending on text length and desired speed:

```javascript
var forgetter = setInterval(disappearWord, 1000);
```

### Step 6: Complete HTML File

Putting it all together, here's a complete HTML file that makes your poem slowly disappear:

```html
<html>
<head>
  <style>
    @keyframes bt {
      0% {opacity: 1;}
      50% {opacity: .5;}
      100% {opacity: 0;}
    }
    .forget {
      animation: bt 5s infinite;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
    }
  </style>
  <script>
    function disappear() {
      // wrap every word in a span with a unique id
      var text = document.getElementById('text').innerText;
      var lines = text.split('\n');
      var count = 0;
      var newtext = '';
      for(var i = 0; i < lines.length ; i++){
        var words = lines[i].split(' ');
        for(var j=0, sizej = words.length; j<sizej; j++){
          count++;
          newtext += ' <span id="' + count + '">' + words[j] + '</span>';
        }
        newtext += '<br>';
      }
      document.getElementById('text').innerHTML = newtext;

      // a function that picks a random word and adds a special class
      // that will make that word disappear
      function disappearWord(){
        var rand = Math.floor((Math.random() * count) + 1);
        var span = document.getElementById(rand);
        span.className = 'forget';
        var word = span.innerHTML;
        console.log(word);
      }

      var forgetter = setInterval(disappearWord, 1000);
    }
  </script>
</head>
<body>
  <div id='main'>
    <div id='text'>
      Place your source text here.<br>
      It could be your own poem,<br>
      Or some other words you like,<br>
      Or want to play with.
    </div>
    <button onClick="disappear()">disappear</button>
  </div>
</body>
</html>
```

## Notes

### Variation: Black Out a Poem

Instead of fading to zero opacity, have words fade to blackout for a more traditional erasure poem look. Replace the `@keyframes` in CSS with:

```css
@keyframes bt {
  0% {background-color: white;}
  100% {background-color: black;}
}
```

### Variation: Appear a Poem

When wrapping each word in a span, add a class so words start at zero opacity and slowly appear:

**JavaScript changes:**
```javascript
newtext += ' <span class="start" id="' + count + '">' + words[j] + '</span>';
```

**CSS changes:**
```css
@keyframes bt {
  0% {opacity: 0;}
  50% {opacity: .5;}
  100% {opacity: 1;}
}
.forget {
  animation: bt 5s infinite;
  animation-iteration-count: 1;
  animation-fill-mode: forwards;
}
.start {
  opacity: 0;
}
```

### Variation: All Words Are Bird Words

Move away from erasure toward transformation. Create a list of words (e.g., bird words) and replace selected words instead of erasing them, ensuring all texts eventually become about your theme:

```javascript
const birdWords = ["hawk", "sparrow", "jay", "eagle", "parrot", "owl", "finch", "fly", "soar", "glide", "flit", "flutter", "drift", "flap"];

function disappearWord(){
  var rand = Math.floor((Math.random() * count) + 1);
  var span = document.getElementById(rand);
  var birdWord = birdWords[Math.floor((Math.random() * birdWords.length))];
  var originalWord = span.innerHTML;
  span.innerHTML = birdWord;
  console.log(originalWord, birdWord);
}
```

### More Variations to Consider

**Add Controls:**
- Consider adding "pause" or "save" buttons to savor particular moments
- Use `clearInterval()` function to turn off the forgetter timer

**Different Text Units:**
- Instead of wrapping each word, wrap each line, sentence, or even each letter
- Creates different erasure effects

**Different Selection Processes:**
- Currently random, but could focus on:
  - Parts of speech (erase all nouns or verbs)
  - Linguistic qualities (starting letter, certain sounds)
  - Mathematical functions (words in order, every third word, Fibonacci sequence)
- Libraries like RiTa (https://rednoise.org/rita/), compromise (https://github.com/spencermountain/compromise), and winkNLP (https://github.com/winkjs/wink-nlp) provide sophisticated language functions

**Reader Control:**
- Give readers more control over the process
- Example: Max Kreminski's "The Redactionist" blacks out the whole poem, lets users select poems to "unredact," but limits options to maintain certain qualities (specific syntactic patterns, words about certain topics, words containing specific letters)

### Sample Works Before You Cook

**The Redactionist** by Max Kreminski
https://mkremins.github.io/blackout/interactive/

Kreminski, Max, et al. "Evaluating Mixed-Initiative Creative Interfaces via Expressive Range Coverage Analysis." *IUI Workshops*, 2022.

**dis/appear** by Max Neely-Cohen and Katy Ilonka Gero
https://www.katygero.com/dis-appear/

Neate, Timothy, et al. "Empowering expression for users with aphasia through constrained creativity." *Proceedings of the 2019 CHI conference on human factors in computing systems*, 2019.

**The Deletionist** by Amaranth Borsuk, Jesper Juul, and Nick Montfort
http://thedeletionist.com/

### Historical Context

**Erasure Poetry Precedents:**
- Doris Cross's reworked dictionary pages (1960s-70s): https://www.poetryfoundation.org/featured-blogger/70334/who-is-doris-cross
- Jen Bervin's "Nets" (Ugly Duckling Press, 2003): Creates poems from Shakespeare's sonnets: https://poets.org/book/nets
- Tracy K. Smith's "Declaration": Critical poem derived from American Declaration of Independence: https://www.poetryfoundation.org/poems/147468/declaration-5b5a286052461

### Something Beautiful

"Something beautiful about removing words slowly is that it lets us experience a single text in many different ways... It can be hard to see a familiar text anew, whether it is your own writing or from someone else, but erasure gives us all new eyes."
