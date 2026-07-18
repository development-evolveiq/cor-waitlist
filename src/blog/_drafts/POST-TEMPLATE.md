---
title: "Your Question-Shaped Title Goes Here (e.g. How Do Lean B2B SaaS Teams Get Cited by ChatGPT?)"
description: "One or two sentences that directly answer the title question. This appears in Google results, AI answers, and the blog listing — write it as a standalone answer, 150–160 characters."
date: 2026-07-18
author: "COR Team"
faq:
  - q: "A real question a buyer would ask an AI?"
    a: "A direct, self-contained answer in 1–3 sentences. This gets marked up as FAQPage schema automatically — AI engines lift these verbatim."
  - q: "Second question?"
    a: "Second answer. Two to four FAQ items per post is the sweet spot."
---

Open with the direct answer to the title question in the first two sentences — no warm-up, no "in today's fast-paced world." AI engines extract the first paragraph under a heading as the answer.

## Use questions as H2 headings whenever possible

Then answer the question immediately in the first sentence below it. Follow with evidence: a number, an example, a step list.

Key rules this template encodes:

- **One post = one question.** If you're answering three questions, that's three posts linking to each other.
- **Numbers and dates make content citable.** "Reply rates tripled" is weak; "reply rates went from 2.1% to 6.4% over 60 days (June–July 2026)" is quotable.
- **Tables get extracted.** Comparisons, before/after, pricing — put them in markdown tables:

| Approach | Reply rate | Effort |
|---|---|---|
| Cold list blast | ~1% | Low |
| Warm signal-based | 4–7% | Medium |

## How to publish a post

1. Copy this file into `src/blog/` (not `_drafts/`) with a short, keyword-rich filename — the filename becomes the URL: `warm-linkedin-prospecting.md` → `corgtm.com/blog/warm-linkedin-prospecting/`
2. Fill in the front matter at the top (title, description, date, faq)
3. Write the body in markdown
4. Commit and push — Vercel deploys it, and it's automatically added to the sitemap, RSS feed, and blog listing with all schema markup included

Files left in `_drafts/` are never published.
