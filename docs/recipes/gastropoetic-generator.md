---
title: Gastropoetic Generator
chef: Talan Memmott, Scott Rettberg
abstract: A limerick-form poetry generator that produces menus for real in-person feasts, blending constraint-based poetics with culinary performance.
description: >
   Write a description in under 250 words. 
genres:
  - Generative Poetry
  - Performance/Experience
difficulty_pans: 2
yields: >
  Write 50 words or less yields
github_link: (https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/gastropoetic-generator.md?plain=1)
---

# **Gastropoetic Generator**

Talan Memmott and Scott Rettberg

**Talan Memmott**  
Associate Professor of Digital Media & Culture, Department of Mass Communication  
Winona State University, Winona, MN, USA

**Scott Rettberg**  
Professor of Digital Culture; Director, Center for Digital Narrative  
University of Bergen

**Class of E-lit:** Culinary Text Generators  
**Dish:** A bespoke formal poetry generator that produces poems that are also menus and result in an in-person feast and online cooking show.  
**Required ingredients:** Computer or phone. Culinary instinct. Code editor. Locally sourced ingredients. Social networks and/or online video services (optional). A well-equipped kitchen.  
**Preparation and cooking time:** 1 hour-2 weeks (coding) \+ variable cooking time  
**Number of servings and serving size:** 1 generator that results in a 3-4 course menu, serves 1-8 diners  
**Rating:** 🍳🍳 two pans, medium

## **From the Chefs**

This sample recipe emerges from our gastropoetic collaborations on *The Limerick Diet* (2019) and *Quarantine Quatrains* (2020), where we discovered that constraint-based poetry generation could produce not only aesthetically pleasing verse, but actually delicious edible results. The project arose from a series of conversations we had over many years about the relationship between cooking and creating different sorts of poetry and narrative generation electronic literature projects. We both love to write experimental electronic literature and love to cook, so it was natural to bring those passions together. Our challenge wasn't to create a parody of a meal, but to use constraints—such the limerick form, locally-sourced ingredients, limited kitchen apparatus—as generative forces that result in genuinely novel culinary experiences.

Limericks are a classic poetic form that bends towards the comic, such as the evergreen classic:

There was a young man of Nantucket.

Who went down a well in a bucket;

The last words he spoke.

Before the rope broke,

Were, "Arsehole, you bugger, and suck it.

We found that limericks, with their AABBA rhyme structure and anapestic trimeter (a metrical foot with two unstressed syllables followed by one stressed syllable, e.g. da-da-DUM | da-da-DUM | da-da-DUM), provide an ideal framework for recipe generation. The short five-line format forces concision while the rhythmic constraints complement the recipe format, providing  scansion for the mise en place. As we bragged: “The meats served will be more Celtic and more tender than the meat of any ancient body found leathering in a bog”—hyperbolic perhaps, depending upon the sear, but the constraint-driven approach did produce surprisingly mouth-watering results.

This recipe will teach you to build your own simplified limerick diet generator, capable of producing a dish in verse form. Because of the limited space available, we will demonstrate only one course. Treat it as both a technical exercise and an extensible culinary adventure.

## **Directions**

1. **Plan your poetic structure:** On a sheet of paper or spreadsheet, create columns for your limerick components. Remember that lines 1, 2, and 5 should consist of three anapests each, while lines 3 and 4 are shorter with two anapests. Think in terms of a slot-style poetry generator, where you can substitute elements such as nouns, verbs, adjectives, etc. within a templated structure, and plan rhyming ingredients accordingly to suit the grammar. The structure itself can be varied and therefore able to produce a series of different rhyme schemes within the controlled structure.  
2. **Build your culinary vocabulary:** Focus on locally sourced, sustainable ingredients. As we emphasized in *The Limerick Diet*, the vocabulary that builds the menu should “spring from the peaty sod of the Irish soil and taste of the salts of the wild Irish sea”—or whatever your local terroir provides. Provide variables including:  
   * **Protein**  
   * **Method**  
   * **Vegetable**  
   * **Sauce**  
   * **Seasonings**  
