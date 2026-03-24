---
title: Gorgeous Taroko Gorges
chef: Mark C. Marino
abstract: A recipe for remixing Nick Montfort's classic infinite generative poem Taroko Gorge with your own themed word lists.
description: >
  Taroko Gorge, written by Nick Montfort on a flight to Taiwan in January 2009,
  is one of the most celebrated and widely remixed works of generative poetry.
  This simple but elegant Python program (with a companion JavaScript/HTML version)
  produces an infinite, ever-changing poem by selecting randomly from lists of
  nouns, verbs, and adjectives. Its clean, accessible code has inspired dozens of
  adaptations—from Scott Rettberg's Tokyo Garage to J.R. Carpenter's gastronomic
  Gorge—making it one of electronic literature's most generative (in every sense)
  works. This recipe guides you through making your own Taroko Gorge variation by
  substituting your own themed word lists into Nick's original code.
genres:
  - Generative Poetry
difficulty_pans: 2
yields: An infinite, ever-changing poem that runs continuously, producing new lines of verse with each cycle.
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/gorgeous-taroko-gorges.md  
---
# Gorgeous Taroko Gorges

**Chef:** Mark C. Marino (h/t to Nick Montfort)
**Affiliation: USC **

**Class of E-lit: Poetry Generators**
**Dish: An infinite poetry generator**
**Required Ingredients: Python or Javascript, a theme, lists of words**
**Preparation and Cooking Time: 20 minutes**
**Number of Servings and Serving Size: one infinite poem**
**Rating:** 🍳🍳 medium

## From the Chef: 
Of course, credit for this goes to Nick Montfort, but with his permission I offer this lovely recipe.

## Background:
On a Taiwan and Eva Air flight in January of 2009, Nick Montfort coded this simple but elegant python poetry generator. He would publish the code, as he would all of his projects, free and open source, ready to be modified. Eventually, he would create a web-friendly Javascript version. That version would be adapted by his friend and former-Grand Text Auto co-blogger, Scott Rettberg, who would make Tokyo Garage, an act that in some ways inspires this entire collection. Scott took Nick's code and replaced all the data with his own, keeping the T and the G of Nick's title, and then repopulating the piece with pop-culture detritus with a Japanese flavor. 

That simple adaptation would inspire countless chefs to remake the piece, following their own inspiration. There were Takei, Geroge (with a Star Treok them), Fred and Geoge (with a Harry Potter Theme), and even the meta-remix Argot Ogre, Ok! by Andrew Plotkin, which remixes both the words and the code of the piece. One of the first adapations, J.R. Carpenter's Gorge, offers a gastronomic theme.

