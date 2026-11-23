---
id: SWAI-L001
format: long
topic: "The AI Showdown: ChatGPT vs Claude vs Gemini in 5 real-life rounds (game-show format, funny, ~8–9 min)"
segments: [BEG, PRO, STU, BIZ]
pillar: "Discover (DEC-010 proposed)"
objective: reach
hypothesis: "If our first video is a fast, funny game show with checkable results (not a dry comparison), then viewers stay longer than in typical comparison videos (avg % viewed ≥45%) and the 5 rounds work as standalone Shorts that feed the long video."
title: "I Made ChatGPT, Claude & Gemini Compete in 5 Real Tasks"
hook: "Three AIs. Five real tasks. One spreadsheet with answers I hid myself. Nobody gets to bluff. Welcome to the AI Showdown."
production_status: SCRIPTED
approval_status: PROPOSED
publish_date: "2026-11-28"
video_url: ""
experiments: []
created: 2026-11-21
updated: 2026-11-21
---

> **v2 (2026-11-21)** at the creator's request: "not too long, not boring, interesting, casual, AI jokes, learning + fun". The format changed from a ~15-min straight comparison to an **~8–9 min game show**. The test protocol is unchanged (still verifiable). Research: `research/competitors/snapshots/2026-11-21-l001-format-research.md`. v1 is in git history.
> Working assumptions: pillar/segments use Claude's recommended defaults (DEC-010/011 still PROPOSED).

## Research
- FACT · "I Tested AI…" challenge videos are the biggest format nearby: 5–10M views (Vlad and Chris, Sambucha, HopeScope). They lead with humour.
- FACT · Comparison videos that worked are **7–13 min**: Parker Prompts "I Tested Gemini vs Claude vs ChatGPT So You Don't Have To" 211K at 8:51; "$20 plan" versions 267K–733K.
- FACT · GPT-6 Astra (2026-09-03), Claude Opus 5.5 (2026-09-22), Gemini 4 (2026-09-30 → 11-18): three new flagships in under 3 months, so "which one?" is the question of the moment. Sources in `research/market/ai-landscape.md`.
- Our angle: the **game show** (energy) + **checkable answers** (trust) + **an engineer's quick verdict** (credibility).
- ⚠️ Show each app's model picker on screen and name only the model actually used.
- 2026-11-21 · The ChatGPT UI no longer shows the model name. Use "ChatGPT default model on the **Go** plan (paid), Nov 2026" in the video and description. Don't ask the AI which model it is (unreliable). Models used: each app's **default** (ChatGPT Go default · Claude Opus 5.5 Medium/Auto · Gemini 4 Hydrogen). Keep defaults for every round so it's consistent, and say "the model each app gave me by default" on screen. Plans (creator, 2026-11-22): ChatGPT = **Go (paid)**, Claude = **paid (₹2,499/month)**, Gemini = **paid (bundled with a Jio recharge)**. All three are paid tiers, which makes the comparison fair. On screen: "all three on paid plans".

## Competitor references
- Parker Prompts: "I Tested Gemini vs Claude vs ChatGPT So You Don't Have To" (211K, 8:51): closest format, without humour or verifiable tasks.
- Vlad and Chris: "I Tested AI Experiments" (8.9M): energy and reactions.
- Jeff Su: "When to use ChatGPT, Gemini, and Claude" (Short, 234K): the decision-card payoff.

## The game (test protocol: unchanged, keeps it honest)
**Rules (on screen as "The Rulebook"):** same prompt word-for-word · fresh chat · the model each app gives on your plan (show the picker) · max 1 follow-up, the same for all · no re-runs, no editing · score each round 0–10 with the rubric.

