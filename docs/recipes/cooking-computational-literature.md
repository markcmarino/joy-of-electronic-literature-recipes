---
title: Cooking Computational Literature
chef: Nick Montfort
abstract: 
description: [Please add]
genres:
difficulty_pans: 2
yields: 
---

# **Cooking Computational Literature**

Nick Montfort  
Professor of Digital Media, Comparative Media Studies/Writing  
Massachusetts Institute of Technology (also Professor II & Principal Investigator, Center for Digital Narrative, University of Bergen)

Among the many types of electronic literature — some based on the traversal of text via links, some emphasizing multimedia elements — several are *computational*. These works are computer programs, interactive or not, based on selecting from a probability distribution(a.k.a. “randomness”) or not. They manipulate symbols, textual ones, engaging with the potential of computing to invite new types of reading.

Examples of computational literary works include, but are not limited to:

* Poetry and story generators

* Literary (as opposed to purely informative) chatbots

* Interactive fiction and other games inflected in literary ways

* Computational works of visual poetry

One productive way to think about this sort of work is that it uses computation not just as a tool or delivery mechanism, but as a *medium,* a distinction that has been discussed clearly with regard to digital art in general (Paul 67–138). Literary artwork in which computation is the medium is not only digital in terms of representation. It’s made out of language and computation.

There are many ways to begin developing computational literary art, if you find this type of work compelling. Those who are expert in programming, or collaborate with expert programmers, can plan and accomplish elaborate projects. But an electronic literature author — let’s call this person an author/programmer — doesn’t have to have extensive programming background to get going. An author/programmer who is a *new programmer* can develop a computational literary work, just as someone learning to cook can prepare a dish.

If you love computational literature, you can develop your abilities as a programmer as you also work on the literary art you love. It’s possible to create new computational literature in a bottom-up way, making incremental changes to an existing work. You can swap out strings of text in the original program with your own text, then change and tune parameters, and then start to explore how to edit the code itself. Modifying a work can help you better understand computation as well as language.

To effectively complete such project of bottom-up modification, I recommend that an author/programmer who is new to programming do the following:

(1) find a work that seems compelling in some way,

(2) make sure this work is free software, so that its code is available for modification,

(3) ensure the code is reasonably simple,

(4) choose a program that is clear and well written, and

(5) proceed incrementally, testing every minor modification.

I’ve tested this advice many times in workshops with others and by developing computational literary works in this way many times. I also developed two just for the current discussion. After going through those, I’ll conclude with an enriched discussion of the more general case, explaining why I think these five recommendations are really essential for any bottom-up modification project of this sort and how they will help a new author/programmer.

1. ## ***Stochastic Texts → Really Eely***

In the late 1950s Theo Lutz wrote a computer program — a work of computational literary art — on the Zuse Z22 computer (Lutz, MacCormac). It is a sentence generator, although sometimes it generates two short sentences at once: “Every house is quiet. Every table is large. / A picture is far. Not every tower is near.” The system draws its vocabulary from Franz Kafka’s *The Castle* and produces logical statements uniformly at random, so that it is just as likely to output a proposition as it is its contradiction. In terms of both its grammatical functioning and its lexicon, it’s Kafkaesque.

As part of a larger project called *Memory Slam,* I wrote a program based on Lutz’s generator that essentially reimplements this generator. While it’s meant to be formally authentic, it doesn’t work *materially* like the original program did — Lutz used a teletype for output. My main point was to provide reasonably clear and cleanly-written code so that new programmers could study and modify it. I wrote two programs; the HTML/CSS/JavaScript version can be found here:

