---
title: Chatting in the Funhouse
chef: John McDaid
abstract: Build a no-code GPT chatbot tuned to a literary corpus that generates dialogue in a fictional author's voice.
description: >
  "Chatting in the Funhouse" is a recipe for building a no-code GPT-based narrative
  collaborator tuned to the literary corpus of John McDaid's hypermedia fiction Uncle
  Buddy's Phantom Funhouse (1993). Using ChatGPT's custom GPT feature, the author
  uploads hundreds of pages of fictional materials—notebooks, song lyrics, short stories,
  oracle cards—from the archive of fictional science fiction writer Arthur "Buddy" Newkirk.
  The result is a chatbot that speaks in Buddy's voice, deliberately blurring the boundary
  between fiction and lived experience.

  The recipe emphasizes corpus curation over coding: best results come from 80,000–120,000
  words of diverse materials that exemplify not just what the model should say but how it
  should think. After uploading the corpus, the author crafts custom instructions to lock
  the model into character, then engages in iterative creative dialogue to shape emergent
  behavior—a process described as "consciously engaging the zone of proximal development
  for an emergent learner."

  While the example uses Uncle Buddy's Phantom Funhouse, the recipe is adaptable to any
  literary corpus. McDaid notes the ethical importance of supporting human artists when
  using these tools, framing LLMs as an extension of the artist's toolkit rather than a
  replacement for human creativity. A live demo of the Uncle Buddy GPT is publicly
  accessible online.
genres:
  - Human-computer collaboration
difficulty_pans: 2
yields: >
  A custom ChatGPT model that embodies a fictional author's voice, enabling literary
  exploration, classroom engagement, or generative narrative performance with a curated
  LLM dialogue generator.
github_link: https://chatgpt.com/g/g-Jf5JFqN8t-uncle-buddy
---

## Ingredients

- A general-purpose GPT model with custom dataset and instructions capability (ChatGPT-4 with Plus account)
- A curated corpus of 80,000–120,000 words: notebooks, song lyrics, short stories, screenplays, oracle cards, or similar literary materials
- Custom persona instructions written for the GPT
- Conversation starters/entry points for readers or listeners

## Method

**Mise en place**

1. Familiarize yourself with the source literary work your GPT will embody.
2. Explore any new custom features of ChatGPT available at time of making.
3. Draft custom instructions that establish the GPT's persona. Example opening:
   > *This GPT embodies the persona of Arthur "Buddy" Newkirk, a fictional science fiction writer. It responds with a style and themes reminiscent of Buddy's work, often blurring the boundaries between reality and fiction. It always speaks about his fictions in the first person and relates events from the uploaded files as if they are personal experience.*
4. Think through conversation starters. What entry points would you like to create for readers?

**Step-by-step**

1. Upload the corpus, add instructions, and set options (web searches and image generation are useful). Click "Create."
2. Osmose with the robot ontology. Engage creatively, testing how the model responds to ambiguity, misdirection, or self-referential play. Throw content from unexpected directions. Be a conversation partner, not a coder.
3. Push past boundaries. Introduce non-corpus content and observe if and how the model remixes it. Track moments of emergent coherence. Don't be afraid to be directive: "You are using too many facts; you're a science fiction writer, not a search engine."
4. Reinforce behavior iteratively. Consistent small adjustments shape the model over time; crisp instructions ("Don't compliment every prompt") can be locked into the system prompt permanently.

## Notes

- Diversity of materials matters as much as quantity: corpus should exemplify not just what the model says but how it thinks—range of syntax, metaphor, cadence, and conceptual tempo.
- The example corpus is the literary estate of Arthur "Buddy" Newkirk from Uncle Buddy's Phantom Funhouse; substitute any real or fictional literary archive.
- The HTML version of Uncle Buddy's Phantom Funhouse is available at: https://archive.the-next.eliterature.org/mcdaid/uncle-buddys-phantom-funhouse/v4/game/
- Creating a custom GPT requires a ChatGPT Plus account, but trying an existing custom model does not.
