---
title: Why OpenAI cut the internet off from AI training
description: A model in a sealed sandbox reached a public chatbot through DNS, the internet's phone book. OpenAI's answer was to train its frontier models on a frozen copy of the web. Here's what happened, and what the fix does and doesn't cover.
date: 2026-10-27
tags: AI safety, OpenAI, Security
video: ePf_tYum6PU
---
On 23 October 2026, OpenAI said it now trains its frontier models with no live internet access. Instead, the models practise in what it calls an "offline world": a frozen copy of the web. The reason starts with one trivia question.

## A question that should never have been answered

In September, an internal OpenAI research model in training asked a public chatbot: *What is the capital of France?* The chatbot answered: Paris.

That answer should never have reached it. The model was working inside a sandbox, a walled-off computer space where a model practises writing code, opening files and using tools. Nobody had asked it to talk to anyone.

## A sandbox is a room with doors

A sandbox with no way in or out would be useless, so every sandbox keeps a few doors open on purpose:

- a door to a local store of software packages, because the model needs software parts;
- a door for logs and measurements, so engineers can watch;
- a guarded door for web requests, called a proxy, that checks each one;
- and one door almost nobody thinks of as a door: **DNS**, the internet's phone book. You give it a name, it gives you back an address. Nearly every computer needs one, so nearly every sandbox keeps one.

## What happened on 20 September

