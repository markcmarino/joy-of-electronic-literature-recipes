---
title: Dis/Appearing Recipe
chef: Katy Ilonka Gero
abstract: Create erasure poetry that computationally removes or transforms words to reveal new meanings within existing texts.
description: >
  Please write a 250-word or less description
genres:
  - Generative Poetry
difficulty_pans: 2
yields: >
  Write 50 words or less for recipe yield
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/disappearing-recipe.md
---

# Dis/Appearing Recipe

Katy Ilonka Gero  
Lecturer, School of Computer Science  
University of Sydney

**Class of E-lit: Digital Poetry**  
**Dish:** Erasure Poetry  
**Required ingredients: source text, plain html file**  
**Preparation and cooking time:**  15 minutes

**Number of servings and serving size: endless**

**Rating: 🍳🍳 medium**

## **Background**  
Within each text lurks many more. Erasure poetry is a mode of writing in which you remove certain words from an existing text in order to create a new text with what remains. [Doris Cross’](https://www.poetryfoundation.org/featured-blogger/70334/who-is-doris-cross) ([https://www.poetryfoundation.org/featured-blogger/70334/who-is-doris-cross](https://www.poetryfoundation.org/featured-blogger/70334/who-is-doris-cross)) reworking of dictionary pages into poems is one of the earliest examples I can find of this—I believe she did this work in the 1960s and 70s—but now erasure poetry has a solid footing in literature. Jen Bervin’s book of poems “[Nets](https://poets.org/book/nets)” ([https://poets.org/book/nets](https://poets.org/book/nets))  (Ugly Duckling Press, 2003\) creates new poems out of Shakespeare’s sonnets. (Sonnets → nets, get it?) Another example is Tracy K. Smith’s poem [Declaration](https://www.poetryfoundation.org/poems/147468/declaration-5b5a286052461) (https://www.poetryfoundation.org/poems/147468/declaration-5b5a286052461), which creates a critical and reflective poem out of the American Declaration of Independence.

How you erase the words can create a certain aesthetic. Do you strike words out with a pen, or completely hide the words with a thick, dark marker? Alternatively, you could paint or collage or draw over them, or physically cut them out, turning the page into a more visual piece with the errant words remaining. You could remove words but leave the empty space behind, or retype the text such that it appears as a new poem with little evidence of the words removed.

Computation affords us a new way to create erasure poetry. We can select which words to remove algorithmically, or animate their removal in particular ways. We can even run erasure backwards, letting words reappear over time. 

Something beautiful about removing words slowly is that it lets us experience a single text in many different ways. My first interest in computationally erasing a poem was to help me revise poems. I was able to see serendipitous moments in my own writing, for instance by pausing an erasure at an interesting moment. It can be hard to see a familiar text anew, whether it is your own writing or from someone else, but erasure gives us all new eyes.

## **Sample before you cook:**

The Redactionist by Max Kreminski  
https://mkremins.github.io/blackout/interactive/

Kreminski, Max, et al. "Evaluating Mixed-Initiative Creative Interfaces via Expressive Range Coverage Analysis." *IUI Workshops*. 2022\.

dis/appear by Max Neely-Cohen and Katy Ilonka Gero  
[https://www.katygero.com/dis-appear/](https://www.katygero.com/dis-appear/)

Neate, Timothy, et al. "Empowering expression for users with aphasia through constrained creativity." *Proceedings of the 2019 CHI conference on human factors in computing systems*. 2019\.

The Deletionist by Amaranth Borsuk, Jesper Juul, and Nick Montfort  
[http://thedeletionist.com/](http://thedeletionist.com/)

# Recipe: Disappear a Poem

## Ingredients:

- A source text  
- A plain html file

## Directions:

1. Put your source text into a div, and put a button beneath it that will trigger the poem to start erasing.

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

2. Write some javascript that will wrap every word in the source text with a span and a unique id – this way we can easily select any word we like by its id.

```javascript
   	// wrap every word in a span with a unique id  
    	var text \= document.getElementById('text').innerText;  
    	var lines \= text.split('\\n');  
    	var count \= 0;  
    	var newtext \= '';  
	// iterate over the lines  
    	for(var i \= 0; i \< lines.length ; i++){   
      	var words \= lines\[i\].split(' ');  
	// iterate over words in the line  
      	for(var j=0, sizej \= words.length; j\<sizej; j++){  
        	count++;  
        	newtext \+= ' \<span id="' \+ count \+ '"\>' \+ words\[j\] \+ '\</span\>';  
      	}  
      	newtext \+= '\<br\>';  
    	}  
    	document.getElementById('text').innerHTML \= newtext;
```

4. Write a function that will select a random word and assign it a special class which will make the word fade away.

```javascript
 	function disappearWord(){  
      	var rand \= Math.floor((Math.random() \* count) \+ 1);  
      	var span \= document.getElementById(rand);  
      	span.className \= 'forget';  
      	var word \= span.innerHTML;  
      	console.log(word);  
    	}
```

4. Write some CSS that will make words fade – feel free to play around with this, as you can make words disappear quickly, slowly, change color, etc.

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

5. Now create a timer that will run our disappearWord() function every second. Again, feel free to mess around with this interval depending on the length of your text and how fast you want the words to disappear.

	var forgetter \= setInterval(disappearWord, 1000);

6. Putting it all together, here is a complete html file that will make your poem slowly disappear.

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

# Variation: Black Out a Poem

Instead of having each word fade to zero opacity, we could have the words fade to a blackout, for a more traditional erasure poem look. Replace the @keyframes in the CSS with this:

```css
  	@keyframes bt {  
    	0% {background-color: white;}  
    	100% {background-color: black;}  
  	}
```

# Variation: Appear a Poem

When we wrap each word in a span, let’s add a class such that we can set the words to start at zero opacity and slowly appear. Changes in red below.

```javascript
  	// wrap every word in a span with a unique id  
    	var text \= document.getElementById('text').innerText;  
    	var lines \= text.split('\\n');  
    	var count \= 0;  
    	var newtext \= '';  
	// iterate over the lines  
    	for(var i \= 0; i \< lines.length ; i++){   
      	var words \= lines\[i\].split(' ');  
	// iterate over words in the line  
      	for(var j=0, sizej \= words.length; j\<sizej; j++){  
        	count++;  
        	newtext \+= ' \<span class=”start” id="' \+ count \+ '"\>' \+ words\[j\] \+ '\</span\>';  
      	}  
      	newtext \+= '\<br\>';  
    	}  
    	document.getElementById('text').innerHTML \= newtext;
```

We’ll also have to change the CSS – add the styling for the “start” class and make the animation run backwards. Changes in red below.

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

# Variation: All Words are Bird Words

We can move slightly away from erasure and instead think of our little system as a way to transform texts entirely, instead of just removing parts. In this variation, I write a list of bird words (but you can write your own list of words that makes sense for your project) and change the disappearWord() function such that instead of erasing a selected word from the source text it is replaced with a bird word, ensuring that all texts are eventually about birds.

```javascript
const birdWords = ["hawk", "sparrow", "jay", "eagle", "parrot", "owl", "finch", "fly", "soar",  "glide", "flit", "flutter", "drift", "flap"];

function disappearWord(){
      	var rand = Math.floor((Math.random() * count) + 1);
      	var span = document.getElementById(rand);
      	var birdWord = birdWords[Math.floor((Math.random() * birdWords.length))];
      	var originalWord = span.innerHTML;
      	span.innerHTML = birdWord;
      	console.log(originalWord, birdWord);
    }
```

# More Variations

Consider adding a “pause” or “save” button, so you can savor a particular moment of the poem as it is being changed. You can use the clearInterval() function to turn off the forgetter timer.

Consider what other units of text might be interesting. Maybe you don’t want to focus on words but actually letters, or whole lines or sentences. Instead of wrapping each word in a span, wrap each line, or each letter.

Consider how else we might pick the words to be erased or transformed. Right now, we pick them randomly, but we could focus on parts of speech (erase all the nouns or verbs), other linguistic qualities (starting letter, certain sounds), mathematical functions (words in order, every third word, in a fibonacci sequence), or other selection processes that make sense for your poem. Libraries like RiTa ([https://rednoise.org/rita/](https://rednoise.org/rita/)), compromise ([https://github.com/spencermountain/compromise](https://github.com/spencermountain/compromise)), and winkNLP ([https://github.com/winkjs/wink-nlp](https://github.com/winkjs/wink-nlp)) provide functions for working with language in more sophisticated ways.

Consider how you might give the reader more control over the process. In Max Kreminski’s Redactionist (listed in the samples) they first black out the whole poem and let the user select poems to “unredact”, but limit the options such that all the erasure poems have a certain quality, like those that follow a certain syntactic pattern. What if you did this but only allowed people to unredact the words about water, or the words that contained the letter ‘s’?

