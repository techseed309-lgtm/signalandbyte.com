# Writing for signalandbyte.com

Add a Markdown file to `content/articles/` (a written explainer, usually one per video) or `content/blog/`
(channel news, behind the scenes). Name it `YYYY-MM-DD-short-slug.md`; the page URL is `/articles/short-slug/`.

```
---
title: The headline
description: One or two sentences for cards, search results and link previews.
date: 2026-10-27
tags: AI safety, OpenAI
video: YouTube video id (optional, shows a click-to-play player)
---
Body in Markdown: ## and ### headings, paragraphs, - and 1. lists, > quotes, **bold**, *italic*, [links](https://...).
End articles with a "## Sources" list.
```

Then run `python tools/build.py` (pages, listings, RSS, sitemap, home page "Latest writing"), commit and push.
The daily GitHub Action only refreshes the video lists (`tools/update_videos.py`).
