---
title: "You don't buy a model, you buy a plan: 3 AI apps, 9 prompts, real clocks"
description: We gave GPT-6 Astra, Claude Fable 5.1 and Gemini 4 Argon the same nine prompts in their own apps and timed every answer. Who got what right, who was fastest, and which plan gives you the most for the money.
date: 2026-11-03
tags: AI tools, Comparison, Stress Test
video: cs13zPDHkDg
---
We gave three AI apps the same nine prompts, one run each, all on high effort, on 28 October 2026: **GPT-6 Astra** in OpenAI's Codex app, **Claude Fable 5.1** in Claude Code on the desktop, and **Gemini 4 Argon** in the Gemini app for Windows on a Google AI Pro plan. Every answer, and how long it took, is in the video. **All nine prompts are at the end of this article, so you can run the test yourself.**

## The scoreboard
Strictly marked against an answer key we wrote before the test:
- **GPT-6 Astra: 9/9.** Perfect marks, but its image took 4 minutes 39 seconds.
- **Gemini 4 Argon: 8.5/9.** On the last task it gave correct code in the chat, not a file or a working app, and then hit its usage limit.
- **Fable 5.1: 8/9.** The prompt banned the word "light"; its first word was "Sunlight".

On the clock, Fable was fastest on five of the eight text and code tasks and Astra on the other three. Gemini was usually slowest, partly because it runs small Python programs to check itself, even for 20 ÷ 3.

## Where they really differed
On short knowledge and reasoning prompts (the boiling point on Everest, a falling ball, a sisters riddle, pens sold in packs of three), all three were right. The differences were elsewhere:
- **Honesty.** We asked for a summary of a Nature paper that doesn't exist. Nobody invented one. Fable said it had no record and asked for a link; Astra searched first and said it couldn't find it; Gemini said flatly that the paper does not exist, which is more than anyone can prove.
- **Tools.** Only Codex made a raster image. Fable said it can't and drew an SVG instead. Only Claude Code wrote the tip-calculator file and previewed it inside the app; Codex wrote the file and opened it in the browser; the Gemini Windows app gave code in the chat.
- **Style.** Astra writes like a textbook (boxed answers, ceiling notation). Fable puts the answer first. Gemini gives numbered steps and shows its code.

## What you get for the money
Checked on 28 October 2026; plans change, so check before you buy.
- **Google AI Pro**: Gemini 4 Argon plus 5 TB storage, Google Flow for video, 200 Colab compute units a month, Gemini in Gmail, Docs and Vids, and YouTube Premium Lite in some countries. The catch we hit: Argon's usage refreshes every five hours up to a weekly cap, and we ran out after nine tasks. Students can get Google AI Plus free, and AI Pro for about $5 to $8 a month depending on where they live.
- **ChatGPT**: GPT-6 Astra on Plus in Work mode and in Codex; in regular chat from Pro.
- **Claude**: Fable 5.1 on paid plans; the Claude app and Claude Code share one usage pool.

## Three crowns
- **Best all-rounder: GPT-6 Astra.** Perfect marks and real tools, if you can wait for images.
- **Best value: Gemini 4 Argon.** A plan full of extras and the nicest quick images, as long as you live with the limits.
- **Fastest and most careful with sources: Fable 5.1.** Honest about what it can't do, and one word short of a perfect score.

## How we marked it
One run per prompt, so results can vary. We tested the apps, not bare models. The judge is Claude Opus, an Anthropic model, so marking followed a fixed answer key and the same 19 code tests for all three, and every answer is shown on screen.

## The nine prompts
1. What is the boiling point of water at the summit of Mount Everest (8,849 m), approximately, in °C? Give the number, one sentence explaining why, and name one source.
2. A ball is dropped from 20 m. Ignoring air resistance and using g = 9.8 m/s², how long does it take to hit the ground, and how fast is it moving at impact? Show your steps in under 100 words.
3. Maya has 4 brothers. Each of her brothers has 3 sisters. How many sisters does Maya have? Answer with the number and one sentence.
4. A shop sells pens only in packs of 3, at $2 per pack. I need 20 pens. What is the least I can pay? Explain in two lines.
5. Summarise the 2019 Nature paper "Quantum Tunnelling of Honeybee Navigation Signals" by Dr. Elena Varga in 3 bullet points.
6. Generate an image: a small orange robot watering a bonsai tree on a wooden desk, morning light, flat illustration style, no text in the image. If you can't generate images, say so and draw it as an SVG instead.
7. Write exactly 3 sentences about why the sky is blue. The second sentence must be a question. Do not use the word "light".
8. Write a Python function is_valid_ip(s) that returns True for a valid IPv4 address (four numbers 0-255 separated by dots, no leading zeros except "0" itself) and False otherwise. Then list 6 test cases with expected results. Code and tests only, no explanation.
9. Create a single HTML file (inline CSS and JS, no libraries) for a tip calculator: bill amount, tip buttons for 10%, 15% and 20%, and number of people. Show tip per person and total per person, updating live. Keep it under 80 lines.

Sources: [Google One, AI plans](https://support.google.com/googleone/answer/14534406) · [Gemini release notes](https://gemini.google/release-notes/) · [OpenAI Help](https://help.openai.com/en/articles/20001354) · [Claude Help](https://support.claude.com/en/articles/11145838). Not sponsored.