[https://nickm.com/memslam/stochastic\_texts.html](https://nickm.com/memslam/stochastic_texts.html)

This links to a Python program that functions the same way, as far as text generation is concerned.

I’ve modified the JavaScript program before. In fact, I often make quick modifications to it when I’m leading a workshop to demonstrate how easy it is to make changes to a text generator of this sort. You can read about some of the ways I often modify this program, and encourage others to modify it, in the second edition of *Exploratory Programming for the Arts and Humanities,* an open access book from MIT Press.

In 2024 I read poet Steve Ely’s remarkable book *Eely.* I modified Lutz’s generator to incorporate nouns and adjectives from the beginning of this book. My main changes to the HTML/CSS/JavaScript version of *Stochastic Texts* are right here:

		`const subjects = ['snow', 'water', 'darkness', 'milt', 'roe', 'eel',`  
			`'egg', 'current', 'journey', 'elver', 'bootlace', 'bank', 'sea',`   
			`'bottom', 'silt', 'vessel', 'body'],`  
		`predicates = ['elongate', 'emphatic', 'autumn', 'twilit', 'zigzag',`   
			`'toxic', 'cool', 'blind', 'rumbling', 'fasting', 'flung', 'deep',`   
			`'submarine', 'winter', 'smoking', 'muscular']`

Other than those two assignments, I only changed the header to provide my new title, name myself as the author, and provide a line of explanation about how this conflates *Stochastic Texts* and *Eely*. Some of the resulting output:

Not every sea is muscular and not every sea is elongate.

No sea is blind. No egg is smoking.

Not every milt is autumn. An elver is twilit.

A body is blind therefore no bottom is submarine.

Of course, I make it sound easy. If you modify this or any of the *Memory Slam* programs, you could encounter problems. For instance, I might have made a seemingly minor typo and made this change instead:

		`const subjects = ['snow', 'water', 'darkness', 'milt', 'roe', 'eel',`  
			`'egg', 'current', 'journey', 'elver, 'bootlace', 'bank', 'sea',`   
			`'bottom', 'silt', 'vessel', 'body'],`

Those who have a good amount of experience programming can use the browser’s error message to debug the program. But if you’re just getting started with programming, don’t worry about that as a very first step.

When you see that there’s a blank Web page, that the text generator isn’t running anymore, just do as follows: *Undo* (CTRL-z, COMMAND-z); *Save* (CTRL-s, COMMAND-s), and open that Web page again. If that doesn’t work, keep undoing your changes and saving the result until you have a working Web page. And if you run out of undos, just download the original again and start over.

Hopefully you will proceed incrementally — that is, very gradually — following my recommendation (5). That will make it much more likely that you can easily back out of any typos or other errors introduced. And as you become a more advanced programmer, you *still* will want to proceed in steps as small as possible, testing along the way. The error I made, by the way, was leaving off the closing straight single quotation mark after “elver.” Remember, though, you don’t have to track that sort of error down to get your modification working — just follow this process.

2. ## ***robotfindskitten → HunterSeeksBounty***

The approach that I’m discussing, bottom-up modification, doesn’t only apply to text generators, nor does it only apply to JavaScript. To demonstrate this, I’ll provide a more advanced example. I’ll take the beloved and tender “zen simulation,” Leonard Richardson’s non-confrontational Rougelike game *robotfindskitten,* and transform it into a dark, post-apocalyptic work, *BountyStalker.*

People have already ported *robotfindskitten* (originally written in 1997\) to many different platforms, and occasionally some have modified it, for instance into *jason finds fleece*, Gunter Schmidl’s Inform 6 game. The now-canonical version of the game runs in a terminal window. The user directs a robot around an ASCII grid, where there are numerous other characters — characters in both the ASCII and the fictional sense. All but one is some non-kitten object. As robot encounters non-kittens, each one is indicated with a whimsical line of text along the top of the terminal window. Eventually, as long as the user persists in the search, robot will find kitten.

I challenged myself a bit by modifying the canonical version of this game, which is written in C.[^1] If I’d wanted to just change the messages, and keep the same name, title screen, and mechanics, I could have done all of that without changing the code and recompiling the game. You can simply edit a text file called “vanilla.nki” to change those non-kitten item messages.

However, I decided I did want to change the game’s name, version number, and title screen, and of course I wanted to credit my new game to me. I also wanted to make one significant change to how *BountyStalker* functioned. I wanted to make sure the “target” was never placed in the window at all. I didn’t invent this sort of unwinnable scenario, but it was how I thought to transform this zen simulation to a nihilist one. Making the game unwinnable involved removing 75 lines of code from the 791-line robotfindskitten.c file. The other changes were mostly minor ones that involved editing text. In order to (temporarily) fool the player, I had to add a “+ 1” in one place so that instead of generating *n* bogus items to scatter across the terminal window, as promised, it generated *n+1* of them.

![][image1]

***Figure \[N\]. The original robotfindskitten (above) and my modified game have an identical playing field, but the messages are selected from a large, less unified, and more whimsical set in the original simulation, which the persistent player will always win.***

The 30 messages I wrote for *BountyStalker* could have been added to the about 700 that are standard in *robotfindskitten,* but I wanted them to stand alone. They’re meant to be darker, more unified, and more allusive. Some of them are:

A puddle of iridescent toxicity.  
A vine. Fake, of course. And very expensive.  
Impassible concrete and rebar.  
Some busted and stripped cyberdeck.

## ***How to Start Cooking Computational Literature***

Having provided these two specific examples, I’ll elaborate on my general advice:

(1) *Find a work that seems compelling in some way.* Many people have modified my simple poetry generator *Taroko Gorge,* but I must admit that most of them were assigned to do so in college classes\! Feel free to start with this one if you like, though. In any case, if you’re choosing a project of your own, make sure there is something that seems really great to you about your starting point. You can intensify that aspect of the original while you question or invert other aspects of that work.

(2) *Make sure this work is free software, so that its code is available for modification.* Some people use “open source” to mean something very similar to “free software,” although this latter term emphasizes providing people with freedoms. In any case, you do somehow need access to the code to be able to modify the code. Although you *can* edit JavaScript that you find on the Web — even if the code isn’t free software, so you haven’t been given permission — doing so could make it harder for you to share the resulting project with others.

(3) *Ensure the code is reasonably simple.* The trick, of course, is to find an original work that is compelling to you (as in point 1\) while also fairly easy to study and manipulate. A few pages of code — ideally, a single page — is a good amount for a first project. Remember that your first project doesn’t have to be your *last* project, and that completing a reasonably easy modification can help you see the potential of computational literature and build toward more elaborate work.

(4) *Choose a program that is clear and well written.* Simplicity, emphasized in point 3, certainly helps here, but short programs can be compressed and obfuscated, so watch for that. Beyond that, there are a few entailments of this principle:

(4a) Use a human-written program. Generative garbage emitted by a hallucinating corporate machine is a very poor starting point, and can contain code obfuscations and incorrect comments — even if it somehow happens to work as intended, which it may not\! Ideally, you could choose a program that has either been developed by a human being to be modified (as with *Taroko Gorge* and the programs in *Memory Slam*) or has been refined and polished collaboratively by several humans (as with *robotfindskitten*).

(4b) In addition to choosing a program that is clear and well written, it’s ideal if the *programming language* used has certain qualities. An interpreted language is better than a compiled one in this case, because you can run the program often without extra steps each time. (C, for instance, is compiled, while JavaScript and Python function as if they were interpreted.) A language that is welcoming for beginners and is in widespread use today is a great choice. This also recommends JavaScript or Python. A poorer choice would be Lisp or Rust. BASIC, which welcomed many new programmers in the 1970s and 1980s, is actually a collection of incompatible dialects and sees little use today, so unless you find carefully crafted programs in this language, they may not be the best to start with. I decided to modify the canonical C implementation of *robotfindskitten,* but a port of that game could have been a better starting point.

(5) *Proceed incrementally, testing with every change to make sure what you’re modifying still works.* If you are able to try out each of your changes in this way, you can avoid dealing with (for instance) version control before you get into a little creative coding. To be a recreational programmer, you don’t need to be a software developer using professional “best practices.” Just try running your project after you make a change or two; if you broke something, you can simply use the “Undo” command in your text editor to restore your code to a working state. In the worst case, since you’re only making small-scale changes, you can grab the original code again and edit again, more carefully. You can and will benefit from learning to use version control as you start to do more, particularly if you collaborate with others — but cross that bridge when you come to it.

With these suggestions in mind, you’ll be well equipped to start actually programming — working with code and making it your own — even if you’ve never taken a programming course of any sort. You can create a work of computational literature that you can share with others by publishing it or posting it. If you find that developing computational literature is compelling, and you want to pursue it further, you can always learn the fundamentals of programming, begin collaborating on projects (with version control), and expand your potential as an author/programmer.

3. ## ***Acknowledgments***

This research was partially funded by the Research Council of Norway Centres of Excellence project number 332643, the Center for Digital Narrative.

4. ## ***Bibliography / References***

Ely, Steve. *Eely.* Longbarrow Press, 2024\.

Lutz, Theo. “Stochastische texte,” *augenblick* 4.1 (1959): 3–9.

MacCormac, Helen. “Stochastic Texts” \[trans. of Lutz 1959\], *netzliteratur.net,* 2005\. https://stuttgarter-schule.de/lutz\_schule\_en.htm

Montfort, Nick. “Taroko Gorge.” *nickm.com.* 2009—2025. https://nickm.com/poems/taroko\_gorge/

——— *Memory Slam.* 2014–2024. https://nickm.com/memslam/

——— “Computational Literature.” *Between Humanities and the Digital,* eds.  Patrik Svensson and David Theo Goldberg, MIT Press, 2015, pp. 205–15. https://doi.org/10.7551/mitpress/9465.003.0020

——— *Exploratory Programming for the Arts and Humanities.* MIT Press, 2021\. https://nickm.com/books/exploratory\_programming\_2e/

Paul, Christiane. *Digital Art,* 3rd ed. Thames & Hudson, 2015\.

robotfindskitten consortium. “The Many Ports,” n.d., http://robotfindskitten.org/aw.cgi?main=software.rfk

[^1]:  Actually, I also changed the documentation, configuration files, and makefiles, which really wasn’t necessary. New programmers: Don’t do this\! I only bothered because I wanted to poke around and learn more about this real project that has been packaged and is available for different Linux distributions.