3. **Account for dietary restrictions:** The algorithm should take guests' dietary restrictions into account as a variable. Create separate arrays for omnivore, vegetarian, and pescatarian options for the appetizers and main course.  
4. **Set up your generator:** Copy the code below into a code or text editor (Sublime, BBedit, Atom, VS code, really any basic editor will do) replacing our sample arrays with your locally-sourced vocabulary of ingredients and preparations. Also try substituting the rhymes in the rh arrays, being to sure to rhyme the end words.  
5. **Don’t be afraid to include fudge in your recipe:** While *The Limerick Diet* always results in tasty meals, the limericks themselves sometimes take short cuts on false rhymes and undisciplined scansion (mushrooms can rhyme with zoom zoom). This adds to comic effect, while also prioritizing quality cuisine over poetic mastery.  
6. **Provide substitutions:** Include fallback ingredients for users for when primary choices aren't available (e.g., “Filet Mignon \> Ground Beef \> Kidney Beans” or “Heirloom Tomatoes \> Canned Tomatoes \> Stolen McDonald's Ketchup Packets”).  
7. **Test rigorously:** Try it out by saving your modified version as a web page (with a file name ending in .html) and opening it in your browser. Remember, as we stated in our original project description, “our intent is not to produce a generative performance that results in poorly produced food.” Test many possible combinations your algorithm might generate by reloading the generator rigorously. Cook representative sample meals to ensure edibility and optimize ROI for diners.  
8. **Draw a menu and prepare:** While it is entirely possible to generate a menu and then immediately prepare it, that would require having all of the possible ingredients on hand, increasing costs considerably. For our performances, we generated a menu live, giving diners opportunities to reload the generators several times in the process of selecting the dishes. Then shop for all necessary ingredients, find the best available kitchen, and be sure that all necessary equipment is available. Also take care in your wine selections, as quality libations enhance the gastronomic experience.  
9. **Implement the performance layer:** Consider how this will be presented—will it be a live cooking show format? A distributed cooking experience? Plan your streaming and documentation accordingly. Then turn on your cameras and start cooking. 

