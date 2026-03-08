---
title: Radical Atmospheres
chef: Andrew Demirjian
abstract: reorganizing archival source texts using regular expressions and NLP to generate poetic material for audio augmented reality experiences.
description: > [Please, write 250 words or less]
genres:
  - Audio
  - Augmented Reality
custom_genres:
  - Audio AR
  - Archival poetics
difficulty_pans: 1
yields: >
 write 50-word or less yields
github_link: (https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/radical-atmospheres.md)
---

						\_\_\_

# Radical Atmospheres \- 

# Poetic Recipes for Audio Augmented Reality

Andrew Demirjian  
Associate Professor (Film & Media / Integrated Media Arts MFA programs)  
Hunter College, City University of New York (CUNY)

**Class of E-lit:** Audio AR   
**Dish:** an approach to reorganizing a source text to reveal patterns for poetic inspiration **Required ingredients:** Computer. Phone. Headphones or earbuds. Code editor. P5.js, RiTa Library  
**Preparation and cooking time:** 20 minutes 

**Number of servings and serving size:** 1 audio experiment

**Rating: 🍳 one pan, easy**

**Background: Archives and Audio Augmented Reality**

Like a food truck serving up delicious bites to throngs of people at lunch time, audio AR (AAR) is about meeting people where they are. Augmented Reality (AR) may be thought of as a new generation of technologically advanced versions of a plaque or memorial, but the impetus for these apps that inscribe physical space may have much deeper roots. In a persuasive article that cites venatic practices of hunters, ancient divination rites, and memory palaces, MIT media theorist William Uricchio, explains, “Whether public, discovery-based, or even personal, augmentation’s inherently dialogic character requires reality for its work. And its work turns on the same semiotic reciprocities that humans have engaged in over the long haul. Technologies will come and go, but humans will continue to mark the world, read it, and find coherence – activities inherent in augmented reality.”[^1] This connection to physical space can create a gravitational pull for e-lit writers working in this medium to explore archival materials and oral histories that connect to a specific place as their source material. Listening to these types of audio AR pieces can create an uncanny feeling of presence/absence, as voices from the past mix with the current moment in the same location. 

	e-lit writers have developed many recipes for working with a corpus as their basic ingredients. Systematic approaches for excerpting, sorting and combining large groups of texts range from web-based pieces like Stephanie Strickland and Nick Montfort’s *Sea and Spar Between* to analog antecedents like Jackson Mac Low’s *Ridiculous in Piccadilly.* For me, the cooking instructions and the meal are both part of the pleasure of the art, like a particularly clever reinterpretation of a delicious classic dish, they delight the mind and body. In an archival context, these computational procedures can produce texts that have a “poetic documentary” feel, as Susan Howe has described her collage-like practice.[^2] 

	Similar to a chef carefully plating a meal, an e-lit author working with AAR needs to think about the location of each component of their dish. What parts pair well with the others, what elements provide contrast, and how do all the parts come together for a unified experience? These spatial considerations are similar to an author working on a kinetic poem planning where elements will go on a two-dimensional screen. However, unlike a screen-based work, the author of an AAR piece must be concerned with elements in the physical world, the language/sound is not only in conversation with the previous track someone listened to, but also the architecture, traffic and people in the environment. How long should a piece be before a listener starts to feel uncomfortable on a street corner? How many sections should be included in a work? Where can people sit down to take a pause? What is the pace for the body to navigate the text and space simultaneously? 

The recipes below were used to create one section of a new work called *Radical Atmospheres: Visions of Liberation/Tactics of Suppression, The Young Lords in East Harlem.* It uses an archival document, ‘Report to the Mayor of New York on the Death of a Citizen, Julio Roldan’ by William J. vanden Heuvel, as its source text. The piece is currently active at the Art Park on East 120th St. between Lexington Ave. and 3rd Ave. if you are in New York City, or virtually navigating it from the link below.    

**Sample before you cook:**

