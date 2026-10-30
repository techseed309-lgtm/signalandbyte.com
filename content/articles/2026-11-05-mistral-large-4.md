---
title: "Mistral Large 4, decoded: open, huge, but cheap?"
description: Mistral released the weights of a trillion-parameter model. In our five-job test it cost more per job than Gemini 3.8 Flash at default settings, until one setting cut the bill by about 80%. The prompts, the token counts, the hardware and the licence.
date: 2026-11-05
tags: AI, Models, Decoded
video: om2EtwDu0a0
---
Mistral published the full weights of **Mistral Large 4** on Hugging Face on 29 October 2026. In our own test it still cost more per job than a closed model from Google, until we changed one setting and the bill fell by about 80%. Here is what was released, why "open" doesn't mean it runs on your computer, what it costs per job instead of per token, the setting, and what the licence lets you build and sell.

## What changed
- The weights are out (8-bit, a 4-bit version for NVIDIA's newest chips, and community llama.cpp conversions). Developers could already call the model through Mistral's API since early October.
- The API price is now **$0.70 per million input tokens and $2.10 per million output tokens**, about half the preview list price ($1.36 / $4.18).

## How it works
About **1.05 trillion parameters** are stored, but only about **52 billion** work on any single word. Most layers are teams of 128 smaller "experts"; a router picks four for each word, plus one shared expert every word goes through. That is why it can be served cheaply, and why the whole model still has to sit in memory.

## What it takes to run
- 2-bit community version: one Apple Silicon Ultra machine with 512 GB of memory.
- Mistral's 4-bit version: four of NVIDIA's top Blackwell data-centre GPUs (Mistral's figure).
- 8-bit version: eight NVIDIA H200s (Hugging Face's deployment recipe).

Not a laptop, not a gaming PC. What the open weights really give is control: a company, university or host can run it on hardware they control, with no outside provider deciding what it may answer.

## Price per token vs price per job
Artificial Analysis puts Mistral Large 4 at **26** on its Intelligence Index v5, at about **$2.06 per task**; Gemini 4 Carbon scores 59 at about $7.76 per task. Its own page calls Large 4 "somewhat verbose".

### Our test (30 Oct 2026, one run each, demo data)
Same five everyday paid jobs, output tokens per job (thinking included):

| Job | Mistral default | Mistral high | Mistral low | Gemini 3.8 Flash |
|---|---|---|---|---|
| Invoice → JSON | 2,138 | 1,881 | 947 | 923 |
| Contract risk review | 2,777 | 3,435 | 1,285 | 1,748 |
| Backup script | 12,473 | 8,984 | 751 | 3,827 |
| Python bug fix | 5,287 | 6,980 | 901 | 1,671 |
| German support reply | 1,955 | 1,050 | 580 | error (HTTP 503) |

- Default Mistral wrote about 24,600 output tokens for roughly 1,800 words of answers: most of the bill was thinking you never see.
- On the four jobs both models answered, default Mistral cost about **55% more** than Gemini 3.8 Flash at Google's paid list price ($0.75 / $3.75), despite cheaper tokens.
- With **`"reasoning_effort": "low"`** Mistral wrote about 82% fewer tokens; all five jobs together cost under one cent, about 70% cheaper than Flash on the shared jobs, in about a third of the time.
- Quality on low: four of five answers correct and usable; the bug fix missed the empty-list case that the default caught.

This is a small test. Run your own jobs before you move a real workload, and on Mistral's free plan your prompts may be used for training, so test with demo data.

### The request
```json
{
  "model": "mistral-large-4",
  "messages": [{"role": "user", "content": "…"}],
  "reasoning_effort": "low"
}
```

### The five prompts (copy them)
### 1. Invoice → JSON

```text
Extract these fields as JSON (vendor, invoice_number, date ISO-8601, currency, subtotal, tax, total, line_items[{description, qty, unit_price}]). Check that the numbers add up and add a field 'mismatch' with any problem you find.

INVOICE
Northwind Print Co. - Invoice #NW-20431 - 14 Oct 2026
3 x A2 posters @ 18.50
250 x business cards @ 0.12
Design hour x 2 @ 45.00
Subtotal 175.50
VAT 20% 35.10
Total 210.60 EUR
```

### 2. Contract risk review

```text
You are reviewing a freelance web-development contract for the freelancer. List every clause below that is risky for the freelancer, explain why in one sentence each, and propose replacement wording.

1. The Client may request unlimited revisions until satisfied.
2. Payment is due 90 days after final approval.
3. All intellectual property, including pre-existing code libraries of the Developer, transfers to the Client on signature.
4. The Developer is liable for any loss of revenue caused by downtime of the website, without limit.
5. Either party may end this agreement with 7 days' written notice; work completed up to that date will be paid.
```

### 3. Backup script

```text
Write a bash script for Ubuntu that backs up /var/www and a PostgreSQL database named shop to /backups with a date-stamped filename, keeps only the last 14 backups, logs to /var/log/backup.log, exits non-zero on any failure, and show the crontab line to run it nightly at 02:30.
```

### 4. Python bug fix

```text
This Python function should return the median of a list of numbers but fails on some inputs. Find every bug, explain each in one line, and give the fixed function with three test cases.

def median(xs):
    xs.sort()
    n = len(xs)
    if n % 2 == 1:
        return xs[n/2]
    return (xs[n/2] + xs[n/2 + 1]) / 2
```

### 5. German support reply

```text
A customer wrote (in German): 'Ich habe vor drei Wochen bestellt, die Sendungsverfolgung zeigt seit zehn Tagen nichts an und niemand antwortet. Ich will mein Geld zurück.' Write the reply from a small online shop: apologise, explain the next step (we open a carrier investigation today, refund in full if not found within 5 working days, or the customer can choose an immediate refund now), and keep it under 120 words. Give the reply in German and an English translation.
```

## Where it's strong, and the case against
By Mistral's own numbers it is strongest at cyber defence, finance, legal work and images (51% on the Artificial Analysis Cyber Index; 93% of Cybench challenges, from its 6 October launch post; the technical report isn't out yet). The case for it is control: run it inside your own walls. The case against is the independent scores: on the broad index it sits far below the closed frontier models.

## The licence
A modified MIT licence. You can use it, change it, fine-tune it and sell copies of what you build, including products where the model powers features inside your app (a contract checker, a support inbox that drafts replies, an invoice reader). Selling the model itself as a service, where other people get raw access and control the prompts, settings or training data, needs a separate commercial licence from Mistral. Keep Mistral's copyright notice in what you ship. There is no revenue threshold in the text. (A summary, not legal advice.)

## Who should switch
- Lots of routine API jobs: try it on low effort against what you pay now, and count tokens, not prices.
- Data that can't leave your building: one of the strongest open models you can run yourself, given the hardware.
- The hardest open-ended problems: a closed frontier model is still ahead.

Try it: sign in to Mistral Studio, open API Keys, create a key, then send your own jobs on low and on high and compare the token counts.

## Sources
- Mistral, Mistral Large 4 open weights: https://mistral.ai/news/mistral-large-4-oss/
- Mistral docs, Mistral Large 4 (price, context): https://docs.mistral.ai/models/mistral-large-4-0
- Mistral docs, reasoning effort: https://docs.mistral.ai/capabilities/reasoning
- Hugging Face, Welcome Le Chonk: https://huggingface.co/blog/mistral-large4
- Hugging Face model page and LICENSE: https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B
- Artificial Analysis, Mistral Large 4: https://artificialanalysis.ai/models/mistral-large-4
- Artificial Analysis, Gemini 4 Carbon: https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
- Google, Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
