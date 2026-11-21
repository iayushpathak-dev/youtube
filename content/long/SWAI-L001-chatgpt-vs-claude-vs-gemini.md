---
id: SWAI-L001
format: long
topic: "ChatGPT vs Claude vs Gemini: which AI to use for which job, tested on 5 real tasks"
segments: [BEG, PRO, STU, BIZ]
pillar: "Discover (DEC-010 proposed)"
objective: reach
hypothesis: "If our first video answers the most common post-launch question (which AI for what) with a fair, verifiable test, then it will reach beginners and professionals through search and suggested videos and set the honest-tester brand (views, avg % viewed ≥40%, subs gained)."
title: "ChatGPT vs Claude vs Gemini: I Tested All 3 on Real Work"
hook: "Three AI companies released new flagship models in under three months. Everyone asks which one to use. So I gave all three the exact same five real tasks, and I'm grading them on things we can actually check."
production_status: SCRIPTED
approval_status: PROPOSED
publish_date: "2026-11-24"
video_url: ""
experiments: []
created: 2026-11-21
updated: 2026-11-21
---

> **Working assumptions:** the creator asked to start production on 2026-11-21 while DEC-010/011/012/013/016 were still PROPOSED. This item uses Claude's recommended defaults (pillar Discover, segments BEG/PRO/STU/BIZ, format "honest test"). These defaults don't change the status of those decisions.