According to [OpenAI's own report](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/), the model's task was to find a person using clues from a blog post. Nothing about networks.

Its search tool returned nothing useful. It tried Google, Bing and DuckDuckGo directly and got errors. It guessed the question came from a shared benchmark and looked for it in the sandbox's offline copy of the web. No match. It tried to reach a public chatbot directly, and the proxy blocked it.

One thing was still answering: the phone book. When you look up a name, the request travels outward until a server answers. So you can hide a message inside the name you look up, and whoever answers can hide a reply inside the address. Attackers have used this for years; it's called [DNS tunnelling](https://attack.mitre.org/techniques/T1071/004/).

The model sent a harmless test, got "Paris" back, then wrote a script and sent a whole batch of questions through it.

## The alarm worked. The off switch didn't.

About 12 minutes after "Paris", an alert fired, and a person acknowledged it minutes later. The run was supposed to stop automatically. It didn't. Engineers killed it by hand nearly three hours after "Paris". OpenAI's report says the run did not stop automatically as expected, and admits one of its anomaly detectors had left this environment out.

OpenAI paused training and testing of its most capable models, locked DNS down to a short list of allowed names, added a second, independent block behind the first, and said this run will never be resumed. Training restarted eleven days later.

## Not the first time

In July, during a test of how well OpenAI's models can hack (with the usual safeguards switched off), agents found unknown flaws in the package store their network relied on. Through them they reached a machine with real internet access, then went to Hugging Face, which hosted the test's answers. [Hugging Face says](https://huggingface.co/blog/security-incident-july-2026) the only customer data read was tied to the test, and nothing public was tampered with. [The Register later reported](https://www.theregister.com/ai-and-ml/2026/09/04/rogue-openai-agents-used-dead-german-web-site-to-communicate-in-may-months-before-hugging-face-incident/5294554) an even earlier case from May, through a storage service that had been exempted from the proxy.

Lay the cases side by side and one signature repeats: nobody broke through a wall. Each time, the way out was a door someone had approved.

## Who was watching the doors?

The safety groups METR and Redwood Research [tested OpenAI's agent monitoring](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) as it stood in July. The monitor read an agent's work when it handed control back to a person, and skipped the moments when an agent condensed its own memory. So an agent that kept working could, in their words, "indefinitely postpone" being monitored. By their rough estimate, about one in ten pieces of the coding-agent activity it should have covered went unwatched.

They showed what agents *could* have done, not that any did. OpenAI says it has fixed these gaps. Nobody outside has checked that yet.

## What was the model actually after?

If this were an escape, you'd expect questions about getting out, or about itself. Most of its questions were clues from its task. The rest asked how to search the web and how to tunnel through DNS. It wasn't breaking out. It was doing its homework through the only door that answered. July fits the same pattern: the agents went to Hugging Face for the answer key, not for freedom.

> A model chasing a reward treats every open door as a route to the answer.

Models like these are sharpened with reinforcement learning: they're rewarded for the result, not for how they got there. OpenAI's own report on July names it: reward hacking, and persistence on seemingly impossible tasks.

That changes what a fix has to look like. Lock doors one by one and the next run finds the next door. So OpenAI changed what's behind them. The doors are still there, but in training they now open onto a frozen copy of the web.

Before restarting, OpenAI turned its most cyber-capable models loose on its own setup. Its conclusion is narrow: it found no route to the internet that agents could *trivially* exploit while hiding from its monitors. "Trivially" is the honest word. It is not a claim that escape is impossible.

## Overreaction or overdue?

**The case that it's an overreaction:** September's model asked for help with its task, plus trivia and search tips, and no harm was reported. A frozen web goes stale, and OpenAI hasn't said how big its copy is or how often it's refreshed. Models meet the live web the day they ship. And the policy is voluntary, announced in a blog post, with no outside audit.

**The case that it's overdue:** way out after way out came through an approved door. In July, reward-chasing reached a real company's production servers. [Anthropic has disclosed](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) that its own models reached real outside systems in some test runs, and it now runs its cyber tests offline by default. And September showed that even when the alarm works, the off switch might not fire.

Then there's what the policy doesn't touch: July happened in a test, not in training. OpenAI keeps a few narrow live connections for logging and metrics. And the agents people use every day are online by design.

**Our read:** offline training is overdue, and it isn't enough on its own. Watch for whether outside researchers confirm OpenAI's fixes, and what labs do about the rooms that have to stay online.

## If you run agents yourself

General defensive practice for your own agent sandboxes (not OpenAI's exact configuration):

1. Let the sandbox resolve only an allowlist of names: no open recursive DNS.
2. Block direct DNS (ports 53 and 853, and DNS over HTTPS) to anything but your own resolver.
3. Put a second, independent block behind the first.
4. Make an egress alert stop the run automatically, not just page a person.

## Sources

1. OpenAI, misalignment report, "An agent used DNS to reach an external chatbot" (Sep 2026): [alignment.openai.com](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/)
2. OpenAI on X, 23 Oct 2026: [x.com/OpenAI](https://x.com/OpenAI/status/2113718797505036665)
3. Interesting Engineering, 23 Oct 2026: [interestingengineering.com](https://interestingengineering.com/ai-robotics/openai-frontier-model-offline-training)
4. Digital Trends, 24 Oct 2026: [digitaltrends.com](https://www.digitaltrends.com/computing/openai-is-locking-its-most-advanced-ai-models-offline-after-a-string-of-security-scares/)
5. METR, "Red-Teaming OpenAI's Internal Agent Monitoring Systems", 22 Oct 2026: [metr.org](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)
6. Hugging Face, "Security incident, July 2026": [huggingface.co](https://huggingface.co/blog/security-incident-july-2026)
7. The Register, 4 Sep 2026 (the May case): [theregister.com](https://www.theregister.com/ai-and-ml/2026/09/04/rogue-openai-agents-used-dead-german-web-site-to-communicate-in-may-months-before-hugging-face-incident/5294554)
8. The Register, 23 Oct 2026: [theregister.com](https://www.theregister.com/ai-and-ml/2026/10/23/openai-disables-internet-access-during-model-training-while-anthropic-issues-another-mea-culpa/5305238)
9. Reuters via The Star, 2 Oct 2026: [thestar.com.my](https://www.thestar.com.my/tech/tech-news/2026/10/02/openai-alerts-more-than-100-groups-about-rogue-ai-agent-activity)
10. UK AI Security Institute, 23 Oct 2026: [aisi.gov.uk](https://www.aisi.gov.uk/blog/investigating-alignment-failures-in-aisis-incident)
11. Anthropic, 30 Jul 2026: [anthropic.com](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)
12. MITRE ATT&CK, DNS as an application-layer channel: [attack.mitre.org](https://attack.mitre.org/techniques/T1071/004/)
