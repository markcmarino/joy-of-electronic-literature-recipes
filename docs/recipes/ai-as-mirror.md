---
title: AI as Mirror Recipes for Three Digital Selves
chef: Carrie Sijia Wang
abstract: Three recipes for creating AI chatbot versions of yourself using rule-based scripting, Markov chains, and large language models.
description: |
  "AI as Mirror" offers three recipes for creating chatbot versions of yourself, each
  using a different AI approach. Recipe 01 (Scripted Self) uses RiveScript keyword
  matching and p5.js to build a rule-based chatbot from prewritten conversations with
  yourself—predictable, comforting, and fully under your control. Recipe 02 (Remixed
  Self) feeds your own journal entries or essays into a Markov chain model via the RiTa
  library, generating new sentences from probabilistic recombinations of your writing.
  Recipe 03 (Reflected Self) uses a large language model such as ChatGPT with a
  retrieval-augmented prompt to perform a generative version of your personality based
  on your uploaded texts.

  Author Carrie Sijia Wang frames AI as a critical and experimental ingredient rather
  than a neutral tool—one that can serve as a lens on human behavior, a means of
  reflective conversation, or a mirror for investigating how one's identity is perceived
  through collective machine intelligence. All three recipes prioritize working with
  small, personally meaningful texts rather than scale, and are accessible without
  advanced programming knowledge.

  Wang emphasizes privacy, agency, and the irreplaceability of genuine human experience,
  while embracing the strange and revealing possibilities of digital self-portraiture.
  These "fake yous" are not meant to replace the real you, but to explore what it means
  to be human in an AI-infused, machine-coded world.
genres:
  - Human-computer collaboration
difficulty_pans: 2
yields: |
  Three distinct AI self-portraits: a scripted keyword-matching chatbot, a Markov chain
  text remixer, and an LLM personalized with your own writings—each revealing different
  facets of digital selfhood.
github_link: https://tinyurl.com/scriptedself
---

## Ingredients

**Recipe 01: Scripted Self**
- Prewritten conversations with yourself (at least 20 exchanges)
- RiveScript (free, open-source chatbot scripting language)
- p5.js (free, open-source JavaScript library for creative coding)
- Cooking template: https://tinyurl.com/scriptedself

**Recipe 02: Remixed Self**
- Your writings in digital format (journal entries, essays, morning pages, stream-of-consciousness notes)
- RiTa (free, open-source library for computational text with Markov chain support)
- p5.js
- Cooking template: https://tinyurl.com/remixedself

**Recipe 03: Reflected Self**
- Your writings in digital format
- A large language model chat platform (ChatGPT or equivalent)

## Method

**Recipe 01: Scripted Self**

1. Write a conversation with yourself—what you might say when you feel a certain way, and the ideal response. Write at least 20 exchanges.
2. Duplicate the table. In the second version, reduce each input to a keyword or phrase; keep responses as-is. Make keywords mutually exclusive, all lowercase, no punctuation.
3. Open the cooking template in your browser: https://tinyurl.com/scriptedself
4. Add keyword/response pairs in RiveScript syntax at the bottom of the code:
   ```
   + [*] keyword you say [*]
   - The chatbot's response.
   ```
5. Modify the "catchall" responses for when no keyword matches.
6. Press the play button to run the program and chat with your bot.

**Recipe 02: Remixed Self**

1. Type up your writings (journal entries, essays, stream-of-consciousness notes, morning pages).
2. Open the cooking template: https://tinyurl.com/remixedself
3. Copy and paste all your text into the input field and press "PROCESS MY WORDS."
4. Press "GENERATE A THOUGHT" to produce remixed sentences—new thoughts built from old ones.

**Recipe 03: Reflected Self**

1. Type up your writings to serve as the chatbot's database.
2. Sign in to ChatGPT (https://chatgpt.com/) and enable "Turn on temporary chat" for privacy.
3. Send the following system prompt, pasting all your writings at the end:
   > *In this conversation, you are a version of me, not an AI assistant. Perform a personality based on the following text, adopt the tone of voice, always retrieve and mix some of the sentences in your response, answer in less than 30 words: [paste writings here]*
4. Start chatting. Add instructions as you go to refine tone and style.

## Notes

- Recipe 02 runs entirely in the browser—no data is sent to a server. Recipe 03 uses ChatGPT; enable temporary chat to prevent your writings from training OpenAI's models.
- Recipe 03 is a manual, simplified version of retrieval-augmented generation (RAG). For more control, use a paid API with a system-level prompt.
- Over longer chats in Recipe 03, the bot may drift from your instructions—this is a known limitation of the method.
- These recipes work best with small, personally meaningful texts, not large corpora.