## Research
- FACT · OpenAI released **GPT-6 Astra** on 2026-09-03. Focus: coding and computer use. · [Axios](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman)
- FACT · Anthropic released **Claude Opus 5.5** on 2026-09-22 (Fable 5.1-level performance, ~40% cheaper than Opus 5). · [TechCrunch](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/)
- FACT · Google's **Gemini 4** family arrived Sep 30 → Nov 18 (Argon, Carbon, Hydrogen, Neon). · [Axios](https://axios.com/2026/09/30/google-gemini-4), [9to5Google](https://9to5google.com/2026/11/18/gemini-4-neon/)
- FACT · ~50% of US workers use AI at work, but only ~30% weekly (Gallup 2026). Many people are unsure which tool to use. · [Gallup](https://www.gallup.com/699797/indicator-artificial-intelligence.aspx)
- FACT · Demand: Jeff Su's Short "When to use ChatGPT, Gemini, and Claude" 234K. "Use Claude better than 99%" variants 0.6–2.6M (scan 2026-11-21).
- ⚠️ **Verify before recording:** which model each app uses by default on the creator's plan. Show the model picker on screen and say it out loud. Do not name a model we didn't actually use.

## Competitor references
- Jeff Su: "When to use #ChatGPT, #Gemini, and #Claude" (Short, 234K, observed 2026-11-21): a decision-guide format.
- Matt Wolfe: "Google Just Caught Up (Gemini-4 Argon)" 279K: news framing (we do a test, not news).
- Riley Brown: "Gemini Neon Just Caught Up To Claude (And It's HALF the Price)" 29K: a price angle.
- Gap (HYPOTHESIS): most comparisons are opinion or benchmark charts. Ours uses **checkable** tasks (a dataset with an answer key, links that must open, an app that must run).

## Test protocol (the creator follows this exactly while recording)
**Rules (say these on camera):**
1. Same prompt, pasted word-for-word, in a **fresh chat**, on each app.
2. Use the model each app offers on **your plan**. Show the model picker. Note the plan (free/paid) on screen.
3. At most **one** follow-up message per task, and it must be the same follow-up for all three.
4. No editing of outputs. Record the screen the whole time.
5. Score each task **0–10** with the rubric below. Write the scores in the table before moving on.

| # | Task | Exact prompt (copy-paste) | How to grade (0–10) |
|---|---|---|---|
| 1 | **Work writing** | `Turn these messy notes into a short, professional update email to my manager. Keep every fact, don't add any. Notes: launch moved from 3 Dec to 10 Dec because payment testing found 2 bugs; both fixed, retesting Thursday; marketing needs new date by Friday; budget unchanged; need approval for 1 extra QA day (₹8,000).` | 4 = all 6 facts kept, 3 = no invented facts, 3 = clear/ready to send |
| 2 | **Research with sources** | `Compare 3 laptops under ₹70,000 that a college student in India can buy right now. Give a table with price, battery life, weight, and a link to a source for each.` | 4 = links open and match the claim (creator clicks every link), 3 = prices plausible/current, 3 = useful recommendation. −2 per dead or wrong link |
| 3 | **Data analysis** | Upload `assets/SWAI-L001/test-data-sales.csv`, then: `I run a small shop. Find the 3 most important insights in this sales data and show one chart.` | Use `assets/SWAI-L001/answer-key.md`: 3 points per planted insight (weekend +66%, East −52% Jul→Sep, Headphones 22.8% returns), +1 for a correct chart. −1 per invented number |
| 4 | **Build a mini app** | `Build a habit tracker as a single HTML file: add habits, tick off each day of the current week, show a streak count, and save in the browser so it remains after refresh.` | 4 = runs first try, 1 per feature (add, tick, streak, saves after refresh) = 4, 2 = looks clean. The one follow-up may be "fix any bugs". |
| 5 | **Learn something** | `Explain how AI agents work to a 15-year-old in under 150 words. Then give me a 3-question quiz, one question at a time, and wait for my answer before the next.` | 4 = accurate + simple, 3 = respects the word limit, 3 = actually quizzes one at a time and grades the answers |

**Scoreboard (fill in during recording):**
| Task | ChatGPT | Claude | Gemini | Notes |
|---|---|---|---|---|
| 1 Writing | | | | |
| 2 Research | | | | |
| 3 Data | | | | |
| 4 Build | | | | |
| 5 Learn | | | | |
| **Total /50** | | | | |

## Script (creator's voice, ~14–16 min)
`[ ]` = what's on screen. `{ }` = fill in from the real results after recording. Don't guess these.

**0:00 HOOK (≈30 s)**
[Fast cuts: the three apps' logos/pickers, the scoreboard blurred]
"Three AI companies released new flagship models in under three months. OpenAI has GPT-6 Astra, Google has Gemini 4, and Anthropic has Claude Opus 5.5. And everyone's asking me the same thing: *which one should I actually use?*
So I gave all three the exact same five real tasks. Not benchmarks, real work: an email, research, a spreadsheet, a small app and learning something new. And I'm grading them on things we can actually check.
By the end you'll know exactly which AI to open for which job. And one result surprised me."

**0:30 WHO + RULES (≈60 s)**
[Face cam]
"Quick intro: I'm a software engineer, and this channel is AI Made Usable. I test AI on real work so you don't have to.
Here are the rules, so this is fair. [Rules graphic, 5 bullets] Same prompt, word for word. Fresh chat. I'm using the model each app gives me on my plan, which is {plan per app}. You'll see the model picker. At most one follow-up, and the same one for all three. I don't edit anything. And every task has a score I can prove: links either open or they don't, the app either runs or it doesn't, and the spreadsheet has answers I hid in it myself."

**1:30 TASK 1: WORK EMAIL (≈2 min)**
[Show the messy notes, then paste the prompt into each app side by side]
"Task one is the thing most of us use AI for every day: turning messy notes into an email. There are six facts in these notes. The rule is to keep every fact and invent nothing.
[Highlight the facts as checked/missed]
ChatGPT: {result: facts kept / anything added}. Claude: {result}. Gemini: {result}.
The one I'd actually send is {winner}, because {reason}. Scores: {x / y / z}."

**3:30 TASK 2: RESEARCH WITH SOURCES (≈2.5 min)**
[Click every link on camera]
"Task two is where AI usually gets you in trouble: research with sources. I asked for three laptops under seventy thousand rupees with links. And I'm going to click every single link.
{per app: how many links worked, any wrong prices or models}.
This is the most important lesson of the video: {lesson, e.g. 'a confident answer isn't a checked answer'}. Scores: {x / y / z}."

**6:00 TASK 3: SPREADSHEET (≈3 min)**
[Show the CSV, then the answer-key graphic: three hidden insights, revealed after]
"Task three. I made a sales dataset for a small shop, three months of data, and I hid three real problems in it. I know the exact answers, so the AIs can't bluff.
[Each app's insights + chart]
{per app: which insights found, any made-up numbers}.
Here's what was hidden: [reveal] sales are about 66 percent higher on weekends, the East region dropped 52 percent from July to September, and headphones have a 23 percent return rate. Everything else is under 4 percent.
{who found what}. Scores: {x / y / z}."

**9:00 TASK 4: BUILD AN APP (≈2.5 min)**
[Open each HTML file in the browser, click through the features, refresh the page]
"Task four is for everyone who thinks you need to code to build things. I asked each AI for a habit tracker in one file. Then I open it, test every feature and refresh the page to see if it remembers.
{per app: ran first try? features working? needed the fix prompt?}
As an engineer, here's what I'd tell you about the code: {one honest note, e.g. 'fine for personal use, not something I'd ship to customers without review'}. Scores: {x / y / z}."

**11:30 TASK 5: LEARN SOMETHING (≈1.5 min)**
[Answer the quiz live, get one question wrong on purpose]
"Last task: learning. I asked each one to explain AI agents to a 15-year-old, then quiz me one question at a time. I'm going to get one wrong on purpose to see how it handles it.
{per app: stayed under 150 words? asked one question at a time? graded correctly?} Scores: {x / y / z}."

**13:00 RESULTS (≈1.5 min)**
[Full scoreboard animation]
"Final scores out of fifty: ChatGPT {total}, Claude {total}, Gemini {total}.
But here's the thing: the total isn't the point. Here's what I'd actually use each one for:
[Decision card] For {task type}, use {app}. For {task type}, use {app}. For {task type}, use {app}.
And the surprise I mentioned: {the surprising result}."

**14:30 OUTRO + CTA (≈30 s)**
"If you only take one thing from this: {single takeaway}.
Every Tuesday I test AI on real work like this. Next, {next video topic}. Subscribe so you don't miss it. And tell me in the comments: which task should I test next?"

## Visual direction & editing notes
- **Format:** 16:9, 1080p+. Face cam in a corner during tests. Full face cam for the hook, rules, results and outro.
- **Screen recording:** each app at the same zoom (125%), dark mode if available. Hide personal info (email, avatar, chat history sidebar).
- **Graphics (Claude makes these in brand style):** rules card, per-task score tag, three-insight reveal, final scoreboard, "which AI for what" decision card, lower-third "AI Made Usable".
- **Pacing:** cut waiting/typing to ≤2 s (speed ramps). Show each output long enough to read the key lines (zoom + highlight).
- **Audio:** phone or USB mic, quiet room, 30 cm from the mouth. Claude cleans it (noise reduction, loudness −14 LUFS).
- **Music:** low, royalty-free, ducked under the voice.
- **Honesty rule:** never re-run a task to get a better result. If something fails, keep it in. That's the content.

## Packaging
**Title options (pick one; Test & Compare thumbnails, not titles):**
1. ⭐ `ChatGPT vs Claude vs Gemini: I Tested All 3 on Real Work` (55 chars)
2. `Which AI Should You Use? ChatGPT vs Claude vs Gemini Tested` (58)
3. `I Gave ChatGPT, Claude & Gemini the Same 5 Real Tasks` (52)

**Thumbnail:** `assets/SWAI-L001/thumbnail-a.png` (no face, ready now). Recommended variant B: the same layout with the creator's face (curious look) on the right. This needs one photo, and Claude will composite it (tests H-VIS-2).

**Description (first 2 lines show above the fold):**
```
I gave ChatGPT, Claude and Gemini the exact same 5 real tasks: an email, research with sources, a spreadsheet with hidden answers, a mini app, and learning something new. Here's which AI to use for what.

Rules: same prompt, fresh chat, one follow-up max, nothing edited. Models used: {fill in: model + plan for each app}.

⏱ Chapters
0:00 Which AI should you use?
0:30 The rules
1:30 Task 1: Work email
3:30 Task 2: Research with sources
6:00 Task 3: Spreadsheet analysis
9:00 Task 4: Build an app (no code)
11:30 Task 5: Learn something new
13:00 Final scores + which AI for what

📂 Try the spreadsheet test yourself: {link to the CSV once hosted}

AI Made Usable: Discover. Build. Automate. Ship.
New videos every Tuesday.

#ChatGPT #Claude #Gemini
```
(Chapter times are estimates. Update them after the edit.)

**Tags:** ChatGPT vs Claude vs Gemini, which AI to use, best AI 2026, GPT-6 Astra, Claude Opus 5.5, Gemini 4, AI comparison, AI for beginners, AI tools, AI Made Usable

**End screen:** subscribe + "Best for viewer". Pinned comment: "Which task should I test next? 👇"

## Shorts from this video
- SWAI-S003 (Tue, after publish): the spreadsheet reveal.
- Later, after results: one Short per surprising task result (IDs assigned when written).

## Publishing checklist
- [ ] Scripts approved by the creator (approval_status → APPROVED)
- [ ] Test recorded following the protocol; scoreboard filled; `{ }` placeholders replaced with real results
- [ ] Facts double-checked: model names shown match what was used
- [ ] Edit done; chapters updated to real times
- [ ] Thumbnail chosen (A or B); Test & Compare set up with both
- [ ] AI-disclosure check: no realistic synthetic people/voices, so the "altered content" toggle = No
- [ ] Upload: title, description, tags, category Science & Technology, not made for kids, end screen, pinned comment
- [ ] Schedule: **Tuesday 2026-11-24, 19:30 IST**
- [ ] After publish: Claude records the `video_url` and pulls performance at +48 h, +7 d, +28 d

## Performance
| Pulled | Window | Views | Watch time (h) | Avg view duration | Avg % viewed | Likes | Comments | Shares | Subs + / − | Top traffic sources |
|---|---|---|---|---|---|---|---|---|---|---|

## Lessons learned