Sheila Heti’s [Alphabetical Diaries](https://www.nytimes.com/interactive/2022/03/23/opinion/sheila-heti-alphabetized-diary-tuv.html?searchResultPosition=2)   
Stephanie Strickland and Nick Montfort’s: Sea and Spar Between [https://nickm.com/montfort\_strickland/sea\_and\_spar\_between/](https://nickm.com/montfort_strickland/sea_and_spar_between/)   
	Andrew Demirjian, Radical Atmospheres  
	[https://rw-app-spaces-speak.surge.sh/](https://rw-app-spaces-speak.surge.sh/) 

Additional Reading:  
Caroline Bergvall, Laynie Browne, et al., eds. *I’ll Drown My Book: Conceptual Writing by Women*

Susan Howe’s, *The Midnight*

William Uricchio, “The Markers, Memories and Meanings Behind Today’s AR”

# Audio AR:

# Recipe: Regular Expressions for Expressive Irregularities 

**From the chef:** *This recipe does not produce a finished dish, but is intended to produce insights or a spoonful of inspiration that can be turned into an al fresco meal. These are two of several different programming routines I use on source texts to help me hear/see it from a fresh perspective. By examining a text outside of its intended use – in this case, as a report to a mayor – this methodology can help you find patterns in the text that may not be as readily apparent when reading in a linear fashion for semantic content. Performing these different ways of slicing and dicing words and phrases helps me get a sense of a distinctive flavors buried within a text. When analyzing the output of these programs and grouping parts that catch the ear/eye into separate containers or bowls, it also allows me to get a sense of what types of ingredients might combine well together.*   
*This code uses Regular Expressions and a JavaScript library called RiTa. Regular Expressions are very useful snippets of code that help you computationally manipulate strings in useful ways – what is cool is that they are programming language agnostic so they work across many different cuisines. RiTa bundles useful computational writing procedures for analyzing and generating texts for JavaScript, to help you creatively manipulate text more easily on the web. The first part of the program below re-orders all of the sentences alphabetically, the lower portion creates a Key Word in Context (KWIC) search and prints it to the canvas on the right side of your code.* 

## Directions 

1. Locate a source text that is of interest to you. Consider texts that have some kind of meaningful connection to the location where the final audio will reside. Something that is over 4000 words will yield best results.     
2. Copy and paste this text into a .txt file if it is not already one. Save this file in a location you’ll remember.   
3. Upload the .txt file to a p5.js sketch using the \+ icon in the upper left corner.   
4. On the index page of the p5 web editor, add the following code: it is a content delivery network (cdn) link that enables us to use the RiTa library. This link may change by the time you are reading this, just go to RiTa’s Github repository for the latest cdn to use.   
      	 \<script src="https://cdn.jsdelivr.net/npm/rita"\>\</script\>  
5. Replace the name next to the loadStrings object of the current text in the code below with your own .txt file title.   
6. Run the code and look at the console, this is where your alphabetically sorted sentences will appear. Copy and paste this into a new document to review when you are ready. I recommend printing it out and stepping away from the kitchen to a cozy place to focus.   
7. Notice patterns in the document. Are there groups of sentences that start with the same words? Is there a pattern in the first few words of these sentences that start to feel oddly poetic or evocative? What words could be erased to open up wider readings and where should the erasure begin? How might you combine this group with other patterns in the text?   
8. If there are words that are particularly evocative or have potential to make interesting phrases and you’d like to see each instance of their use, not just the ones starting a sentence – this program also enables you to do searches for Key Words in Context (KWIC).     
9. A KWIC is a type of concordance, it provides a user designated number of words before and after the key word. Look for the section of code that states RiTa.concordance, just below you’ll see a variable called word, replace the current search term in quotes with yours and then hit the play button.  
10. The last section in the draw() function displays the output to the canvas on the right. If you’d like it printed to the console just uncomment the two console.log lines at the bottom of the code. 

## Starter Code: Hear a Source Text in a New Way 
```javascript
let txt, word;
let sorted
let opts;
function preload(){
    txt = loadStrings('Report to the Mayor.txt')
}
function setup() {
  createCanvas(1000,4000)//increase the second parameter for larger outputs
  textFont("Times New Roman", 10);
  
  let allwords = txt.join("\n")
  allwords.split(/\W+/)
  //The ‘\W+’ is a regular expression (regex) that separate strings if there are one or more characters of white space and places them into an array called allwords 
  let sent = RiTa.sentences(allwords)
  //split text into sentences
  let alphaSent = sent.sort()
  //the .sort() is a string method reorders the sentences by the first letter in the sentence

  for(i=0; i<alphaSent.length;i++){
    console.log(alphaSent[i],'\n');
    //outputs each sentence to the console in alphabetical order with a line break between
  }
    opts = {
    ignoreCase: true,
    ignorePunctuation: true,
    ignoreStopWords: false,
  };//options for the concordance method

RiTa.concordance(txt.join("\n", opts));
  word = "Roldan";//replace the word in quotes with your search term
}
function draw() {
  let kwic = RiTa.kwic(word,8);//the second parameter sets the amount of words before and after the search term
  if (kwic < 1) {
    console.log("no match");
  }
  
  function remove_linebreaks(str) {
    return str.split(/\r?\n|\r/).join(''); //regex to remove line breaks
    }
  
  let tw = textWidth(word) / 2; //this will be used to center the search term
  background(250);
  //the for loop below goes through each found instance of the search term and displays it with the term centered in red
  for (let i = 0; i < kwic.length; i++) {
    let parts = kwic[i].split(word);
    parts = parts.slice(0, 2); //just look at the first two arrays
    let rM = remove_linebreaks(parts[0]);
    let rM2 = remove_linebreaks(parts[1]);

    let x = width / 2,
    y = i * 20 + 75;
    if (y > height - 20) return;
    fill(0);
    textAlign(RIGHT);
    text(rM, x - tw, y);

    fill(200, 0, 0);
    textAlign(CENTER);
    text(word, x, y);

    fill(0);
    textAlign(LEFT);
    text(rM2, x + tw, y);

    // console.log(rM +word + rM2);
    // console.log(" ")
  }
  noLoop();
} 
```

## Notes for turning text to audio: 

1. After whittling down the output to some text excerpts that you found compelling, there are many ways to turn your language to audio. If you are working from audio/video interviews or oral histories, skip down to step 6\.   
2. Using the best microphone you have, record yourself speaking the text. If you record your voice, try to enunciate the words the way you’d like to have people hear them. Salt this to taste, what is right for the atmosphere you are trying to create? Is it a mid-level bureaucrat, a monotone droning professor, are certain phonemes lengthened or shortened?   
3. Alternatively, you can also bring the words/phrases into a text to speech application or website. You can try and emulate a more expressive approach by putting spaces between lines, commas or periods at places where the text to speech app is reading it too quickly.   
4. I often have a particular vocal delivery in mind or cadence, but don’t really like the sound of my voice. If you can relate to this, you can combine steps 2 and 3 with a web app like elevenlabs.io voice changer. You upload the audio you read and find a voice that closely resembles what you are imagining.   
5. If you choose to try the voice changer, I strongly recommend taking time to really craft the voices you are creating carefully. The voice, even an AI one, communicates so many subtle expressions beyond the words. Many of the voices are geared towards corporate or professional situations and can sound off-putting for poetic material. Sometimes I use AI software for making music like Udio to get a vocal delivery that is more expressive or poetic.   
6. A program like Adobe Premiere enables you to transcribe interviews. If you are using an oral history with audio or video recordings, you can do searches to find the text excerpts output from the code above and create a new timeline that features just your selections or export your phrases one at a time.   
7. Check out AAR apps like Echoes, Dreamwaves, Roundware or others and upload your sound files to listen to the piece in your desired location. 

## Variations:

You can export each of your audio phrases individually and have them chosen at random in a particular location when using an application like Roundware if you want an element of chance in your AAR experience. 

Explore RiTa’s other types of language analysis tools to find additional interesting patterns within a text. Consider using the phonetic analysis object RiTa.phone() to look at the sonic content of the source text, with this info, you can find assonance or consonance – similar sounding vowels or consonants within multiple words. RiTa.alliterations() and RiTa.rhymes() may also produce mouthwatering bites. 

## Related Recipes

[^1]:  Uricchio, William. “Augmenting Reality: The Markers, Memories, and Meanings Behind Today’s AR.” In Urban Interfaces: Media, Art and Performance in Public Spaces, edited by Verhoeff, Nanna, Sigrid Merx, and Michiel de Lange. Leonardo Electronic Almanac 22, no. 4 (March 15, 2019).

[^2]:  As quoted by Marjorie Perloff, “Unoriginal Genius: Poetry by Other Means in the New Century.” University of Chicago Press, p.101 