## **Starter Code: (Based on *The Limerick Diet)***

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>LIMERICK DIET: MAIN COURSE GENERATOR</title>:
  <style>
    body { background: #06380e; text-transform: capitalize; margin: 0; padding: 0; }
    a { color: #690000; text-decoration: underline; }
    .menu, .coursename, .captions { font-family: serif; text-align: center; width: 80%; margin: 0 auto; }
    .menu { color: #486828; font-size: 32px; font-weight: bold; font-style: bold; }
    .coursename { color: #000; font-size: 18px; font-weight: bold; text-decoration: underline; }
    .captions { color: #000; font-size: 16px; font-style: italic; }
    .insert { color: #acd187; font-family: serif; text-align: center; font-size: 12px; }
    .details { background: #fdfff0; text-align: center; width: 80%; max-width: 600px; margin: 1em auto; border: 1px solid #660000; padding: 1em; }
  </style>
</head>
<body>
  <div class="details">
    <div class="menu"><a href="#" id="refresh">&#9752; The Limerick Diet &#9752;</a></div>
    <div class="insert">Refresh page for a new menu<br><br></div>
    <div class="captions">&diams; Main Course &diams;<br><br></div>
    <div id="main-course" class="captions"></div>
  </div>
  <script>
  (function(){
    var rnd = function(a){ return a[Math.floor(Math.random() * a.length)]; },
        pro = ["Lamb","Fowl","Pork","Beef","Tofu"],
        nameArr = ["Supreme","ala King","du Monde","Blarney","Parisienne","Zamboni","Alaska","Deconstructed","de Rigeur","Napoleon","Uprising","Wellington","Wilde","Godot","Finnegan","O'Kerry","O'Sullivan","Maguire","Laure-Ryan"],
        met = ["Braised","Sautéed","Pan-Roasted","Broiled"],
        veg = ["Puréed Parsnips","Broccoli","Onions","Edamame","Beans"],
        sauce = ["Red Wine Sauce","Creme Sauce","Mustard Sauce","Anchovy Sauce","Vodka Sauce","Avocado Sauce","Tomato Sauce","Au Jus"],
        herb = ["Rosemary","Oregano","Cumin","Garlic","Nutmeg","Cayenne","Cinnamon","Horseradish"],
        actors = ["an old man","an old woman","a young lady","a drunk poet","a sous chef","an Oulipian","a theologian","a programmer","a professor","a gourmand","a plate-licker","a trencherman","a bloody butcher","a mystic"],
        rh = {
          cork: ["historic","loved by Bjørk","served on a fork","fit for a dork","fed to Orcs"],
          dingle: ["makes you tingle","intertwingled","multilingual","'tis not for singles","served on a shingle"],
          galway: ["that's all fair play","is made in the French way","will all sway","is just as always","clears a grey day","makes all gay"],
          dublin: ["is all a'bubblin'","can silence the mumblin'","won't leave you grumblin'","is quite humblin'","sends Michelin stars all a'tumblin'"],
          belfast: ["calls forth the past","is built to last","can satisfy a belle vast","packs a flavorful blast","will make your hunger hold fast","brings out the whole cast"],
          kells: ["gives off the best smells","rings all bells","truly excels","really jells","dropped like bombshells","is without parallels","is favored by mademoiselles"]
        },
        ing = {
          "Hot Peppers": ["To revive a leper","Lock-pop like a stepper","Diced up by the prepper","Spliced in like striped zebras","Tossed in like warm zephyrs"],
          "Pop Rocks": ["WOOT WOOT! like shock jocks","Like wearing clown socks","To stop cuckoo clocks","More disco than sock hop","To bust all your crock pots","That taste is just top notch"],
          Mushrooms: ["No need for brush brooms","To sate all lush grooms","Served in plush rooms","For sure to crush gloom","The flavors will KABOOM!","Whizbang and zoom zoom"],
          "Red Beets": ["You'll leap from your seats","SWEET SHEEP! You will bleat","Blood-red candied treats","They compliment the best meats","The nature-lover's best sweets","As loved by aesthetes","To quicken up your heartbeats","Healthy snacks for athletes"]
        },
        st = {
          cork: function(m,p,h,v){ return ["<br>Don't miss the "+m+" "+p+" in Cork<br><br><span class=menu>&#9752;</span><br>", "<br>The tasty "+p+" and "+v+" of Cork<br><br><span class=menu>&#9752;</span><br>"]; },
          dingle: function(m,p,h,v){ return ["<br>Don't miss the "+h+"-crusted "+p+" in Dingle<br><br><span class=menu>&#9752;</span><br>", "<br>The extravagant "+m+"  "+p+" with "+h+" "+v+" of Dingle<br><br><span class=menu>&#9752;</span><br>"]; },
          galway: function(m,p,h,v){ return ["<br>Don't miss the "+m+" "+h+" "+p+" of Galway<br><br><span class=menu>&#9752;</span><br>", "<br>Oh! the "+m+" "+p+" with "+v+" of Galway<br><br><span class=menu>&#9752;</span><br>"]; },
          dublin: function(m,p,h,v){ return ["<br>Don't miss the "+p+" and "+v+" in Dublin<br><br><span class=menu>&#9752;</span><br>", "<br>Superb "+h+" "+p+" with "+v+" in Dublin<br><br><span class=menu>&#9752;</span><br>"]; },
          belfast: function(m,p,h,v){ return ["<br>Pipes are calling for the "+h+" "+m+" "+p+" of Belfast<br><br><span class=menu>&#9752;</span><br>","<br>Man! the "+m+"  "+p+" of Belfast<br><br><span class=menu>&#9752;</span><br>"]; },
          kells: function(m,p,h,v){ return ["<br>Hearts swell for the "+m+" "+p+" and "+v+" of Kells<br><br><span class=menu>&#9752;</span></br>", "<br>Salivate for the "+m+" "+p+" and "+v+" of Kells<br><br><span class=menu>&#9752;</span><br>"]; }
        },
        templates = [];
    for (var loc in rh) {
      (function(loc) {
        var cap = loc.charAt(0).toUpperCase() + loc.slice(1);
        templates.push(function() {
          var p = rnd(pro), nm = rnd(nameArr), mth = rnd(met), h = rnd(herb), v = rnd(veg), s = rnd(sauce),
              a = rnd(actors), L = rnd(rh[loc]), k = rnd(Object.keys(ing)), I = rnd(ing[k]), stg = rnd(st[loc](mth,p,h,v));
          return '<span class="coursename">' + cap + ' ' + p + ' ' + nm + '</span></br></br>' +
                 'There was ' + a + ' from ' + cap + '<br>' +
                 'Whose ' + h + '-' + s + ' ' + L + '<br>' +
                 'So many ' + k + '<br>' + I + stg;
        });
      })(loc);
    }


    function render() {
      var tpl = rnd(templates);
      document.getElementById('main-course').innerHTML = tpl();
    }


    function init() {
      render();
      document.getElementById('refresh').addEventListener('click', function(e) {
        e.preventDefault();
        render();
      });
    }


    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  })();
  </script>
</body>
</html>
```

Sample Dishes:

**Dublin Lamb Parisienne**

There was an Oulipian from Dublin  
Whose Horseradish-Avocado Sauce sends Michelin stars all a'tumblin'  
So many Pop Rocks  
That taste is just top notch  
Don't miss the Lamb and Onions in Dublin

**Kells Pork Wilde**

There was a young lady from Kells  
Whose Cumin-Red Wine Sauce rings all bells  
So many Pop Rocks  
Like wearing clown socks  
Hearts swell for the Pan-Roasted Pork and Edamame of Kells

**Galway Tofu Wellington**

There was a gourmand from Galway  
Whose Rosemary-Anchovy Sauce is made in the French way  
So many Mushrooms  
Whizbang and zoom zoom  
Oh\! the Pan-Roasted Tofu with Beans of Galway

## **Variations**

**For intimate gatherings (*Limerick Diet* model):**

* Generate menu in real-time during cooking performance  
* Stream live with commentary from an "obtrusive cooking show host"  
* Serve to select group of 8 diners maximum  
* Emphasize quality control and artisanal presentation

**For distributed events (*Quarantine Quatrains* model):**

* Generate standardized menus in advance  
* Allow participants to cook at home simultaneously  
* Create "moveable feast" across time zones  
* Encourage social media documentation with event hashtags

**Advanced modifications:**

* Use more complex forms (such as sonnets or sestinas) for more complex dishes  
* Integrate a cocktail game and/or wine pairing algorithms  
* Integrate with shopping list generators  
* Create review generators for post-meal critique

Consider culture-specific adaptations: haiku-based sushi preparation, sonnet-structured pasta courses, or ghazal-inspired curry spice combinations. The fundamental insight—that constraint-based generation can produce both artistic and practical value—opens possibilities far beyond our initial limerick experiments. Gastropoetics brings together poetry, the culinary arts, and performance and results in unique cultural experiences your diners will treasure for years to come.

## **Takeaway**

This recipe relies on several key gastropoetics principles:

* **Constraint-based generation:** The limerick form forces both poetic structure and culinary logic.  
* **Local sourcing:** Vocabulary should reflect available regional and seasonal ingredients. Don’t be *offal*: think hoof to tail\!   
* **Collective performance:** Participants should share their interpretations and variations. The meal and the conversations around it are part of the performance.

The algorithm accommodates dietary restrictions as variables and includes substitution systems for ingredient availability. As we learned from *Quarantine Quatrains*, “each chef will interpret each poem differently”—this is a feature, not a bug. When we performed *Quarantine Quatrains*, with multiple chefs around the world each preparing the same menu, the meals were nevertheless wildly different, highlighting the fact that cooking itself is a generative experience and that chefs interpret recipes just as readers interpret poems.

