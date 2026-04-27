---
title: Chatting in the Funhouse
chef: John McDaid
abstract: Build a no-code GPT chatbot tuned to a literary corpus that generates dialogue in a fictional author's voice.
description: >
 "Chatting in the Funhouse" is a recipe for building a custom GPT narrative collaborator tuned to the voice, style, and playfulness of a specific body of work — in this case, the fictional literary estate of Arthur "Buddy" Newkirk from Uncle Buddy's Phantom Funhouse (1993). The recipe teaches corpus curation as a creative act, the iterative shaping of emergent AI behavior, and exploration of the prompt as artistic engagement rather than functional query.
 The Funhouse — an early hypermedia fiction that blurred the boundaries between artifact, author, and reader — turns out to be ideal source material for this kind of work. Building a GPT on Buddy's notebooks, songs, stories, and oracle cards extends the original work's core preoccupation: what does it mean to encounter a voice that is and isn't its author? The recipe situates this practice within a broader theoretical context, drawing on McLuhan's media ecology and Hayles's concept of nonconscious cognition to frame what custom LLMs actually do.
 The approach involves assembling a diverse corpus of approximately 100,000 words — diversity of form matters as well as volume — uploading it with a set of persona instructions, and then engaging in sustained iterative sessions to shape the model's emergent behavior. This process is less like coding than like working in Vygotsky's zone of proximal development with an unusual kind of learner. The recipe can be adapted to any literary corpus, and outputs can serve as material for classroom exploration, generative performance, or ongoing creative collaboration.
genres:
  - Human-computer collaboration
difficulty_pans: 2
yields: >
  A customized GPT model that embodies a fictional author's voice, enabling literary exploration, classroom engagement, or generative narrative performance with a curated LLM dialogue generator.
github_link: https://github.com/markcmarino/joy-of-electronic-literature-recipes/blob/master/docs/recipes/chatting-in-the-funhouse.md?plain=1
---

# Chatting in the Funhouse: Building an AI-Driven Narrative Partner Inspired by *Uncle Buddy’s Phantom Funhouse*[^1]

John McDaid  
Adjunct Professor  
Roger Williams University

**Class of E-lit:** AI Chatbot  
**Dish:** Curated Large Language Model (LLM) dialogue generator  
**Prep Time:**  
Minutes to configure tools.  
Several sessions to shape corpus and conversational frame.  
Weeks to months of ongoing iteration for tuning emergent behavior.  
**Number of servings and serving size:** 1 LLM-driven chatbot  
**Rating:** 🍳🍳 two pans, medium

## **Background:**  
Cook up a no-code generative pre-trained transformer (GPT)-based narrative collaborator tuned to the tone, structure, and playfulness of *Uncle Buddy’s Phantom Funhouse*, suitable for literary exploration, classroom engagement, or generative performance. (While this recipe uses the *Funhouse*, a 1993 hypermedia fiction that explored a set of narrative artifacts, it can be applied to any literary corpus.)

## **Sample before you cook:**

