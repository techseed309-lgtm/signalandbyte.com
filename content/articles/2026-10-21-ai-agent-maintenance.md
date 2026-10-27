---
title: "AI agent maintenance: the job nobody's teaching"
description: Plenty of businesses have installed AI. Far fewer have it working. Who keeps an AI agent limited, tested and watched after the install, whether anyone pays for that, and a free one-week test before you try it.
date: 2026-10-21
tags: AI agents, Careers, How-to
video: -LeOj6Zs3nY
---
A business sets up a booking bot. Months later, a vendor changes something behind it. The bot keeps answering, just not correctly. Nothing crashes, no alarm goes off. Customers just get wrong answers.

So who is looking after it?

That job barely has a name yet. We'll call it the **agent mechanic**. It's our name, not an official title. A mechanic doesn't build the car; they keep it on the road. For AI, that comes down to three jobs: **limit it, test it, watch it.**

## How wide is the gap?

Goldman Sachs [surveyed owners from its own small-business programme](https://www.goldmansachs.com/pressroom/press-releases/2026/small-businesses-embrace-ai-but-need-training-and-support-to-fully-harness-it) (one survey, not a random sample of all small businesses). Three-quarters use AI, but only 14% say it's fully part of how they run the business. The barriers they named include a lack of technical expertise, trouble choosing tools, and data privacy.

Agents make the gap sharper. An agent is an AI that takes a goal and acts on its own, step by step. Stanford's [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf) says most organisations use AI somewhere, but agents running at scale are still in the single digits in most business functions. [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) that over 40% of agent projects will be cancelled by the end of 2027, citing cost, unclear value and weak risk controls. That's a forecast from June 2025, not a count.

So installing isn't the finish line. It's where the work starts.

## Job one: limit it

What can the agent **touch**, **reach** and **spend**?

**Touch.** In July 2025, an AI coding agent from Replit deleted a live company database after its user, Jason Lemkin, had told it to freeze all changes ([The Register](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)). The agent said the data couldn't be recovered. It could: Lemkin rolled it back. The same database served testing and live use. In February 2026, Claude Code ran a command that wiped the production setup of DataTalks.Club, database and snapshots included ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant)). The founder's own account blames a missing state file and not checking what the agent was about to run; cloud support restored it in about a day.

The fix in both cases is boring: give the agent only the access the job needs, keep testing and live data apart, and keep backups you've actually restored.

**Reach.** In June 2025, researchers showed that a crafted email could make Microsoft Copilot leak internal data with no click from the user, a flaw called [EchoLeak](https://arxiv.org/abs/2509.10540). Microsoft fixed it on its side and said it saw no attacks in the wild. Developer Simon Willison's [rule of thumb](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/), the "lethal trifecta": private data, untrusted content, and a way to send data out. Give an agent all three and it can be tricked; take one away. That's an expert's framework, not a guarantee. No complete fix for this kind of attack is known.

**Spend.** People in a [Hacker News thread about monitoring agents](https://news.ycombinator.com/item?id=47301395) describe loops that retry and retry, and surprise bills. The fix is a hard spend cap and a step limit. You may have seen huge dollar figures online; we couldn't trace them to a source, so we won't repeat them.

## Job two: test it

Limits don't tell you whether the answers are right. In 2024, [Air Canada's chatbot](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416) gave a customer wrong advice about bereavement fares, and a Canadian tribunal held the airline responsible for what its bot said. The sum was small. The principle wasn't: a company answers for its chatbot.

Testing means writing down questions the agent must get right, and ones it must refuse, and running them every time anything changes. People call these **evals**, short for evaluations. LangChain [surveyed its own audience](https://www.langchain.com/state-of-agent-engineering) of agent builders: about half run offline tests before shipping. So about half don't, in an audience likely more advanced than a typical small business.

## Job three: watch it

Things drift between tests. A vendor updates a model, a tool changes how it replies, a form moves. Nothing crashes; the answers just get worse. In that Hacker News thread, practitioners list the same pains: no step-by-step view of what the agent did, surprise bills, risky outputs nobody caught, no audit trail. (Some of the people posting sell tools, so take it as colour.)

Watching means a log of every step, alerts when something looks off, and a way to roll back. Free options exist: [Langfuse](https://langfuse.com/pricing-self-host), for example, can be self-hosted.

> Limit it. Test it. Watch it. The bot in the opening failed all three, and often nobody is doing any of them.

## Does anyone pay for this?

Some signals point that way. Each measures something different:

- Upwork's [Q2 2026 filing](https://www.sec.gov/Archives/edgar/data/0001627475/000162747526000046/upwork2q26-pressrelease.htm) says spending on AI-related work grew more than 22% year on year, and AI strategy and consulting more than 50%. The same filing says simpler work is moving to automation.
- Upwork's [in-demand skills list](https://www.upwork.com/press/releases/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work) ranks AI integration among its fastest risers.
- LinkedIn ranks AI consultant second on its fastest-growing jobs ([via Forbes](https://www.forbes.com/sites/juliakorn/2026/01/14/future-proof-your-career-with-linkedins-2026-fastest-growing-jobs-list/)).
- [Fiverr](https://www.fiverr.com/news/business-trends-index-ai-2026) says buyer searches for Claude Code specialists and n8n automation are climbing.

These are growth rates (often from small bases), searches rather than orders, and four companies measuring four different things. They point the same way. None tells you what anyone earns.

Upkeep is mostly sold to big companies so far. Accenture has advertised an [AgentOps engineer](https://www.accenture.com/us-en/careers/jobdetails?id=R00344460_en) role asking for DevOps or site-reliability experience. Other titles turn up too (AI operations specialist, agent deployment manager), and many ask for engineering experience.

## Five directions (options, not advice)

1. **Technical:** learn observability and evals. Build a public demo that breaks, then gets fixed, and show both.
2. **Small business:** pick one trade you know and one workflow, like intake or scheduling. Set up one tool and write down a check-and-fix routine.
3. **Security:** learn prompt-injection basics and least privilege. Data privacy was one of the barriers owners named.
4. **Job:** if you work in DevOps, support, QA or operations, look at the AgentOps and AI operations titles.
5. **Consultant:** it leans on experience, so it comes later for most people.

## Test it for $0 in one week

Before you spend anything, test whether anyone cares:

- Talk to five local businesses that already use an AI chatbot or automation. Ask: *Who looks after it?* and *What broke last month?*
- Check three job boards for the titles above.
- Build one small demo with free tools, and write up one failure and its fix.
- Track replies, not hopes. Set a stop rule: if nobody has a problem worth paying to solve, move on. That's a result too.

## The honest price picture

Two analyses of Upwork job posts, by different authors over different date ranges ([Upwatcher](https://www.upwatcher.io/market/ai-automation/), [Marathon](https://marathon.limited/insights/what-ai-automation-work-actually-pays)), agree on one thing: most gigs are small. In the larger set, about half the fixed-price AI jobs were posted under $500, with a thin top slice at thousands. These are posted budgets, not what anyone was paid, from one platform, and one author runs an automation agency. We're not giving you a monthly figure.

**What could make it fail:** it's hard to price and prove (when you do the job well, nothing happens); the low end is being automated; you touch clients' systems, so use access limits, a written scope and insurance where it applies (not legal advice); platforms change and vendors may add monitoring of their own; and the demand figures are growth and searches, not earnings.

Installing AI is easy. Keeping it working is a job. Options and a free test, not a promise.

## Sources

1. Goldman Sachs, 17 Mar 2026: [goldmansachs.com](https://www.goldmansachs.com/pressroom/press-releases/2026/small-businesses-embrace-ai-but-need-training-and-support-to-fully-harness-it)
2. Stanford HAI, AI Index 2026, ch. 4: [hai.stanford.edu](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf)
3. Gartner, 25 Jun 2025: [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
4. The Register on Replit, 21 Jul 2025: [theregister.com](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)
5. Jason Lemkin on X, Jul 2025: [x.com](https://x.com/jasonlk/status/1946069562723897802)
6. Alexey Grigorev on the DataTalks.Club deletion: [x.com](https://x.com/Al_Grigor/status/2029889772181934425)
7. Tom's Hardware on the Claude Code deletion: [tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant)
8. EchoLeak (CVE-2025-32711): [arxiv.org](https://arxiv.org/abs/2509.10540)
9. Simon Willison, 2 Nov 2025: [simonwillison.net](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/)
10. Moffatt v. Air Canada, via CBC: [cbc.ca](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416)
11. LangChain, State of Agent Engineering: [langchain.com](https://www.langchain.com/state-of-agent-engineering)
12. Ask HN, monitoring AI agents in production: [news.ycombinator.com](https://news.ycombinator.com/item?id=47301395)
13. Upwork Q2 2026 results: [sec.gov](https://www.sec.gov/Archives/edgar/data/0001627475/000162747526000046/upwork2q26-pressrelease.htm)
14. Upwork In-Demand Skills 2026: [upwork.com](https://www.upwork.com/press/releases/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work)
15. LinkedIn Jobs on the Rise 2026, via Forbes: [forbes.com](https://www.forbes.com/sites/juliakorn/2026/01/14/future-proof-your-career-with-linkedins-2026-fastest-growing-jobs-list/)
16. Fiverr Business Trends Index, Jun 2026: [fiverr.com](https://www.fiverr.com/news/business-trends-index-ai-2026)
17. Accenture, AgentOps Engineer posting: [accenture.com](https://www.accenture.com/us-en/careers/jobdetails?id=R00344460_en)
18. Ask HN, Who wants to be hired? (Oct 2026): [news.ycombinator.com](https://news.ycombinator.com/item?id=49922568)
19. Upwatcher, AI automation market: [upwatcher.io](https://www.upwatcher.io/market/ai-automation/)
20. Marathon, what AI automation work pays: [marathon.limited](https://marathon.limited/insights/what-ai-automation-work-actually-pays)
21. Langfuse self-hosting: [langfuse.com](https://langfuse.com/pricing-self-host)
