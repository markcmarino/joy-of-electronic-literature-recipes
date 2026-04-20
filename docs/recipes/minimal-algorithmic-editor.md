---
title: A Minimal Algorithmic Editor
chef: Kyle Booten
abstract: A recipe for building a personalized algorithmic editor that uses regular
  expressions to detect writing patterns and insert custom annotations prompting revision.
description: >
  Let's say that you've noticed something about your writing that you wish you could remember to do a bit better.  
  Perhaps you tend to overuse a word.  Perhaps you slip into syntactic repetition.  
  This recipe is for a very simple algorithmic editor that will automatically scan your text for signs of these infelicities.
  It will automatically annotate them with editorial messages to you, the writer, such as "hey, don't use that word so much!"
  To make this editor work, you will have to write regular expressions, which allow you to flexibly match patterns in text.
  The patterns your editor notices, however, need not be limited to errors or infelicities.  
  You might use this minimalistic algorithm editor more creatively, just to furnish you with unexpected, strenuous suggestions to make.
  Other uses could surely be imagined.
genres:
  - Human-computer collaboration
  - Machine reading
difficulty_pans: 3
yields: >
  Pairs, each consisting of 1) a textual PATTERN, and 2) an ANNOTATION that will be automatically applied to it. One line of code for applying a (PATTERN, ANNOTATION) pair to a plain text file. A Python script for applying many of these patterns at once and according to user-defined probabilities. 
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/minimal-algorithmic-editor.md
---

# A Minimal Algorithmic Editor

Kyle Booten

Assistant Professor, Department of English

University of Connecticut

**Class of E-lit:** Human\~computer collaboration, machine reading  
**Dish:** A program that automatically inserts editorial comments into a human writer’s text.

**Required ingredients:** *Computer (ideally a Mac or Linux machine).  The computer language Perl. The computer language Python. Text editor. Terminal emulator. A piece of human-written text.*

**Preparation and cooking time:**  30 minutes 

**Number of servings and serving size:** Melange of editorial annotations applied to the human-written text

**Rating: 🍳🍳🍳** three pans, medium

# Background

When the jagged red serpent appears underneath a misspelled word, or when Google Mail’s “Autocompose” suggests a way to finish your sentence, you have participated in something akin to “e-lit.” The human writes. A computer program reads and gives suggestions.  The human writer may respond in turn, rejecting or accepting any algorithmic suggestions.

Perhaps you have tried out a more ambitious version of this human\~computer collaboration using state-of-the-art AI. (“Please, ChatGPT, make this email sound smarter, sound nicer, have better grammar, make more sense.”) In this case, the AI is your editor, albeit one much more complex (and presumptuous) than the spell-checker or even Autocompose.

This recipe is for creating another kind of algorithmic editor (or writing partner, or coach, or, if you are in the mood, saboteur), one that is simpler even than a spell-checker—simpler, but also more flexible. 

The general pattern of this recipe is as follows:

1\.    	the human produces some writing

2\.    	the human observes places where their writing could be corrected, expanded, challenged, or otherwise developed

3\.    	the human writes code that automatically notices these infelicities; 

4\.	the code is executed, and it marks up the text with helpful messages

5\.    	these messages prompt the human’s revision of the text

# Recipe

## Step 1: Write Something

The first step—the human produces some writing—is self-explanatory.  For the purposes of this recipe, it is important for the human-generated writing to exist as a “plain text” (.txt) file rather than something more complicated such as a .docx.

Here is a short example text:

I was driving back to the shop to see if I could find a thing that could make me feel happy. I was listening to jazz. Then my phone rang.

## Step 2: Discover Places for Further Development or Improvement

There is nothing wrong with the above text, per se. There are no spelling errors, no malapropisms. But this does not mean that it oughtn’t be torqued or retuned—made more minimalistic, more rococo, wittier, slimier, cleaner, greener, bluer, stronger, faster, more ergonomic, more profane.

* First, we might notice with mild discomfort a word that is too vague—“thing.” Lots of things are things. What type of thing is this thing?  
* A pet peeve: when two sentences begin the same way and it does not seem like intentional anaphora but rather mere lethargy: “I was driving…” and “I was listening…”  
* What kind of jazz? Couldn’t we use some detail here?  
* “Then my phone rang.” is simply boring.


## Step 3: Get the Computer to Notice these Patterns

This is the trickiest part. We have ourselves noticed some places where the text could be improved. Now we need to get the computer to notice them too.

For this recipe, you will do this with *regular expressions*. Regular expressions (or “regexes,” from *REGular EXpressions*) are a way of describing patterns that you want to look for and capture in a sequence of characters (a “string”). For instance, if you want to match the word “thing”, you could use this very simple regex

>`\bthing\b`

which is the sequence of five letters, thing, bracketed on either side with `\b`, a special sequence that means “word boundary”; these are added so that the regex will match the word “thing” but not this sequence of letters when it is inside other words, such as “brea*thing*.”

Let’s say you wanted to match any of some number of words, not just one word. You could do so like this:

>`\b(jazz|ragtime|big band)\b`

which means “word boundary,” then “either the letters ‘jazz’ or ‘ragtime’ or ‘big band’,” then another word boundary.

Going back to our original paragraph, we could also build a regular expression to hunt for overuse of “I was” to begin a sentence. Like so:

>`\bI was\b.{1,1000}\bI was\b`

