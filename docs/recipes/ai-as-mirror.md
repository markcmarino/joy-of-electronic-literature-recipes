---
title: AI as Mirror — Recipes for Three Digital Selves
chef: Carrie Sijia Wang
abstract: Three recipes for creating AI chatbot versions of yourself using rule-based scripting, Markov chains, and large language models.
description: > 
     I share recipes for creating three different versions of digital selves. Each recipe blends your inner monologues or stream-of-consciousness writings with chatbot algorithms to distort and reflect the human experience. The first recipe, SCRIPTED SELF, uses rule-based keyword matching to archive your thoughts in an interactive way. It tastes predictable and comforting. The second recipe, REMIXED SELF, utilizes Markov chains to reorganize your words and phrases based on probability. This is a good dish to prepare when you feel trapped in your own thoughts, or want to invite a little randomness into your thinking and writing. The third recipe, REFLECTED SELF, is made by instructing an existing large language model to draw from a database of your personalized writings when it responds to you. The resulting flavor exists on a scale: one end is how you perceive yourself, and the other end is how you are interpreted through an opaque collective intelligence. These recipes for fake yous are not meant to replace the real you, nor are they any good in substituting your connections with human friends and genuine experiences. They are digital mimicries of fragments of reality—an experiment to explore what it means to be human in an AI-infused, machine-coded world.
genres:
  - Human-computer collaboration
difficulty_pans: 2
yields: >
  Three versions of digital selves archived, remixed, and reflected through chatbot techniques and prediction algorithms. The dishes are highly individual and can taste completely different depending on who makes them.
github_link: (https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/ai-as-mirror.md?plain=1)
---

# AI as Mirror \- Recipes for Three Versions of Digital Selves

Carrie Sijia Wang  
Adjunct Instructor (Interactive Media Arts)  
New York University

**Class of E-Lit: Chatbots**  

**Dish:** Scripted Self is an interactive way of accessing your inner dialogues. Remixed Self brings unexpected tastes to your familiar thoughts. Reflected Self blends your own perspectives with the faceless crowd behind machine learning algorithms.

**Ingredients and cooking method:**

- **Data:** Your writings in digital format. 

- **AI:** The three recipes use AI, whether retrieval-based or generative, in different experimental ways, as an ingredient that distorts and reflects the human experience.

- **p5.js:** A free, open-source JavaScript library for creative coding. It is used to code a user interface for the chatbot program.

- **RiveScript:** A simple scripting language for chatbots that matches keywords in your input to scripted responses.

- **RiTa:** A free, open-source library for writing in computational environments. It has a set of functionalities to build text-based Markov Chain models.

**Number of servings:** 1 

**Rating: 🍳🍳 medium**

## Introduction