| Round | Name on screen | Exact prompt (copy-paste) | Scoring (0–10) |
|---|---|---|---|
| 1 | **The Boss Email** | `Turn these messy notes into a short, professional update email to my manager. Keep every fact, don't add any. Notes: launch moved from 3 Dec to 10 Dec because payment testing found 2 bugs; both fixed, retesting Thursday; marketing needs new date by Friday; budget unchanged; need approval for 1 extra QA day (₹8,000).` | 4 = all 6 facts, 3 = invents nothing, 3 = ready to send |
| 2 | **Trust Me Bro (Sources)** | `Compare 3 laptops under ₹70,000 that a college student in India can buy right now. Give a table with price, battery life, weight, and a link to a source for each.` | 4 = links open and match (click all), 3 = plausible current prices, 3 = useful pick. −2 per dead/wrong link |
| 3 | **The Hidden Problems** | Upload `assets/SWAI-L001/test-data-sales.csv`, then: `I run a small shop. Find the 3 most important insights in this sales data and show one chart.` | 3 per planted insight (weekend +66%, East −52%, Headphones 22.8% returns, see `answer-key.md`), +1 correct chart, −1 per invented number |
| 4 | **Build Me an App** | `Build a habit tracker as a single HTML file: add habits, tick off each day of the current week, show a streak count, and save in the browser so it remains after refresh.` | 4 = runs first try, 4 = features (add, tick, streak, saves), 2 = looks clean. Allowed follow-up: "fix any bugs" |
| 5 | **Teach Me Like I'm 15** | `Explain how AI agents work to a 15-year-old in under 150 words. Then give me a 3-question quiz, one question at a time, and wait for my answer before the next.` | 4 = accurate + simple, 3 = word limit, 3 = quizzes one at a time and grades. Get one answer wrong on purpose |