This regex has three main parts. First, `I was` matches this sequence of characters exactly (and both preceded and followed by word boundaries). Next, `.{1,1000}`. This part is tricky, because `.` in a regex does not mean period; rather it is a special symbol that means “any character” (except a newline). `{1,1000}` modifies this special symbol here, so `.{1,1000}` means “between one and one thousand characters, (more or less)[^3] whatever those characters happen to be.” Finally, the last part of the regex: `\bI was\b`. So this regular expression matches a span of text that begins and ends with "I was", with some number (between one and one thousand) characters in between.[^1] Whew!

It would be hopeless to try to explain all the things that one can do with regular expressions; they are as flexible as they are tedious, and they can be extremely tedious. If you are new to them, start out simply: write one to match a word, one to match a word from a series of words, and one to match a word that is not followed by some other word or character. You can get pretty far with just those.[^4]

## Step 4: Compose Annotations

Having used regular expressions to computationally read your own text, it is now time to computationally annotate your text. For each of the regular expressions, come up with one or more series of messages that you want to send yourself.

Messages might be simple, hinting at simple fixes:

>`\bthing\b` → “come up with a more specific word?”

>`\bI was\b.{1,1000}\bI was\b` → “make sure you really want this repetition in these sentences...it might sound kind of lifeless”

But they might also be more opinionated, raising open-ended challenges:

>`\b(jazz|ragtime|big band)\b` → “implicitly contradict Adorno’s critique of jazz”

## Step 5: Let the Program Annotate your Text

Regular expressions can be used in various contexts and in most programming languages, making them both handy and portable. However, one way of using regular expressions is with the programming language Perl, which can be invoked directly in the command line and used to edit files. If our human-written text is saved in a file such as `my_text.txt`, a Perl command can be used to match the regular expressions against the file’s contents and then rewrite these contents, adding annotations where appropriate, and then output the annotated contents to a second file. Like so:

>`perl -pe 's/\b(jazz|ragtime|big band)\b/$1 <~[implicitly contradict Adorno’s critique of jazz]/g' my_text.txt > my_text_annotated.txt`

The file `my_text_annotated.txt` now contains:

>`I was driving back to the shop to see if I could find a thing that could make me feel happy. I was listening to jazz <~[implicitly contradict Adorno’s critique of jazz]. Then my phone rang.`

## A Variation on Step 5

Let’s say you have many regex patterns that you want your computer, using regex, to look out for and annotate in your text.  Running each individually could get very annoying.  Additionally, let’s say you don’t want the computer to annotate your text every time it notices your pattern.  That might get boring and predictable, after all.  

A program written in Perl could do this. But more people these days use Python, so here is a simple Python program:

### Starter Code

```python
import re
import random
import sys

pattern_annotation_pairs = [ ## regex, annotation, probability of annotation
    (r"\bjazz\b",  "<~[contradict Adorno’s critique of jazz]",  0.4),
    (r"\bthing\b",  "<~[use a more specific word!]",  0.9),
    (r"\bhappy\b",  "<~[what even is happiness?]",  0.4),
    (r"\bI was\b.{1,1000}\bI was\b",  "<~[nix repetition!]",  0.5),
]

def annotate_line(line):
    for pattern, note, p in pattern_annotation_pairs: ## iterate through each rule in `rules` (above)
        regex = re.compile(pattern, flags=re.IGNORECASE)

        def repl(match):
            if random.random() < p:
                return match.group(0) + " " + note
            else:
                return match.group(0)

        line = regex.sub(repl, line)
    return line ## return the (possibly) annotated line

for line in sys.stdin:
    print(annotate_line(line), end="")
```

The key part of this code[^2] is the variable called `pattern_annotation_pairs`. It contains a list of three-part data that look like this:

```python
(r"\bjazz\b",  "<~[contradict Adorno’s critique of jazz]",  0.7)
```

That is: a regex, an annotation, a probability that the annotation will be inserted any time a match is found. Add your own patterns there.  

Then, save this code in a file called my\_editor.py.  You can create an annotated version of your text file like this:

>`python my_editor.py < my_file.txt > my_file_annotated.txt`

There are all kinds of features that one might add to this program.  For instance, a more complicated version might associate each regex with a series of annotations, one of which is selected randomly, so there is more variation.

## Step 6: Revise Your Text

Take the editorial comments you receive seriously.  This could mean taking up the challenges offered by the comments and revising accordingly, like so:

>I was driving back to the record shop to see if I could find a riff that could make me feel like I am merely repeating a day I never lived and that is enough.  Jazz, I had the hunch, would do it, would help me (not “regress” but) return. Then my phone rang.

Taking these comments seriously, however, could also mean fighting back against them.

## Related

**Title TK**

Explanation TK.

Go to page: TK

[^1]:  This is a simpler regular expression than what you’d want to use to make sure that “I was” appears in two sequential *sentences*; I have simplified this for demonstration purposes.  Additionally, this regular expression is "greedy" rather than "lazy," but let's not get bogged down in such subtleties.    

[^2]:  This program is, in a sense, a simple and customizable version of a “linter” for writing, though these tend to focus quite narrowly on errors and other infelicities; see, for example, Ampersand Lab’s Prose Lint ([https://github.com/amperser/proselint](https://github.com/amperser/proselint)). On the other hand, Zach Smith has been developing a linter that is “designed to impose constraints on a literary composition that are both stochastic and concrete.” It is much like the linter I describe here, except much more technically sophisticated and designed integrate into various text editors ([https://git.sr.ht/\~subsetpark/gym](https://git.sr.ht/~subsetpark/gym)).

[^3]:  This `.` will not match a newline (i.e, a linebreak) character. So the algorithmic editor will only notice patterns that occur within a single line in a text file. 

[^4]:  An important caveat is that, in the case of the Perl and Python code provided by this recipe below, these regular expressions will only apply to a line of text at a time.