## Sample Before You Cook:
A dive into Taroko Gorge, would not be complete without a look at the piece and some of its adaptations.  You can see a full list here: [Taroko Gorge and variations] (https://nickm.com/poems/taroko_gorge/)


## Category: Poetry Generator

## Recipe

## Ingredients:
* Nick's starter code
* Editor
* Theme
* List of words

## Directions:
To make this infinite poetry generator, it helps if you first choose a theme. What would you like to see an infinite meditation on? Nick's original work took the bucolic and eponymous Taroko Gorge.  Later variations took everything from pop-culture detritus to fandom (more pop-culture detritus). But wait, there was also the substance of our appetites (Gorge) and the toys of our childhood. 

Next, you may want to make some lists. 
Above (nouns)  for list a
Below (nouns)   for list b
Trans (transitive verbs) for list beginning with "track"
imper (imperative verbs ) for list beginning with "command"
texture (adjectives)  for list j
encompassing (adjective) for list x

monkey (a noun that appears rarely) for where you see monkey
monkey trigger (the first letter of the word from "above" that causes monkey to appear): you'll see that is currently set to f. 


Now insert those lists into the code below in list label above. 

## Starter Code:

We're going to use the original here, even though the HTML is a little easier to read and replace. 

```python
#!/usr/bin/env python
#
# Taroko Gorge
#  A one-page Python program to generate an unbounded poem
#
# Nick Montfort
#  8 January 2009, Taroko Gorge National Park, Taiwan and Eva Air Flight 28
#
# Copyright (c) 2009 Nick Montfort <nickm@nickm.com>
#
# Copying and distribution of this file, with or without modification, are
# permitted in any medium without royalty provided the copyright notice and
# this notice are preserved. This file is offered as-is, without any warranty.
#
# Updated 31 May 2018, changed "print" for Python 2 & 3 compatibility
# Updated 26 November 2018, substituted a shorter all-permissive license
#
# x() splits a string into a list      c() is just random.choice()
# f() picks a fresh value from a list  p() prints a line and pauses
# cave() -- walking through the tunnels carved in the mountains
# path() -- walking along outdoors, seeing what is above (a) and below (b)
# site() -- stopping at a platform or viewing area

import time,random,sys
def x(s): return s.split(',')
def c(l): return random.choice(l)
#Above and below go here (columns a and b)
a=x('brow,mist,shape,layer,the crag,stone,forest,height')
b=x('flow,basin,shape,vein,rippling,stone,cove,rock')

def f(v):
    l=globals()[v]
    i=c(l[:-1])
    l.remove(i)
    globals()[v]=l+[i]
    return i

def p(s=''):
    print(s.capitalize())
    sys.stdout.flush()
    time.sleep(1.2)

def cave():
# texture (column f) goes here
# encompassing (column g) goes below
    j=['encompassing',c(x('rough,fine'))]+\
    x('sinuous,straight,objective,arched,cool,clear,dim,driven')
    t=c([1,2,3,4])
    while len(j)>t:
        j.remove(c(j))
# imperative verbs here
    v=' '+c(x('track,shade,translate,stamp,progress through,direct,run,enter'))
    return v+' the '+' '.join(j)

def path():
 # transitive verbs here (column c)
    v=c(x('command,pace,roam,trail,frame,sweep,exercise,range'))
    u=f('a')
    if c([0,1]):
        if u[0]=='f':
         u=c([u,u,'monkey'])
        h=u+'s '+v
    else:
        h=u+' '+v+'s'
    return h+' the '+f('b')+c(x(',s'))

def site():
# intransitive verb here (column e)
    return f(c(x('a,b')))+'s '+c(x('linger,dwell,rest,relax,hold,dream,hum'))

p()
while True:
    p(path()+'.')
    m=c([0]*6+[1,2])
    for n in range(0,m):
        p(site()+'.')
    p(path()+'.')
    p()
    p(cave()+' --')
    p()
```

You can test out your code in an online python 3 editor.

## HTML version

Many people find it easier just to make your swap-ins using the HTML

```html

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<!--

Nick Montfort
 Original Python program:
 8 January 2009, Taroko Gorge National Park, Taiwan and Eva Air Flight 28

Copyright (c) 2009 Nick Montfort <nickm@nickm.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

-->
<style type="text/css">
/* <![CDATA[ */
body {
 background: #062;
 color: #dad;
 margin: 0 24pt 0 24pt;
 font-family: Optima, sans-serif;
 font-size: 13pt;
}
div {
 height: 16pt;
}
a {
 color: #117;
 text-decoration: none;
}
/* ]]> */
</style>
<script language="JavaScript" type="text/javascript">
var t=0;
var n=0;
var paths=0;
var above='brow,mist,shape,layer,the crag,stone,forest,height'.split(',');
var below='flow,basin,shape,vein,rippling,stone,cove,rock'.split(',');
var trans='command,pace,roam,trail,frame,sweep,exercise,range'.split(',');
var imper='track,shade,translate,stamp,progress through,direct,run,enter';
imper=imper.split(',');
var intrans='linger,dwell,rest,relax,hold,dream,hum'.split(',');
var s='s,'.split(',');
var texture='rough,fine'.split(',');
function rand_range(max) {
 return Math.floor(Math.random()*(max+1));
}
function choose(array) {
 return array[rand_range(array.length-1)];
}
function path() {
 var p=rand_range(1);
 var words=choose(above);
 if ((words=='forest')&&(rand_range(3)==1)) {
  words='monkeys '+choose(trans);
 } else {
  words+=s[p]+' '+choose(trans)+s[(p+1)%2];
 }
 words+=' the '+choose(below)+choose(s)+'.';
 return words;
}
function site() {
 var words='';
 if (rand_range(2)==1) {
  words+=choose(above);
 } else {
  words+=choose(below);
 }
 words+='s '+choose(intrans)+'.';
 return words;
}
function cave() {
 var adjs=('encompassing,'+choose(texture)+',sinuous,straight,objective,arched,cool,clear,dim,driven').split(',');
 var target=1+rand_range(3);
 while (adjs.length>target) {
  adjs.splice(rand_range(adjs.length),1);
  }
 var words='\u00a0\u00a0'+choose(imper)+' the '+adjs.join(' ')+' \u2014';
 return words;
}
function do_line() {
 var main=document.getElementById('main');
 if (t<=25) {
  t+=1;
 } else {
  main.removeChild(document.getElementById('main').firstChild);
 }
 if (n===0) {
  text=' ';
 } else if (n==1) {
  paths=2+rand_range(2);
  text=path();
 } else if (n<paths) {
  text=site();
 } else if (n==paths) {
  text=path();
 } else if (n==paths+1) {
  text=' ';
 } else if (n==paths+2) {
  text=cave();
 } else {
  text=' ';
  n=0;
 }
 n+=1;
 text=text.substring(0,1).toUpperCase()+text.substring(1,text.length);
 last=document.createElement('div');
 last.appendChild(document.createTextNode(text));
 main.appendChild(last);
}
function poem() {
 setInterval(do_line, 1200);
}
</script>
  <title>Taroko Gorge</title>
</head>
<body onload="poem()">
<div style="float:right; margin-top:12px; color:#0b3; height:60pt">
<div>Taroko Gorge</div>
<div><a href="http://nickm.com">Nick Montfort</a></div>
</div>
<div id="main"></div>
</body>
</html>
```




## Notes:

## Variations:
Of course, every Taroko Gorge is a variation, but here are a few more ideas:
Change the pacing
Change the poetic form (haikus, sonnetts)
Change the context (a dialogue, a speech)

## Related Recipes:
Literary Dish Generator

## References:
Chapter 7 of Critical Code Studies.
Output by Nick Montfort and Lillian-Yvonne Bertram