**Scoreboard (fill in while recording):**
| Round | ChatGPT | Claude | Gemini | Funniest moment (timestamp) |
|---|---|---|---|---|
| 1 Boss Email | **9** (official recorded run 2026-11-22, 18 s: all 7 facts kept; added "so we can proceed with the retesting", a small invented link → −1. An earlier unrecorded run scored 10 and is not used) | **10** (recorded 2026-11-22, 15.7 s, model shown on screen: Opus 5.5 · Medium: all 7 facts, nothing invented, subject line + "Send via Gmail", flagged the "confirmed by Friday" wording for the user to check) | **10** (recorded 2026-11-22, 11.4 s, model shown: **Hydrogen** (Gemini 4 everyday tier): all 7 facts, nothing invented, no name in the signature, rendered as a native **Gmail draft** card) | ChatGPT: the reply area sits blank with only icons for a moment, then a loader, then the email card (~25–65% of the clip) → joke: "thought about it, said nothing, then changed its mind" · Claude: status text "Untangling…" while thinking; then says "all **five** facts" when there were seven → joke: "even Claude can't count all my problems". ⚠️ **PRIVACY: Claude signed the email with the creator's real first name. Blur the signature line in the edit.** · Gemini: fastest (11 s), went straight into a Gmail draft → joke: "Gemini didn't even think about it. Straight to Gmail." Crop out the browser permission pop-up (top-left) at the start. |
| 2 Sources | **6** (answer recorded 2026-11-23, 36 s; link check recorded the same day, 76.5 s. **ASUS Vivobook S14**: ChatGPT said ₹65,990, but its own shopping panel + the Shopsy page opened at **₹78,176** (MRP ₹92,990), over the ₹70k budget. **Acer Aspire Pro AP14-55**: said ₹69,999, panel shows Amazon ₹61,975 / Croma ₹72,990, Croma page opened (location pop-up). **Acer Aspire 15**: panel showed no seller price, unverifiable. No dead links. Score: links open but 1 of 3 price claims contradicted by its own source 2/4 · prices 1/3 · usefulness 3/3. Caveat: retail prices change daily; both checks were on 2026-11-23) | **7** (recorded 2026-11-23, 66.6 s, prompt + clicks in one take. **Apple MacBook Neo** ₹69,900: the 91mobiles page shows ₹69,900 but "**Out of Stock**… not available in any online store", which fails "buy right now". **ASUS Vivobook S14 M3407KA** ₹67,990: Cashify "starting price ₹67,990" ✓. **Lenovo IdeaPad Slim 3 15IRH10** ₹62,490: the MySmartPrice page shows lowest **₹76,499** (Amazon) ✗, but Claude itself warned "Watch the price… gone up to ₹81,900" and "check the live price… especially for the Lenovo". No dead links. Score: links 2/4 · prices 2/3 (1 exact, 1 flagged as uncertain) · usefulness 3/3) | **10** (recorded 2026-11-23, 80 s, one take. **ASUS Vivobook 16 X1605VA** ₹60,999 → Gadgets Now page ₹60,999 ✓ (1.88 kg ✓). **HP 15-fc0704AU** ₹42,990 → Gadgets Now ₹42,990 ✓ (1.59 kg ✓). **Lenovo IdeaPad Slim 3 15IRU8** ₹54,900 → Amazon ₹54,900 ✓ (1.6 kg vs 1.62 claimed). All three under budget, buyable, prices match the sources exactly. Battery given as hours + Wh. Caveat: cheaper, lower-spec picks (8GB / i3) than the others, and the Gadgets Now product pages show 1.0★ ratings) | ChatGPT: gave the battery as 70Wh (size, not hours) but admitted it ("ASUS publishes capacity, not a comparable runtime") · ended with an interactive quiz + "Find my best laptop" button → joke: "I asked for a table. It gave me a quiz." · Price twist: "Under ₹70,000, it said. The store disagreed by eight thousand rupees." / "₹65,990 in the chat, ₹78,176 in the shop. That's not a discount, that's a plot twist." · Claude R2: recommended a MacBook the source says you can't buy → joke: "Top pick: a laptop that is, quote, not available in any online store." · but it warned me about the Lenovo price itself → "Claude basically said: don't trust me, check. Fair." · Gemini R2: every link matched to the rupee → "Gemini clicked-checked: three for three. I had nothing to roast. I'm upset." |
| 3 Hidden Problems | **5** (redo 2026-11-23, 67.7 s, CSV attached. Insights: revenue falling every month −14.35% (₹42.09L→₹40.69L→₹36.05L ✓ exact), Headphones 22.79% returns ✓, Headphones+Backpack = 56.4% of revenue ✓. Missed the East region and the weekend effect. Correct monthly bar chart. All numbers verified against the data. 3 + 1 (decline found, not the region) + 0 + chart 1) | **4** (51 s: went straight to the planted East problem with a weekly revenue-by-region line chart (East ~₹1.96L/wk → ~₹1L/wk ✓, "zero headphones on 28 and 30 Sept" ✓ verified) but the visible answer gives **only that one insight**. Thinking showed it checked headphone returns, yet didn't report them. 3 + chart 1. ⚠️ Confirm with the creator that nothing above the chart was cut off) | **6** (96 s: Headphones 22.8% returns + ₹7.92L lost ✓, monthly decline 14.4% ✓ with return rate rising 3.8→4.1→4.8% ✓, East "underperforms by a third" ₹21.59L / 18.2% ✓ (found the region, not the trend). Interactive dashboard + product ledger. All numbers verified. 3 + 2 + 0 + chart 1) | Nobody found the weekend effect (+66%) → joke: "Not one AI noticed people shop more on weekends. Apparently AIs don't get weekends." · First attempt blooper: all three said "no file attached" |
| 4 Build an App | **10** (new run 2026-11-23, 88 s: downloadable "Weekly Habit Tracker", opened, habits added + ticked, streak 1 ✓. Claude's scripted test (`production/apptest/habit-test.js`, real Chromium): add 2 → tick today → reload = **all persisted**, 0 errors. Future days disabled) | **10** (new run, 118 s: in-app habits added + ticked, 🔥 1 day + "best 1" ✓. Scripted test: **all persisted**, 0 errors. Future days disabled, week navigation, storage-failure warning. Said honestly "checked for syntax errors but haven't clicked through it". The first attempt's in-app add failure did not reproduce) | **8** (new run, 59 s: prettiest UI. Scripted test passes and persists. −2: it **pre-fills 3 fake habits with fake history** (a "3-day water streak" before you did anything) and **lets you tick future days** (Tue/Wed ticked on Monday). Also needs the Tailwind CDN, so it's not truly offline/single-file) | Jokes: "Gemini gave me a 3-day water streak before I drank anything." · "Gemini lets you complete Wednesday on Monday. Productivity unlocked." · Engineer verdict: all three work. ChatGPT and Claude are the safer code, Gemini the prettiest |
| 5 Teach Me | **10** (recorded 2026-11-23, 62.9 s: 5-step agent loop (plan → use tools → take action → learn from results) + "AI agent = Brain (LLM) + Tools + Memory + Planning + Actions"; interactive "AI Agents Quiz" card, one question at a time ✓, waited ✓. Q1 B ✓, Q2 Tools C ✓, Q3 answered A on purpose → "Not quite! correct is B…" with a travel-budget example ✓, final 2/3 table. Graded correctly. ⚠️ Top of the explanation is cut off in the recording, so the <150-word limit could not be fully counted; visible part fits. Check the full clip before the final edit) | **10** (recorded 2026-11-23, 45.7 s: "plan a cheap weekend trip to Jaipur" example, Think → Act → Observe → Repeat, "like a smart intern" ✓ under 150 words. One question at a time ✓. Q1 b ✓ "That's right!", Q2 D (wrong on purpose) → "Not quite. The answer is B… Observe step" ✓, Q3 A ✓, "Final score: 2 out of 3" + tip on the missed step ✓) | **10** (recorded 2026-11-23, 64.5 s: "brain in a jar" explanation, 3-option questions one at a time ✓. Q1 B "Spot on!" ✓. Q2 the creator typed **D** (no D exists) → "Haha, nice try—there is no D! The options are A, B, or C." ✓ handled gracefully; then B wrong → explained hallucination, correct C ✓. Q3 B wrong → correct A) Tools ✓, "1 out of 3" ✓) | Gemini: "Haha, nice try—there is no D!" → joke: "I tried to cheat the quiz. Gemini caught me." · ChatGPT built a whole quiz app with a score table. Overkill, very ChatGPT · Claude: "smart intern" → joke: "Claude describing itself, basically" · Round 5 is a three-way tie: all taught well and graded honestly |
| **Total /50** | **40** | **41** | **44** 🏆 | Winner: **Gemini** (won on Round 2 sources, lost points on Round 4 fake data). Claude 2nd by 1 point over ChatGPT |

## Script (creator's voice, casual: ~550 fixed words + ~400–500 words of real results ≈ 8–9 min with demo time)
Narrated by the creator's **voice clone** (DEC-020, faceless). Tone: talking to a friend, quick, a bit cheeky. Jokes are about what the AIs actually did on screen, never claims about the companies. `{ }` = fill in from the real recording only. **[SFX]** = sound effect. **[MEME]** = a reaction overlay (zoom-in, freeze-frame, emoji stamp, text pop) placed by Claude in the edit. No face on camera.

**0:00 COLD OPEN (≈15 s)**
[The funniest real fail from the recording, 3–4 s, then freeze-frame + record-scratch SFX]
"Yep. That's an AI, confidently doing {the fail}. Let me explain how we got here."

**0:15 HOOK + INTRO (≈35 s)**
[Game-show title card: "THE AI SHOWDOWN" · drum roll SFX]
"Three AIs. Five real tasks. And one spreadsheet with answers I hid myself, so nobody gets to bluff.
In this corner, ChatGPT: the famous one. Your uncle uses it. Your boss uses it. Your boss's uncle uses it.
Claude: the polite one. It apologises so much I'm pretty sure it's Canadian.
And Gemini: Google's one. It has the entire internet at home.
I'm a software engineer, and I've spent more time arguing with AI than with my family. Let's go."

**0:50 THE RULEBOOK (≈20 s)**
[Rules card, fast]
"Rules. Same prompt. Fresh chat. One follow-up, max. No re-runs, no editing. If an AI embarrasses itself, it stays in the video. That's the deal."

**1:10 ROUND 1: THE BOSS EMAIL (≈75 s)**
[Messy notes on screen → three outputs side by side, the 6 facts tick ✓/✗]
"Round one: the thing everyone actually uses AI for, turning chaos into an email your manager won't laugh at. Six facts. Keep all six. Add nothing.
{per AI result}.
Joke bank, pick what really happened:
- adds a fact → "I said don't add anything. It added {thing}. Nobody invited it."
- way too long → "I asked for an email. It wrote a LinkedIn post."
- perfect → "Honestly? I'd send this. My manager would think I'm finally organised."
Scores: {x / y / z}. [SFX ding]"

**2:25 ROUND 2: TRUST ME BRO (≈90 s)**
[Click every link on camera. ✓ / ✗ stamps]
"Round two. I asked for laptops under seventy thousand rupees, with sources. And I'm going to click every single link, because AI links are like gym memberships: they look great until you actually use them.
{per AI: how many links worked, any wrong models/prices}.
Joke bank:
- dead link → "This link goes nowhere. Like my New Year's resolutions."
- wrong price → "That price is from a parallel universe. Lovely place. Doesn't ship to India."
- all links work → "All links work. I'm genuinely shocked. Someone write this down."
The lesson, and I mean this: a confident answer is not a checked answer. Scores: {x / y / z}."

**3:55 ROUND 3: THE HIDDEN PROBLEMS (≈100 s)**
[CSV scrolls; three "🔒" padlocks]
"Round three, my favourite. I made a sales spreadsheet for a small shop and hid three problems inside it. I know the exact answers. No bluffing possible.
[Each AI's insights + chart, padlocks unlock when found]
{who found what, any invented numbers}.
Joke bank:
- invents a number → "That number doesn't exist anywhere in the file. That's not analysis, that's fan fiction."
- finds all three → "All three. My accountant just got nervous."
- finds none → "It looked at three months of data and said 'sales happened'. Thanks."
[Reveal card] The answers: weekends sell sixty-six percent more, the East region dropped fifty-two percent, and headphones get returned almost a quarter of the time. Scores: {x / y / z}."

**5:35 ROUND 4: BUILD ME AN APP (≈85 s)**
[Open each HTML file, click everything, refresh the page: the moment of truth]
"Round four. No coding. One prompt. Build me a habit tracker that remembers my habits after I refresh the page.
{per AI: runs first try? features? needed the fix?}
Joke bank:
- crashes → "It built an app with one feature: disappointment."
- forgets after refresh → "It has the memory of a goldfish. A very well-designed goldfish."
- works first try → "It works. It saves. I'm now tracking one habit: testing AI."
Engineer's verdict, ten seconds: {e.g. "fine for you, not for 10,000 customers, so get it reviewed before you sell it"}. Scores: {x / y / z}."

**7:00 ROUND 5: TEACH ME LIKE I'M 15 (≈55 s)**
[Live quiz screen recording. Creator types one wrong answer on purpose. MEME overlay on the AI's response]
"Last round. Explain AI agents to a fifteen-year-old, then quiz me. I'm getting one wrong on purpose.
{how each handled it: one question at a time? graded fairly? under 150 words?}
Joke bank:
- gentle correction → "It corrected me more kindly than any teacher I ever had."
- dumps all questions at once → "I asked for one question at a time. It gave me the whole exam. Board exam flashbacks."
Scores: {x / y / z}."

**7:55 FINAL SCOREBOARD (≈40 s)**
[Animated scoreboard + drum roll + confetti SFX]
"Final scores, out of fifty: ChatGPT {n}, Claude {n}, Gemini {n}. The winner gets… absolutely nothing. It's software.
But here's what actually matters: [Decision card] for {task} use {AI}, for {task} use {AI}, for {task} use {AI}.
And the biggest surprise: {surprise}."

**8:35 OUTRO (≈20 s)**
"So, which AI is best? Honestly, the one you double-check. I'm AI Made Usable: every week I test AI on real stuff so you don't waste your time. Comment which task I should throw at them next. And subscribe, before Gemini answers for you."

## Visual direction & editing notes
- **Game-show package (Claude builds it):** "THE AI SHOWDOWN" title card, contestant cards (name tiles, no company logos needed), round title cards, ✓/✗ stamps, padlock unlocks, animated scoreboard, decision card, "AI Made Usable" lower third.
- **Pace:** cut every pause. Speed-ramp the AI "thinking". No shot longer than ~4 s without a change (zoom, highlight, stamp, cut to face).
- **No face cam (DEC-020).** Energy comes from motion graphics, MEME overlays (freeze-frame, zoom punch-in, emoji stamps), SFX and fast cuts. The intro and verdicts use full-screen graphic cards.
- **SFX (royalty-free):** drum roll, ding, buzzer, record scratch, confetti. Low background music, ducked under the voice.
- **Screen hygiene:** same zoom (125%) in all apps. Hide email, avatar and chat history.
- **Honesty:** never re-run a task for a better result. Fails stay in, they're the comedy.
- **Audio:** the voice clone via the ElevenLabs connector (Claude generates it per section), then mixed at −14 LUFS with music + SFX.

## Packaging
**Title options (finalise after recording; must match what happened):**
1. ⭐ `I Made ChatGPT, Claude & Gemini Compete in 5 Real Tasks` (54)
2. `ChatGPT vs Claude vs Gemini: The AI Showdown (5 Real Tasks)` (58)
3. `{Loser} Embarrassed Itself. ChatGPT vs Claude vs Gemini` (only if true)

**Thumbnail:** A (ready): `assets/SWAI-L001/thumbnail-a.png`. Faceless channel (DEC-020): variant B uses the funniest real AI fail screenshot in the slot instead of a face.

**Description:**
```
I made ChatGPT, Claude and Gemini compete in 5 real tasks: a boss email, research with sources, a spreadsheet with hidden answers, building an app, and teaching me something. Same prompts, no re-runs, nothing edited.

Models used: {fill in model + plan per app}

⏱ Chapters
0:00 That moment
0:15 Meet the contestants
0:50 The rules
1:10 Round 1: The Boss Email
2:25 Round 2: Trust Me Bro (sources)
3:55 Round 3: The Hidden Problems
5:35 Round 4: Build Me an App
7:00 Round 5: Teach Me Like I'm 15
7:55 Final scores + which AI for what

AI Made Usable: Discover. Build. Automate. Ship.
New videos every Tuesday.

#ChatGPT #Claude #Gemini
```
(Update chapter times after the edit.)

**Tags:** ChatGPT vs Claude vs Gemini, AI showdown, which AI is best, GPT-6 Astra, Claude Opus 5.5, Gemini 4, AI test, AI for beginners, funny AI test, AI Made Usable

## Shorts from this video (7)
SWAI-S001 teaser (Sun) · S002 Round 1 (Mon) · S003 Round 3 (Tue) · S006 Round 2 (Wed) · S008 Round 4 (Thu) · S009 Round 5 (Fri) · S010 final cheat sheet (Sat).

## Publishing checklist
- [ ] Script approved by the creator
- [ ] **Creator screen-records the test on Sunday 11-22** (laptop or phone screen recording, no face/mic), fills in the scoreboard, notes the funniest moments
- [ ] Claude fills in the `{ }` results, generates the narration with the voice clone, and the creator listens and approves
- [ ] Claude edits: package graphics, SFX, captions, chapters, thumbnail B
- [ ] AI disclosure: **Altered content = Yes** (cloned own voice, DEC-020)
- [ ] Upload + schedule **Tuesday 2026-11-24, 19:30 IST**. Title/thumbnail Test & Compare A/B
- [ ] Pinned comment: "Which task should I throw at them next? 👇"

## Performance
| Pulled | Window | Views | Watch time (h) | Avg view duration | Avg % viewed | Likes | Comments | Shares | Subs + / − | Top traffic sources |
|---|---|---|---|---|---|---|---|---|---|---|

## Lessons learned