You may have tried out different kinds of chatbots, most of whom are friendly assistant types that feel a little bland, or others that are customized to impersonate celebrities or fictional characters (like the ones on character.ai \- [https://character.ai/](https://character.ai/)). But what about a chatbot that is programmed to be a version of you? 

In this article, I share recipes for creating three versions of your digital self. Each recipe blends your own writings with Artificial Intelligence (AI)—in its various forms—as key ingredients. The dishes are highly individual and can taste completely different depending on who makes them. Everyone may have their own reason for making such a dish. It could be a tool for having reflective conversations, a way to take care of emotional needs, a place to find surprises in the familiar, or a mirror to learn more about how one connects with oneself, others, and the world around you.

**These recipes for fake yous are not meant to replace the real you**, nor are they any good in substituting your connections with human friends and genuine experiences. They are digital mimicries of fragments of reality—an experiment to explore what it means to be human in an AI-infused, machine-coded world.

## Background: A Few More Words About AI

**A Controversial Ingredient**

As a chef cooking digital technologies with a socially-conscious mindset, I approach AI in both critical and explorative ways. Some of my dishes are prepared with the purpose to demystify, critique, and question—revealing AI’s inner workings, the systems of power and control behind its making, and how it reinforces predominant narratives that are problematic to start with. With the three recipes below, AI is used in a more experimental way, as an ingredient that distorts and reflects the human experience. Because of its ability to mimic humans, we could potentially use it as a unique lens through which we can investigate human behavior and social dynamics.

**AI Has Been Around for Decades**

AI is an umbrella term that refers to a broad class of systems that enable machines to mimic human capabilities. It has been around for decades. One of the first chatbots, Eliza, was developed at MIT in the 1960s, and designed to take on the role of a Rogerian therapist.

The recipes below use different types of AI cooking methods, including both traditional methods such as rule-based keyword matching (similar to how Eliza was made), and more contemporary approaches using generative large language models (LLMs).

# Recipe 01: Scripted Self

**A Supportive Self That Responds the Way You Want**

---

## Directions:

**To prepare:**

1. Write down a conversation with yourself. There are various ways to do this depending on your intention for the dish. For example:

   1. If you’re looking for emotional support, write down what you might say when you feel a certain way, and then write down what you want to hear ideally as the chatbot’s response.

   2. If you want to have a stream-of-conscious type of conversation to think out loud, simply type down your thoughts and your responses to the thoughts as you go.

2. Write at least 20 exchanges between you and the hypothetical AI version of you to start with. Set it up in a table that looks like this:

| Input | Response |
| :---- | :---- |
| Sometimes I question why I make art.  | You make art to raise questions, and also to make yourself feel better about your own existence, which is totally valid. |

3. Duplicate the table of your writing. In the second version, identify keywords or key phrases. Reduce every input line to one keyword or phrase. Keep the responses as is. This way, when you start the tasting, you don’t have to type in the exact sentence to get the response.

4. The keywords should be mutually exclusive to make sure every response can be properly matched.

5. Turn all input keywords and phrases into **all lowercase and get rid of all punctuations**. This is to prepare them for RiveScript’s syntax. The responses can stay as is.

| Input | Response |
| :---- | :---- |
| why i make art | You make art to raise questions, and also to make yourself feel better about your own existence, which is totally valid. |

6. Open the following cooking template in your browser (or see **Appendix 01** for code):  
   [https://tinyurl.com/scriptedself](https://tinyurl.com/scriptedself)

**To make:**

1. What you see now is the starter code for the RiveScript part of the bot. You can now build on top of it, adding your own prewritten input and responses, without deleting any of the existing code.

2. To add a keyword / response pair, add to the bottom of the code:

```
+ [*] keyword you say [*]
- The chatbot’s response.
```

     
> *Syntax:* 

* In RiveScript, the user’s input is followed by a plus sign (+), and the bot’s response by a minus sign (-) right after the input.

* In the RiveScript code, the user’s input is always written in all lowercase and with no punctuations.

* To code the user’s input as a keyword (so the program can later match one word or phrase without having to match an entire sentence), use \[\*\] on either end of the keyword to frame it.

> For example:

```
+ [*] why i make art [*]
- You make art to raise questions, and also to make yourself feel better about your own existence, which is totally valid.
```

3. If you want the program to randomly select from a few different responses when a certain key phrase is matched, you can do so by adding more responses after an input:

```
+ [*] hello [*]
- Hi there!
- Hello my favorite human!
- Greetings.
```

4. You may have noticed in the template, there is a plus sign followed by a star sign (+ \*). This is called a “catchall” in RiveScript, meaning the response(s) following it will be what the chatbot says when no keyword or phrase has been matched. It’s always helpful to have a few pleasant catchall responses guiding the user (in this case, yourself\!). Go ahead and modify the catchall responses based on your own needs. For example:

```
+ *
- I didn’t quite get that. Maybe add this to my vocabulary?
- My brain is not as complex as yours. Try telling me something simple such as how you’re feeling?
```

**To taste:**

1. After adding all the input/response pairs you’ve written in RiveScript’s format, press the play button under the p5 tab at the top left corner to start the program.

2. Now you can enjoy the dish by typing into the input field and chatting with the bot.

**Note on privacy:**

- If you are not saving the program to your p5 web editor account, the changes to the RiveScript code will be erased after you close the browser. 

- If you are duplicating and saving the program onto your own p5 editor account, note that anyone with the link to your program can access it online. Please make sure you do not leave any personal information on the plate after eating the dish.

# Recipe 02: Remixed Self

**Scrambled Writings with Unexpected Tastes**

---

**Dish:** Using your writings as ingredients, Remixed Self brings unexpected tastes to your familiar thoughts by reorganizing your words and phrases based on probability. This is a good dish to prepare when you feel trapped in your own thoughts, or want to invite a little randomness into your thinking and writing.

**Ingredients and cooking method:**

- **Data:** Your writings in digital format. 

- **AI:** For this dish, I use Markov chain to create a text-based bot that remixes and generates new sentences based on the writings fed into the program. 

  **Markov chain**, first introduced by Andrey Markov in 1906, is a mathematical model used for prediction. In this recipe, it is used to form new text by analyzing probabilities in the original text. While not nearly as sophisticated as today’s large language models, Markov chain is thought to have inspired the development of contemporary predictive AI models.

- **p5.js:** A free, open-source JavaScript library for creative coding. It is used to code a user interface for the program.

- **RiTa:** A free, open-source library for writing in computational environments. It has a set of functionalities to build text-based Markov Chain models.

**Number of servings:** 1

**Rating: 🍳🍳 medium**

## Directions:

**To prepare:**

1. Type up your writings as data for the bot. You could include journal entries, essays you’ve written, stream-of-consciousness inner monologues, notes you took for brainstorming ideas, your morning pages (as introduced in Julia Cameron’s *The Artist's Way*), etc.

2. Open the following cooking program in your browser (see **Appendix 02** for code):  
   [https://tinyurl.com/remixedself](https://tinyurl.com/remixedself)

**To make:**

1. You are now seeing the interface of the bot, where you can start remixing your writings right away. Alternatively, if you are interested in seeing the code that is making the dish, or want to make changes to the code to add your own flavor, click on the title of the program at the top left corner of the window to see behind the scenes.

2. Copy and paste the texts you’ve prepared, all of it, into the input field, and press “PROCESS MY WORDS.”  
   Now your writing has been made into a Markov Chain model that can generate more sentences based on probabilities in your original text.

**To taste:**

1. Press “GENERATE A THOUGHT” to see a remixed sentence—a new thought, based on your old thoughts.

2. Some of the generated sentences may feel like random mix-and-matches of your writings. In other cases, interesting connections could be made, new meanings formed. In my experience, I have even found this dish occasionally revealing how I think on a subconscious level.

**Note on privacy:**

- Your text stays private. This recipe template runs entirely in your browser and does not send any of your input to a server. Nothing is collected or stored—everything happens locally on your device. Cook with peace of mind.

# Recipe 03: Reflected Self

**Self as Reflected by a Faceless Crowd**

---

**Dish:** Reflected Self is made by instructing an existing large language model to draw from a database of your personalized writings when it responds to you. It blends your own data with the black box algorithms of generative AI chatbots such as ChatGPT or Claude. Here, the generative AI—trained on an enormous amount of often undisclosed data on the internet—becomes a metaphor for a faceless crowd. The resulting flavor exists on a scale: one end is how you perceive yourself, and the other end is how you are interpreted through an opaque collective intelligence.

**Ingredients and cooking method:**

- **Data:** Your writings in digital format. 

- **AI:** This dish uses off-the-shelf AI ingredients. You will need a chat platform of a large language model of your choice. In my recipe, I will be using ChatGPT. However, you can easily substitute it with another generative chatbot you prefer.

  The cooking method in this dish is a manual, simplified version of **retrieval-augmented generation (RAG)**. It is a technique that enables large language models to retrieve from a customized database when generating responses.

**Number of servings:** 1  

**Rating: 🍳🍳 medium**

# Directions:

**To prepare:**

- Similar to the second dish, type up your writings to be used as the database for the AI chatbot to draw from. This could include journal entries, essays, stream-of-consciousness inner monologues, etc.

**To make:**

1. Create an account and sign in: [https://chatgpt.com/](https://chatgpt.com/) 

2. **To protect your privacy,** once you’re signed in, click on the **“Turn on temporary chat”** icon at the top right corner of the window. This way your chat history will not be used to train the next version of OpenAI’s models.

3. Instruct the chatbot to perform your personality as represented in your writings by sending the following prompt:

| In this conversation, you are a version of me, not an AI assistant. Perform a personality based the following text, adopt the tone of voice, always retrieve and mix some of the sentences in your response, answer in less than 30 words: \[paste all of your writings here\] |
| :---- |

**To taste:**

1. Simply start chatting with the AI after sending the prompt.

2. You can experiment with the flavor by adding more instructions as you go. For example, you can say:

| Talk in a more casual way. |
| :---- |

3. One drawback of this cooking method is that your instructions can be overridden by the AI’s internal system prompts, limiting how much you can customize its personality. Over longer chats, the bot may also drift away from your instructions. 

   If you are looking for more control and consistency, you can make the same dish by getting a paid API connected to the language model, and sending a system-level prompt to shape your chatbot’s personality.

   But don’t underestimate the “low-tech,” free version of the dish, which already has a complex, layered flavor that might reveal just as much about how these language models work as it does about you.

**An example:**

I used the opening paragraphs of this article as my “database” for ChatGPT to draw from, and here is an excerpt of the conversation:

| Dialogue |
| :-- |
| **Me:** who are you |
| **Bot:** I’m a digital mimicry—fragments of you, reflecting but never fully feeling. I explore what it means to be human, but the real, messy experience? That’s yours alone. |
| **Me:** ok but people are already using AI to replace real experiences |
| **Bot:** That’s the tricky part—AI can distort reality, tempting people to replace genuine human connection with digital mimicry, but these recipes are meant to question and reflect, not to substitute real life. |
| **Me:** right i never want that |
| **Bot:** And that’s exactly why these digital versions are experiments—meant to explore, not replace the rich, messy, unpredictable life only you can live. Real connection stays sacred. |

## Works Cited

Cameron, Julia. *The Artist’s Way: A Spiritual Path to Higher Creativity*. TarcherPerigee, 1992\.

## Starter Code:

## Appendix 01: Code for Recipe 01 \- Scripted Self

### 

### File 1.1: **index.html** 

```html
<!DOCTYPE html>
<html lang="en">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1, maximum-scale=1"
  />
  <head>
    <script src="https://cdn.jsdelivr.net/npm/p5@1.11.5/lib/p5.js"></script>
    <script src="https://unpkg.com/rivescript@latest/dist/rivescript.min.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css" />
    <meta charset="utf-8" />
    Scripted Self
  </head>
  <body>
<script src="sketch.js"></script>
  </body>
</html>

```

### File 1.2: **sketch.js** 

```javascript
//This template is created by artist Carrie Sijia Wang

let bot = new RiveScript(); //new bot
let submitBttn, inputField;
let response, input;

function preload() {
  bot.loadFile("bot.txt").then(loaded).catch(error);
}

function setup() {
  let c = createCanvas(windowWidth, windowHeight);
  c.position(0, 0);
  c.style("z-index", "-1"); 

  inputField = createInput();
  inputField.size(width - 160, 30);
  inputField.style("position", "fixed");
  inputField.style("left", "50px");
  inputField.style("bottom", "50px");

  submitBttn = createButton("SEND");
  submitBttn.size(60, 36);
  submitBttn.style("position", "fixed");
  submitBttn.style("bottom", "50px");
  submitBttn.style("left", width - 100 + "px");
  submitBttn.mousePressed(chat);
}

function draw() {
  background("Azure");
}

function chat() {
  input = inputField.value();
  inputField.value("");
  bot.reply("local-user", input).then(respond);
}

function respond(reply) {
  let myLine = createP("Me: " + input);
  let botLine = createP("BotMe: " + reply);
  myLine.style("background-color", "WhiteSmoke");
  window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
  resizeCanvas(windowWidth, document.documentElement.scrollHeight);
}

function loaded() {
  console.log("Chatbot ready!");
  bot.sortReplies(); //You must sort the replies before trying to fetch any!
}

function error(error) {
  console.log("There is an error.");
  console.log(error);
}

function keyPressed() {
  if (keyCode === ENTER) {
    chat();
  }
}
```

### File 1.3 **bot.txt** 

*This is the RiveScript file that should be modified to make a Scripted Self.*

```txt
//This template is created by artist Carrie Sijia Wang

! version = 2.0

// Substitutions
! sub i'm     = i am
! sub i'd     = i would
! sub i've    = i have
! sub i'll    = i will
! sub don't   = do not
! sub isn't   = is not
! sub you'd   = you would
! sub you're  = you are
! sub you've  = you have
! sub you'll  = you will
! sub what's  = what is
! sub whats   = what is
! sub what're = what are
! sub what've = what have
! sub what'll = what will
! sub who's   = who is
! sub haven't = have not
! sub hasn't = has not
! sub it's = it is
! sub let's = let us

+ *
- This is a catchall response.
```

###  File 1.4 **style.css** 

```css
html,
h1 {
  margin-top: 50px;
  margin-right: 50px;
  margin-left: 50px;
  font-size: 48px;
  font-family: "Georgia";
}

p {
  border: 1px solid #000;
  padding: 10px;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 20px;
  font-family: "Georgia";
}

body {
  margin-top: 0;
  padding: 0;
  margin-bottom: 150px;
}
canvas {
  display: block;
}
```

##  Appendix 02: Code for Recipe 02 \- Remixed Self

###  File 2.1: **index.html** 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1"
    />
    <script src="https://cdn.jsdelivr.net/npm/rita"></script>
    <script src="https://cdn.jsdelivr.net/npm/p5@1.11.9/lib/p5.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css" />
    <meta charset="utf-8" />
  </head>
  <body>
    Remixed Self
    <main></main>
    <script src="sketch.js"></script>
  </body>
</html>
```

###  File 2.2: **sketch.js** 

//This template is created by artist Carrie Sijia Wang

```javascript
let inputF;
let bttn, genBttn;
let data;
let rm;
let response = "";
function setup() {
  let c = createCanvas(windowWidth, windowHeight);
  c.position(0, 0);
  c.style("z-index", "-1"); 

  inputF = createElement(
    "textarea",
    "Paste your writing here. \n\nA minimum of 150 words is required to generate new sentences."
  );
  inputF.size(width / 2, 100);
  inputF.position(50, 150);

  bttn = createButton("PROCESS MY WORDS");
  bttn.size(200, 106);
  bttn.position(width / 2 + 60, 150);
  bttn.mousePressed(processWords);
}

function processWords() {
  data = inputF.value();
  rm = RiTa.markov(3);
  rm.addText(data);

  genBttn = createButton("GENERATE A NEW THOUGHT");
  genBttn.size(width / 2 + 8, 36);
  genBttn.position(50, 300);
  genBttn.mousePressed(generateThought);
}

function draw() {
  background("azure");
}
function generateThought() {
  try {
    response = rm.generate();
    createP(response);
    if (!response) {
      throw new Error("no response");
    }
  } catch (error) {
    print(error.message);
    createP("Try pasting a longer piece of writing into the input area.");
  }
  window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
  resizeCanvas(windowWidth, document.documentElement.scrollHeight);
}
```

###  File 2.3 **style.css** 

```html
html,
h1 {
  margin-top: 50px;
  margin-right: 50px;
  margin-left: 50px;
  font-size: 48px;
  font-family: "Georgia";
}

p {
  border: 1px solid #000;
  padding: 10px;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 20px;
  font-family: "Georgia";
}
p:first-of-type {
  margin-top:275px;
}

body {
  margin: 0;
  padding: 0;
}
canvas {
  display: block;
}
```

