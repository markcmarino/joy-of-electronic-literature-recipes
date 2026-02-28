---
title: Queering Bash Love Poems as Recipes
chef: Winnie Soon and Mara Karagianni
abstract: Create electronic poetry using Bash terminal commands that transform code into love letters and feelings.
description: >
  Bash, created in 1989 as the "Bourne Again Shell," is typically used by system administrators for automating tasks, navigating filesystems, and managing servers. But this queer Bash kitchen embraces the poetics of code, exploring how computation can be a site of vulnerability, ambivalence, and creative subversion rather than just efficiency. As tech oligopolies like Amazon Web Services shift administration toward proprietary dashboards and vendor-locked environments, working directly with terminal-based Bash becomes an act of reclaiming hands-on craft. This recipe guides you through creating "Infinite Missing," a simple yet profound love poem where longing builds with each loop—"I miss you so so so much"—growing infinitely through terminal commands. By replacing standard logic terms like "true" with queer variables like "love," the code becomes confession, syntax becomes poetry, and repetition becomes rhythm. The approach draws on principles of elegance, fusion, diversity, fuzziness, separation, and presence to write code that shimmers, meant not just to run but to feel.
genres:
  - Generative Poetry
difficulty_pans: 1
yields: >
  A terminal-based love poem that loops infinitely, each iteration adding layers of longing through expanding text visible in your command line.
github_link: https://git.systerserver.net/systerserver/queering-bash
---

## Ingredients

- A computer with Bash terminal access (Linux, MacOS, or Windows with PowerShell/ports)
- Terminal/console window (Command Line Interface)
- Text editor like `nano` (or `edit` on Windows)
- Basic willingness to embrace feelings and code together

## Method

### Understanding the Bash Kitchen

Bash is a text-based interface where you type commands to instruct your system directly. Unlike Graphical User Interfaces (GUI), the terminal unlocks powerful capabilities often hidden from view.

### Ingredients for a Shimmering Queer Love Poem

**a. Elegance**: Write code that does one thing—and does it poetically. Let algorithms be simple, data structures tender. When lost in logic, lean into queer intuition.

**b. Fusion**: Craft programs that shimmer—written to run, but meant to feel. Let syntax speak as much as it runs.

**c. Diversity**: Let your lines mean more than one thing. Syntax, like love, should resist singular readings.

**d. Fuzziness**: Write with feeling first. Let poetry bloom before compiling.

**e. Separation**: When missing, code a poem for the one not there—let code become a letter.

**f. Presence**: Write for the NOW. Because feelings matter.

### Creating "Infinite Missing"

**Queer Kitchen Ambience**

Open your terminal:
- **Mac**: Open Finder, search for "Terminal.app"
- **Windows**: Search for "PowerShell" in applications

You'll see a command prompt like:
```
queer@joy:~$
```

The name before `@` is your username; after is your machine's name.

**Navigate Your Space**

Commands are built-in keywords for communicating with your machine:
- `pwd` (print working directory): reveals your current location
- `mkdir queerkitchen`: creates a new directory
- `cd queerkitchen`: enters that directory

### Starter Code: Serving Dish - Infinite Missing

The final poem looks like:

```bash
while $love
how="so"
do
  so+="${how} "
  echo I miss you $so much
  sleep 0.2
done
```

### Chopping Together - Step by Step

**Step 1: Create Your Love Letter**

Open a new file in the terminal with `nano`:
```
queer@joy:~$ nano infinite_missing.sh
```

**Step 2: Write Your Feeling**

Inside the file, type:
```bash
echo "I miss you so much"
```

**Step 3: Save the Message**

Press Ctrl/Cmd + X, then type Y, and hit Enter to save and exit.

**Step 4: Read It Aloud (via Bash)**

Back in the terminal, run:
```
queer@joy:~$ bash infinite_missing.sh
```

You'll see your message—simple, direct, like the first line of a love poem.

**Step 5: Make It Linger**

Let's echo this line forever—a loop of longing. Edit the file again:
```
queer@joy:~$ nano infinite_missing.sh
```

Replace the content with:
```bash
while true
do
  echo "I miss you so much"
  sleep 0.2
done
```

Each heartbeat of "missing" now pulses through your terminal (every 0.2 seconds). To stop the loop, press Ctrl + C.

**Step 6: Add Softness and Depth**

Let's stretch the "so" with each repetition:
```bash
while true
do
  so+="so "
  echo I miss you $so much
  sleep 0.2
done
```

Now the longing builds—"so so so much"—growing with every loop, like a feeling that keeps returning, never quite still.

In Bash, variables are called by placing `$` in front of their name. The `+` sign adds to what was already there—each loop appends another "so," layering the sentiment line by line.

**Step 7: Queering Poetics**

Change the loop's logic to something tender:
```bash
love=true
while $love
do
  so+="so "
  echo I miss you $so much
  sleep 0.2
done
```

We begin to rewrite the logic of longing:
- We've assigned the `true` value to something queer—a variable named `love`
- The loop changes from `while true` to `while $love`, but executes the same way

**Step 8: Becoming a Piece of Codework**

Final version:
```bash
while $love
how="so"
do
  so+="${how} "
  echo I miss you $so much
  sleep 0.2
done
```

In Bash, any variable—even if undeclared—evaluates as true in a loop condition (unless assigned to null or empty string). We introduce variable `how` to echo the intensity. Since we want breathing room, we place the variable inside quotes with a space: `"so "`. Bash requires curly brackets `${how}` when referencing a variable inside quotes.

You've replaced `true` with `love`, and incremented longing in a loop. The syntax becomes poetry: repetition as rhythm, code as confession.

## Notes

### Variations and Related Recipes

Compose your own language poem by replacing variable names and crafting output text.

**Examples:**
1. Change `while $love` to `while $hot`
2. Change `echo I miss you $so much` to `echo I want you $so badly`

See other dishes cooked in the Queer Bash Kitchen: https://git.systerserver.net/systerserver/queering-bash

### Understanding the Changing Kitchen

The tech landscape is shifting from terminal-based system administration (where administrators work with Bash recipes, piping one into another, acquiring deep knowledge of filesystems and networks) to cloud-based environments (where administrators click through web pages in vendor-locked infrastructures).

This queer Bash kitchen resists that shift, highlighting computation's potential not just as a tool of efficiency, but as a site for vulnerability, creative, and culinary subversion.

### Queering as Practice

"Queering is, thus, understood as specific appearance, gathering, performing, as a disturbance of order." (Götz 18)

"[Q]ueer spaces per se do not exist, neither do queer things - it is their use that makes them potentially queer spaces of things" (Götz 18)

### References

- Charm. *Charm: We Make the Command Line Glamorous*. https://charm.sh/
- Götz, Magdalena. "Queering Practices: Uses of Digital Mobile Media in Queer/Feminist Art." *CRC Media of Cooperation Working Paper Series*, no. 18, 2021, pp. 15–22.
- Kaldrack, Irina, and Martina Leeker. "Introduction." *There Is No Software, There Are Just Services*, edited by Irina Kaldrack and Martina Leeker, meson press, 2015, pp. 9–19.
- Raymond, Eric Steven. *The Art of Unix Programming*. Addison-Wesley Professional, 2003.
- Soon, Winnie, and Mara Karagianni. *Queering Love Letters* [Slide deck]. HackMD, 2023. https://hackmd.io/@siusoon/queeringbash2
