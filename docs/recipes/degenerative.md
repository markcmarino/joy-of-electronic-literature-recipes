---
title: Degenerative
chef: Eugenio Tisselli
abstract: Create a web page that degenerates with each visit through PHP-driven character deletion and replacement.
description: |
  Every time someone visits this page, one character that makes up the HTML code gets either deleted or replaced, causing step-by-step degeneration of both content and structure. Programmed and launched in 2005, this de-generative language art piece was created as a counterpoint to the then-popular generative art movement. Inspired by Gustav Metzger's Auto-Destructive Art Manifesto (1959), which encouraged using perishable or unstable materials that degrade naturally or through human intervention, degenerative parodies what Metzger saw as industrial societies' "obsession with destruction." The work aesthetically demonstrates the power of societies to "accelerate disintegrative processes." Beyond its raw nihilism, degenerative has provoked interesting critical thoughts. Justin Berner found it confronts readers with technical obsolescence, critiquing unopposed instrumentality in fields like digital humanities and technosolutionism. Because degenerative reveals underlying code through a subtractive process triggered by readers, the irreversible descent into textual formlessness foregrounds material effects of collective action on a medium that conceals materiality through seemingly immaterial interfaces. The work reminds us of the fragility of our collective online spaces.
genres:
  - Generative Poetry
custom_genres:
  - Code Art
  - Web Page Deformation
difficulty_pans: 2
yields: |
  A web page that slowly degenerates into unreadability through collective visitor interaction, revealing code and structure progressively.
github_link: http://motorhueso.net/degenerative
---

## Ingredients

- A plain text editor (such as Leafpad on Linux, or any text editor)
- Access to a remote or local web server with PHP support
- Basic understanding of HTML and PHP

## Method

### Understanding the Concept

When readers open the degenerative web page, a PHP script:
1. Reads an HTML file (A)
2. Destroys a fragment of A by replacing or deleting one character
3. Saves the altered content
4. Displays the result to the reader

All of this happens on the web server. The destruction is cumulative—each visit degrades the page further.

### Understanding PHP and Servers

**Servers:** Computers that fulfill users' internet requests. In the ancient World Wide Web, servers delivered mostly static HTML pages. As demands for personalized content increased, dynamic web pages emerged.

**PHP (Hypertext Pre-Processor):** A language that carries out server-side data processing. Yes, many programmers avoid PHP—it feels patchy, like it was designed by a gang of crazy monkeys, each with its own idea of how the language should look. But PHP has been around for 30 years, and it's perfect for degenerative!

### Creating the Degenerative Code

The code is divided into two files:
- **File A:** The original HTML code and text of the degenerative web page
- **File B:** The PHP code that executes the degeneration

### Step 1: Create File A (The HTML Content)

Open a simple text editor and type this example:

```html
<!DOCTYPE html>
<html>
<head>
<title>degenerative</title>
</head>
<body bgcolor="#000000" text="#999999">
<p align="center"><strong><font size="5" face="Arial, Helvetica, sans-serif">Your text here</font></strong></p>
</body>
</html>
```

Save the file as `A.txt`. File A can include whatever you want, as long as its contents are composed exclusively of HTML tags and text.

### Step 2: Create File B (The PHP Degeneration Code)

Create a new file with the following PHP code:

```php
<?php
$modify = "A.txt";
$fd = fopen($modify,"r"); // open file A.txt
$pgdata = fread($fd, filesize($modify)); // store file contents in $pgdata
fclose($fd); // close file

// These four lines read contents of file A and store in $pgdata

$j = strlen($pgdata)-1; // contains the length of file A
$k = strpos($pgdata,"<body");
$k = strpos($pgdata,">",$k)+2; // position after the <body> tag

$charlist = array("*","_","-",""," "); // characters used for degeneration
$c = $charlist[rand(0,sizeof($charlist))]; // choose one at random

$destrukt = rand($k,$j); // randomly choose a character to degenerate

$pgdata = substr($pgdata,0,$destrukt-1).$c.substr($pgdata,$destrukt,($j-$destrukt+1));
// reconstruct the original text of file A with the degenerated character

unlink($modify); // delete the previous version of file A

$fc = fopen($modify,"w+");
fwrite($fc,$pgdata);
fclose($fc);
// these lines write the new version of A with degenerated text

echo($pgdata); // output the resulting text for the user to read
?>
```

**Note:** Don't type the explanatory comments into the editor, or you'll get error messages when executing the code!

Save this file as `B.php`. This file should be in the same folder as `A.txt`.

### Step 3: Understanding What the Code Does