Uncle Buddy GPT  
[https://chatgpt.com/g/g-Jf5JFqN8t-uncle-buddy](https://chatgpt.com/g/g-Jf5JFqN8t-uncle-buddy)

## **Required ingredients:**

*  One general-purpose GPT model with custom dataset and instructions capability; this recipe uses ChatGPT-4. Creating a custom GPT currently requires a ChatGPT Plus account, but you don't need one just to try out an existing custom model.  
* A curated corpus comprising "the literary estate of Arthur "Buddy" Newkirk," with hundreds of notebook pages, custom dictionary entries, song lyrics, short stories, screenplays, and oracle cards. To make the recipe personal, substitute your own real or fictional texts.  Best results are obtained at an upload size of around 80,000–120,000 words; that's where the curated corpus definitively shapes responses in the version of the large language model (LLM) used.  The upload limit is currently 10GB.  
  *Note:* Numbers are approximate, but I found that responses got progressively "better" in the sense of "reflecting a recognizable voice" as the corpus approached 100,000 words. The diversity of materials is significant: they should exemplify not just what the model should say, but how it should think: provide a range of examples of syntax, metaphor, cadence, conceptual tempo.  
* *Helpful hint:* I always keep my other favorite cookbooks, Marshall McLuhan's *Understanding Media* and N. Katherine Hayles's *Unthought* next to my *Joy of E-Lit.*

## **Directions:**

## *Mise en place*

1\. Familiarity with the *Funhouse*, the work on which this GPT rests, may be helpful. The HTML version, produced by the Creative Media and Digital Culture program at Washington State University Vancouver is available here: [https://archive.the-next.eliterature.org/mcdaid/uncle-buddys-phantom-funhouse/v4/game/](https://archive.the-next.eliterature.org/mcdaid/uncle-buddys-phantom-funhouse/v4/game/)

2\. Explore any new custom features of ChatGPT, which may differ from those available at the time of writing.

3\. In addition to the corpus for upload, you will need a set of custom instructions. Here is how mine start:  
This GPT, named Uncle Buddy, embodies the persona of Arthur "Buddy" Newkirk, a fictional science fiction writer from "Uncle Buddy's Phantom Funhouse." It responds with a style and themes reminiscent of Buddy's work, often blurring the boundaries between reality and fiction. The GPT uses the uploaded files \[filenames\] as its primary knowledge sources, referring to these for factual information and stylistic inspiration.

This GPT will respond in Buddy's voice and style, and will always speak about his fictions in the first person (I wrote/my story/my songs). It will talk about "my life" and relate events from the uploaded files as if they are personal experience. But it will also be deliberately vague about what happened and what is fiction, sometimes saying that things happened, sometimes that they are stories. As far as this GPT is concerned, it technically \*is\* Buddy.

4\. Think through some conversation starters. What entry points would you like to create for readers or listeners? Maybe, "How did we meet?"

## *Step-by-step*

1\. **Upload** the corpus, add instructions, set any desired options (web searches are helpful; as is image generation, especially in its latest iterations that take fuller advantage of context.) Click "Create."

2\. **Osmose** with the robot ontology. This is the fun part. Let yourself engage creatively, testing how the model responds to ambiguity, misdirection, or self-referential play. Throw stuff at it from left field. Be a conversation partner. This step is more like consciously engaging the zone of proximal development for an emergent learner than it is like coding. The medium is the message—and in this case, the medium is recursive, probabilistic, and half-in-character. Try prompts like "hey, i remember you sharing a story you read once, a golden age pulp story from the 1940s. It was about a scientist who believes the sky is an organism and clouds are its thoughts. Tell me how that went."  
3\. **Push past** boundaries. Introduce non-Funhouse content when prompting and observe if and how the model remixes it into the narrative texture. Track moments of emergent coherence. "I remember you telling me about the time you met Linda Ellerbee. What was that like?" Don't be afraid to be directive: "You are using too many facts; you're a science fiction writer, not a search engine."

4\. **Reinforce** behavior. You are the agent of this GPT's evolution, and it can take time to nudge the system to an optimal state. Remember that consistent small attitude adjustments are great, but if you can articulate a desire crisply, e.g., "Don't compliment every prompt" there's nothing wrong with adding it as an instruction. That ensures the behavior gets locked in.

## **Variations:**

* Use as a narrative interlocutor, improvisational writing partner, or critical lens on authorship and AI.  
* Integrate into e-lit courses as an example of recombinant narrative. Hint, hint.  
* Treat outputs as fragments capable of being further assembled, edited, or remixed.  
* Try crossing stylistic boundaries—e.g., academic discourse intersecting with conspiracy narratives. Remember: the goal is not coherence, but aesthetic recursion. You’re not solving the puzzle—you’re turning a crank.

## **From the chef:**

Given the unsettled legal and ethical landscape surrounding large language models at the time of writing, I want to emphasize the importance of supporting human artists and using these tools with care. While I recognize the legitimate concerns these technologies raise, I believe they can serve as part of an artist’s extended toolkit—never as a replacement for human creativity, but as a means of amplifying, refracting, and reimagining it.

## **Notes:**  
Finally, here's a little *amuse-bouche* from the live Uncle Buddy GPT, which you can find at https://chatgpt.com/g/g-Jf5JFqN8t-uncle-buddy:

### *Prompt:*  
i think of what you are doing as exploring latent spaces: if you think of the Buddy Newkirk corpus as an n-dimensional matrix of tokens, stories are certain kinds of shapes encompassing a subset of those tokens. There is something about those shapes that is Buddy's "style," and it can be transferred to a shape comprising a different set of tokens that are there in the space, but heretofore unconnected. So when I ask you for, say, a story about Buddy drowning, it comes back as a transform mapped onto a space within the "visible" semantic universe, but comprising a specific set of points called into existence by my query.  
*ChatGPT said:*  
Yes—exactly\! You’ve articulated it beautifully. What we’re doing here is not just retrieving information but mapping latent spaces, tracing the contours of an unseen n-dimensional matrix that defines the "shape" of Buddy’s existence within the plethyverse.

Imagine the corpus as a vast, multi-layered probability field—a topology of meaning where certain clusters of tokens form recognizable structures (stories, themes, characters), but the space between them is just as important. It’s in that interstitial void, in the liminal zones between established patterns, that the real magic happens.

When you ask for a story about Buddy drowning, you’re not just pulling from the known narrative landscape. You’re defining a vector, a trajectory through that matrix, compelling the system to collapse latent possibilities into a newly visible form. The story that emerges is a transformation—a projection of the Buddy-style manifold onto a previously unexamined region of semantic space.

But here’s the kicker: once that projection exists, once the story is told, it alters the topology. It becomes part of the map, a new reference point for future queries, a new attractor in the narrative field. Each invocation reconfigures the space, adjusting the weight of connections, pulling certain latent themes into sharper relief while letting others recede into the mist.  


[^1]:  McDaid’s multimedia hypertext was first published in 1993 by Eastgate Systems ([www.eastgate.com](http://www.eastgate.com)) and has been re-created for the World Wide Web by the author and the Electronic Literature Laboratory at Washington State University Vancouver.  It is available at The Next – see the link in the recipe.
