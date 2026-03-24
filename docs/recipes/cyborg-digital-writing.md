---
title: A Cyborg Digital Writing Primer
chef: Leonardo Flores
abstract: Learn to create digital writing by hacking existing works or using AI to generate frameworks.
description: >
 Please write 250 words or less summary
genres:
  - Generative Poetry
difficulty_pans: 1
yields: >
  Please write 50 words or less for yield
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/cyborg-digital-writing.md
---

# A Cyborg Digital Writing Primer

## Leonardo Flores Professor and Chair, Department of English Appalachian State University

**Category: Digital Poetry**  
**Class of E-Lit:**  E-Poetry  
**Required ingredients:**  
Web browser and internet connection  
Text editor  
**Preparation and cooking time:** under an  hour  
**Rating: 🍳** one pan, easy

## **Background:**

**Cyborg digital writing** describes how both human authors and their writing have become enmeshed with digital technologies. Here are some related terms to contextualize.

* **Cyborg writing** refers to how our own writing is increasingly shaped by digital writing technologies such as spell and grammar checkers, predictive keyboards and suggested texts, generative AI, and bespoke engines for text generation. Cyborg writing can result in writing designed for the page (printed or virtual) or in digital writing.  
* **Digital writing** refers to *writing* that embraces the potential digital media offers to produce generative, interactive, multimodal, kinetic, hypertextual, textual works that engage digital culture to go beyond the limitations of the page (printed or virtual).  
* **Electronic literature** is *literary* digital writing. As an older term in the field, it includes practices that aren’t strictly digital writing, such as sound and video poetry in which language is not presented in written form.

This primer will show two approaches to produce cyborg digital writing, first by showing how to hack an existing work of digital writing to produce a new one, and then by showing how to use AI to generate code to produce a new framework for digital writing.

## **How to Hack a Digital Work:**

**Direections: t**he first step is to select any standalone work (that is, not using external libraries) using Hypertext Markup Language (HTML), or one of the recommended ones below:

* [Leonardo Flores’ Generative Template](http://iloveepoetry.org/creative/floresgenerativetemplate.html) by Leonardo Flores http://iloveepoetry.org/creative/floresgenerativetemplate.html  
* [Taroko Gorge](https://nickm.com/taroko_gorge/original.html) by Nick Montfort  
  [https://nickm.com/taroko\_gorge/original.html](https://nickm.com/taroko_gorge/original.html)  
* [The Two](https://nickm.com/2/the_two.html) by Nick Montfort  
  [https://nickm.com/2/the\_two.html](https://nickm.com/2/the_two.html)  
* [A House of Dust](https://nickm.com/memslam/a_house_of_dust.html) by Alison Knowles and James Tenney (reimplemented by Nick Montfort)  
  [https://nickm.com/memslam/a\_house\_of\_dust.html](https://nickm.com/memslam/a_house_of_dust.html)  
* Any of the works published in [*Taper*](https://taper.badquar.to/).

  https://taper.badquar.to/

### **Process:**

1. Open the work, linked to above in your browser, and save it as an HTML file in your computer (smartphones and tablets are not recommended for this).  
2. Open the saved file with a code or text editor (I recommend [Visual Studio Code](https://code.visualstudio.com/)):  
   https://code.visualstudio.com/  
3. Open the same saved file in a browser. Whenever you make changes to the original file, save it in the editor, and reload it in the browser to see the changes.  
4. Modify the code as you see fit, being careful not to break it by missing a comma, quotation mark, semicolon, etc. Take small steps in changing datasets.  
5. When you’re satisfied with the text the work is generating, give it a title, modify the aspects of the source code that display your title and name, modify the style sheet as you see fit, and rename the file as something that is yours. I recommend writing an artist’s statement in the source code documentation in which you credit the original work and any AI systems you used to assist in coding.

If the code breaks you have some options for debugging:

* See if the code editor identifies the problem by making the line number red.  
* Open the developer tools in your browser and look for the error messages, which will tell you where the problems are by line and space number.  
* Copy paste your code into the AI system and ask it to fix it. Describe the problem in your prompt.  
* Use undo (Control/Command \+ z) until you get to an earlier version of your document that works.

## **How to use AI to create a digital work:**

AI can significantly reduce the access barrier to creating new frameworks for digital writing, but you do need to know some programming basics and a general familiarity with the conventions of the programming language you will use and debugging tools. For the purposes of this exercise, I will focus on HTML (including CSS and JavaScript).

### **Preparation:**

Before you start prompting, think of what framework for digital writing you would like to create. Here’s an example I will illustrate after describing the process:

A word (or phrase or poetic line) appears in the middle of the screen. When the user touches it, it changes to a different word. This allows you to write a sequence of words that can complete a sentence, tell a story, or deliver a poem.

### **Process:**

1. Create a new document with a code editor (I recommend [Visual Studio Code](https://code.visualstudio.com/) \- https://code.visualstudio.com/) and give it a simple name in lower case, followed by the suffix .html (such as sequence.html).  
2. Open Chat GPT ([https://chat.openai.com/](https://chat.openai.com/)), Claude ([https://claude.ai](https://claude.ai)), Gemini ([https://gemini.google.com](https://gemini.google.com)) or AI system of choice.  
3. Prompt the AI to generate HTML code to produce the results you want, starting with a simple yet descriptive prompt.  
4. Copy-paste the generated code into your document.  
5. Save the document and then open (or reload) in your browser to see the results.  
6. If you don’t like the results or would like to modify them, repeat steps 3-5.  
7. Once you’re happy with the “engine.” Modify the code directly in your editor so that it says what you want it to say. Repeat step 5 after each modification.

If the code breaks you have some options for debugging:

* See if the code editor identifies the problem by making the line number red.  
* Open the developer tools in your browser and look for the error messages, which will tell you where the problems are by line and space number.  
* Copy paste your code into the AI system and ask it to fix it. Describe the problem in your prompt.  
* Use undo (Control/Command \+ z) until you get to an earlier version of your document that works.

If the code becomes too long for the AI to read, focus on the portions you want to modify, such as the script, style (CSS or Cascading Stylesheets), header, etc. Be sure to only copy-paste the sections you wish to modify.

### **Example:**

Prompt: “Generate HTML code to produce a page in which there’s a word centered on the screen. When the user clicks or touches the word, it changes to the next word in a sequence of 10 words. Use lorem ipsum text for the words.”

Here’s the output produced by ChatGPT 4o.

```html
<!DOCTYPE html>
 <html lang=”en”>
 <head>
 <meta charset=”UTF-8″>
 <meta name=”viewport” content=”width=device-width, initial-scale=1.0″>
 <title>Word Sequence</title>
 <style>
 body, html {
 height: 100%;
 margin: 0;
 display: flex;
 justify-content: center;
 align-items: center;
 font-family: Arial, sans-serif;
 background-color: #f0f0f0;
 }
 #word {
 font-size: 2em;
 cursor: pointer;
 }
 </style>
 </head>
 <body>
 <div id=”word”>Lorem</div>
 <script>
 const words = [“Lorem”, “Ipsum”, “Dolor”, “Sit”, “Amet”, “Consectetur”, “Adipiscing”, “Elit”, “Integer”, “Nec”];
 let currentIndex = 0;
document.getElementById(“word”).addEventListener(“click”, () => {
 currentIndex = (currentIndex + 1) % words.length;
 document.getElementById(“word”).textContent = words[currentIndex];
 });
 </script>
 </body>
 </html>
```

Notice that the lorem ipsum text is in the line that begins with the initial word in the “div” and then the sequence in the “const words.” If you modify that text and save it, it will produce the sequence of words or phrases you write. Here’s my modification.

```html
<body\>  
 <div id=”word”\>Cyborg Digital Writing\</div\>  
 <script\>const words \= \[“I”, “love”, “creating”, “new”, “frameworks”, “for”, “digital”, “writing.”, “Don’t”, “you?”\];
```

When you save the work, it works, but with the current configuration, the first click will begin displaying the word “love” instead of “I”.

A simple way to correct it is to prompt the AI with the following: “Make it so the first click goes to the first word in the words sequence in this code: \[copy-paste the complete code\].” And that fixes it\! This is a simple way to use natural language in an AI system to generate functional code. However, be sure to take a moment to read the code and begin to learn how it operates.

And these are the first steps towards increasing your code literacy and creating new frameworks for digital writing using AI systems.

Some final touches:

* Change the title for the piece by modifying the line “\<title\>Word Sequence\</title\>” to whatever title you want to give it (I’m changing it to “Cyborg Digital Writing”).  
* Add some documentation to give credit where credit is due by inserting the following code in a new line after the title tag and modifying it with your details. (Note that I have included a short version of the MIT license \- https://opensource.org/license/mit):

```html
<!– “Cyborg Digital Writing” Copyright (c) 2024 Leonardo Flores
Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.
This is a minimalist digital writing framework created on June 24, 2024 by Leonardo Flores using ChatGPT 4o.
–>
```

* Here’s a link to the work \- https://iloveepoetry.org/creative/sequence.html:  
* Now, play with this simple code and develop it in a variety of ways, such as:  
  * Randomize the sequence of words.  
  * Have the click affect the font size, so the words are larger, smaller, or randomly sized.  
  * Make the word’s color or background color (or both) change with every click.  
  * Make the words appear in a random location on the screen with every click.  
  * Make the user be able to drag the words.  
  * Make the words move in a random direction and fly off screen, or bounce when it hits the edges.  
  * While you’re at it, make the words accumulate so the whole phrase is on screen.  
  * Make the words grow or shrink in size over time and or fade.  
  * Do whatever else you can think of.  
* Final advice: add one feature at a time and work on it iteratively until it functions as desired before adding another feature.

You are ready. Now go have fun creating new digital works\!