**Variables $j and $k:**
- `$pgdata` contains entire text of A
- `$j` points to the last character
- `$k` points to position just after the ">" character of the `<body>` tag

**Character list:**
- `$charlist` contains possible characters for degeneration: `"*"`, `"_"`, `"-"`, `""` (empty), `" "` (space)
- Note that the list includes the empty character
- One character is randomly chosen and stored in `$c`

**The destruction variable:**
- `$destrukt` is assigned a random numerical value between `$k` and `$j`
- This chooses a random position within the text string
- Position can be anywhere between the `<body>` tag and the end of text (to respect HTML code before it)

**The dirty deed:**
- The character in `$c` is inserted at the position stored in `$destrukt`
- This is achieved by splitting the `$pgdata` text string into two parts: before and after the desired position
- The character in `$c` joins the parts
- Result: new `$pgdata` with text degenerated by substituting/destroying the character originally at `$destrukt` position

### Step 4: Deploy Your Degenerative Page

**Remote Server:**
- Upload both files to the same folder on your remote server
- Access `B.php` at the corresponding URL (e.g., `https://myserver.net/b.php`)

**Local Server:**
- Use XAMPP (https://www.apachefriends.org/) or similar local server designed for PHP development
- Save files to appropriate folder on your computer
- Open `B.php` from your web browser

## Notes

### Progressive Degeneration

The initial state shows your original text. With each visit, the page degenerates further. Successive stages show increasing textual breakdown until the page becomes unreadable.

### The Original Message

The original degenerative web page featured this passage:

"One day, all this text will be unreadable. This will happen slowly or quickly, depending on how this page is visited. It will not be a natural decomposition: it will be the effect of code that lies within. Like an unstoppable disease, this code will eventually render the page sick and crippled."

### From the Chef (2025 Reflection)

"As I write this recipe in 2025, twenty years after originally coding degenerative, I can't shake away the feeling that the digital environment is rapidly falling apart. I look around and it seems like an 'unaccommodating, destructive inertia' (that's how Justin Berner described my work!) has taken hold of the online spaces in which both trivial and important aspects and events of our lives play out. It's not a pretty sight, and I just don't know how to make things better anymore. Perhaps it's too late for that, and we'd be better off just by letting go of the digital. I really just don't know. For now, I can only say that we've taken our passion for disruption several apps too far, and that these turbulent times ask of us to maybe cool it down so we can imagine ways of rebuilding things and caring for them, rather than breaking them while we move fast. **Gentle is the new punk.** In that spirit, I hope degenerative will remind us of the fragility of our collective, online spaces."

### Critical Reception

**Justin Berner** found that the piece:
- Confronts readers with technical obsolescence
- Critiques unopposed instrumentality in digital humanities
- Critiques technosolutionism
- Reveals underlying code through subtractive process
- Foregrounds material effects of collective action
- Exposes materiality concealed by seemingly immaterial interfaces and proprietary black boxes

**Diego Zorita Arroyo** proposed that:
- Stretching fragility to breaking point obstructs the formal task of language
- Natural language, upon losing its semantic function, reveals itself purely as "material surface of inscription" devoid of meaning
- Like unmodeled clay, or a sculpture that disfigures itself into nothingness

### Historical Context

**Gustav Metzger's Auto-Destructive Art Manifesto (1959):**
- Encouraged artists to use perishable or unstable materials that degrade naturally or through human intervention
- Purpose: parody industrial societies' "obsession with destruction"
- "Form of public art for industrial societies" aesthetically demonstrating power to "accelerate disintegrative processes"

**Pete Townshend (The Who):**
- One of Metzger's most famous students at Ealing Art College in London
- Mirrored teacher's lessons by enthusiastically bashing his guitar at end of shows

### Technical Resources

- **PHP Documentation:** https://php.net
- **Leafpad (text editor):** http://tarot.freeshell.org/leafpad/
- **XAMPP (local PHP server):** https://www.apachefriends.org/

### References

- Arroyo, Diego Zorita (2022). "Dilemas ontológicos en la demarcación del hecho literario a raíz de Degenerativa (2005) y Regenerativa (2005) de Eugenio Tisselli." In *Formas precarias en las literaturas hispánicas del siglo XXI* (pp. 123-135). Peter Lang.
- Berner, Justin (2020). "Unhelpful Tools: Reexamining the Digital Humanities through Eugenio Tisselli's degenerative and regenerative." *Electronic Book Review*. https://doi.org/10.7273/kbfc-4145
- Metzger, Gustav (1959). "Auto-Destructive Art." http://radicalart.info/destruction/metzger.html
