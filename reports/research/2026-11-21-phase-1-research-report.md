# Phase 1 research report: ShippedWithAI

**Date:** 2026-11-21 · **Status:** for the creator's review. Every recommendation here is PROPOSED (DEC-005, 006, 008–016). Nothing is approved by this report.
**Labels:** **FACT** = observed, dated, sourced · **HYPOTHESIS** = inference to test · **REC** = recommendation.

## 0. Method and limits
- **Competitors:** 24 YouTube searches across 10 segments (600 results, 49 without metadata), then deep dives into **34 channels** (subscribers, latest ~30 long-form + ~30 Shorts with views, exact dates of the latest 15 uploads via RSS), plus visual review of the top thumbnail per channel (24). Raw data: `research/competitors/snapshots/2026-11-21-phase1-channel-scan.md`. Registry: `research/competitors/channels.md`.
- **Market:** 14 web searches across models, coding tools, agents, business, work, education, creators, platform policy and India. Entries with links: `research/market/ai-landscape.md`.
- **Not possible in this pass (FACT):** YouTube per-video pages are blocked by a bot check, so there are **no transcripts (hooks/structure), no comments, no like counts**. List-mode views are rounded and have no dates. Growth over time can't be measured (no history). Google Trends, Reddit and Hacker News are blocked by the network policy. Hooks and storytelling were therefore **not** analysed. Audience "needs" come from titles and surveys, not viewer comments. This is a search/title/thumbnail-level analysis, not a full video analysis.
- Many survey sources are vendor-run (Zapier, CrewAI, AIR, Metricool), so they are flagged as such.

## 1. What the research discovered (headline findings)
1. **FACT:** The biggest AI videos in late 2026 are **"use AI better" and "build with AI, no code"** content for non-developers, not developer content. Examples: Jeff Su "AI Agents, Clearly Explained" 5.79M, Sandeep Swadia "Use Claude Better Than 99%" 2.6M, Metics Media "Build Your First AI Agent (No Coding)" 877K, Tina Huang "Vibe Coding Fundamentals" 1.13M.
2. **FACT:** **Expertise-compression packaging** recurs across ≥6 channels at 0.5–5.8M views: "Learn 80% of X in N minutes", "Better than 99% of people", "Clearly Explained".
3. **FACT:** **AI news is a frequency race.** Matt Wolfe and Matthew Berman post ~10/week with medians of 137–157K. Fireship (4.34M subs) dominates the dev-news angle.
4. **FACT:** **Shorts underperform long-form on views for almost every AI channel.** Across the 25 channels with ≥5 recent Shorts, the median Short reaches **11%** (range 3–72%) of the median long-form views. 23 of 25 are below 34%, and only Kevin Stratvert (58%) and Fireship (72%) are higher. The best AI Shorts are single concrete tips/demos (Greg Isenberg "10x your Claude with 4 .md files" 846K; Riley Brown 639K).
5. **FACT:** **Frequency ≠ performance for education channels.** Jeff Su posts ~0.6/week and has one of the highest medians (~268K). Justin Sung posts ~0.8/week with a 154K median.
6. **FACT:** The market moved fast in Sep–Nov 2026: GPT-6 Astra (09-03), Gemini 4 family (09-30 → Neon 11-18), Claude Opus 5.5 (09-22), Anthropic IPO (11-19). Claude Code leads developer workplace adoption (39%, JetBrains). ~half of US workers use AI, but only ~30% weekly (Gallup).
7. **FACT:** YouTube policy: "inauthentic content" (Jul 2026) demonetizes mass-produced repetitive AI content. A cloned own-voice narration requires an AI disclosure. Views count from the first frame since 2026-08-24, and the YPP thresholds are reported to double from Feb 2027.

## 2. Competitors across segments (summary)
Full table: `research/competitors/channels.md`.

| Segment | Leaders observed (subs) | Formats that win (FACT) | Opening for us (HYPOTHESIS) |
|---|---|---|---|
| PRO / BEG | Jeff Su (1.96M), Kevin Stratvert (4.5M), Futurepedia (773K), Metics Media (775K) | Clearly-explained concepts, "learn 80%", step-by-step tool tutorials | An engineer explaining *why* it works and where it fails, with real builds rather than feature tours |
| BIZ / STARTUP | Dan Martell (3.17M), Greg Isenberg (745K), Liam Ottley (871K), Nick Saraev (640K), Nate Herk (1.14M) | 1-person business with AI, agents/automation courses, experiments | Actually shipping working automations for small businesses, honestly |
| DEV / SWE | Fireship (4.34M), Tech With Tim (2.12M), JS Mastery (1.28M), Riley Brown (315K) | Long build courses, "how senior engineers build with AI", vibe coding | Our strongest credibility, but the most crowded. Use as the trust anchor. |
| ENT | Matt Wolfe (1.03M), Matthew Berman (646K), Wes Roth (336K), AI Explained (460K) | High-frequency news, dramatic framing, deep analysis | Avoid the race. Do weekly "what changed for builders" at most. |
| STU | Justin Sung (2.31M), Tina Huang (1.38M), Ali Abdaal (6.71M) | Learning science, roadmaps, AI as a study tool | Learning roadmaps by role (OPP-014), not study hacks |
| CRE | Dan Kieft (332K), Youri van Hofwegen (343K), Modern Millie (801K) | AI video tutorials, content systems | "How we run this channel with AI" as a real case study (OPP-013) |
| FRE | Patrick Dang (434K), Vaibhav Sisinty (890K) | Side hustles, money promises | Anti-hype real projects with real numbers (OPP-015) |
| ADV | IBM Technology (1.85M), KodeKloud, codebasics (1.59M) | Concise concept explainers, fundamentals | Deep long-form on agents, monthly |
| India | Vaibhav Sisinty, Satish Dhawale (Hindi masterclasses, 5.8M top), codebasics, Tejas AI | News + tools, very long courses | English-first global (DEC-001). Note: Hindi long courses are a separate large market. |

**Frequency (FACT, RSS window):** news/business channels post 5–26/week (mostly Shorts). Top education channels post 0.6–1.3/week.

## 3. AI market landscape across the four proposed pillars
Details and links: `research/market/ai-landscape.md`.

| Pillar | Current state (FACT) | Content implication (HYPOTHESIS) |
|---|---|---|
| **Discover** | 3 flagship families in 10 weeks (GPT-6 Astra, Gemini 4, Claude Opus 5.5). Many version names in creator titles are unverified. Local AI is popular. | Evergreen **decision guides** ("which AI for which job") and clear explainers outperform raw news for a new channel |
| **Build** | Claude Code 39% dev adoption. "Vibe coding"/no-code app building is mainstream content. Sora exited video, while Seedance and Veo lead | Engineer-guided "build it yourself" for non-coders, with honest quality checks |
| **Automate** | Agents widely piloted (71–88% in vendor surveys), but only 5% of orgs report being ready (Deloitte). Automation courses do 1.3–2.7M views | Real, small, working automations beat "replace your team" hype |
| **Ship** | Anthropic IPO, "1-person business with AI" narratives. YPP thresholds rising | Real outcomes and case studies (including our own channel's numbers) build trust |

## 4. Audience segments: validation and priority (REC → DEC-011)
`research/audience/segments.md` has the full evidence table.
- **Primary:** PRO + BEG + BIZ/STARTUP. They have the largest observed demand, and the same "build/automate it with AI" topic serves all three when explained clearly.
- **Secondary:** DEV/SWE (credibility; occasional deep builds), FRE (anti-hype), ADV (monthly deep dives).
- **Tertiary:** STU, CRE (via roadmaps and our own case study).
- **Avoid:** ENT daily news.
- **The positioning bridge (HYPOTHESIS):** "AI for everyone, explained by an engineer who ships." Non-developer outcomes plus engineering credibility plus honesty about what breaks. No observed channel combines all three.

## 5. Content pillar recommendations (REC → DEC-010, DEC-016)
| Pillar | Proposed definition | Share | Example formats | Primary segments |
|---|---|---|---|---|
| **Build** | Make real things with AI, no-code → code, with an engineer's verdict | 35% | "Learn 80% of Claude Code for non-developers", "I let AI build X: an engineer's review" | BEG, PRO, BIZ, DEV |
| **Automate** | Working AI workflows and agents for work and small business | 30% | "Your first useful AI agent (no code)", "Automate one real business process" | PRO, BIZ, FRE |
| **Discover** | Explain concepts and choose tools (decision guides), **not** daily news | 25% | "X, Clearly Explained", "ChatGPT vs Gemini vs Claude: which for what" | BEG, PRO, STU, ENT |
| **Ship** | Outcomes: launching, earning, real results, our own channel's journey | 10% | Case studies, "what it actually earned/cost" | BIZ, FRE, CRE |

What to publish first (topic shortlist only, no calendar per instructions): OPP-006 (which AI for which job), OPP-007 (first useful agent), OPP-008 (Claude Code for non-developers), OPP-001 (AI builds a SaaS, engineer reviews), OPP-014 (AI roadmap by role). See `research/opportunities.md`.

## 6. Shorts ↔ long-form (REC → DEC-012, DEC-013)
- **Evidence (FACT):** the Shorts view share is low across the niche (§1.4). Vendor studies suggest a mixed strategy helps, at roughly 25–40% of uploads or ~5/month (not peer-reviewed). Repetitive AI mass production is demonetizable.
- **Recommendation:**
  1. Shorts are mostly **standalone single-idea tips/demos** (the best-performing type), each tied to a long-form "go deeper" video where one exists. Plus 1–2 cut-downs per long-form. Do not assume every Short is a cut-down.
  2. **Cadence: start at 3–4 Shorts/week for 8 weeks** (Option B), then use our data to decide whether daily adds value. Changing DEC-002 needs your approval. Option A keeps daily.
  3. **Narration:** one recognisable voice. Your own voice (recorded) or a clone of your voice **with the YouTube AI disclosure**. Generic TTS is the weakest option for trust (HYPOTHESIS).
  4. Use Shorts as cheap **topic tests**: a Short that over-performs becomes a long-form candidate.

## 7. Titles, thumbnails, packaging (REC)
Details: `strategy/seo-packaging.md`.
- **Titles:** lead with the tool/topic. Use expertise-compression ("Learn 80% of…", "…Clearly Explained"), a concrete outcome ("Build your first agent in 20 minutes") and honest experiment framing ("I let AI…"). The promise must be delivered in the video. No "$1000 this weekend", no "AGI".
- **Thumbnails:** your face + one tool logo/object + ≤3 words on the brand ink background with a mint accent (in ~18/24 top thumbnails a face was present, and ≤4 words in ~17/24). Use YouTube Test & Compare from the first long-form video.
- **Opening 5–15 s:** state the outcome, show the end result first, then say who it's for. This is a HYPOTHESIS: competitor hooks were not observable (no transcripts).
- **Hypotheses logged:** H-SEO-5/6, H-VIS-2, H-SHORT-1 in `experiments/register.md`.

## 8. Brand communication: banner and About (REC → DEC-005, DEC-006)
- **Banner v2 (proposal):** `brand/assets/proposals/banner-v2.png`. "ShippedWithAI" + "AI for everyone, explained by an engineer who ships." + Discover / Build / Automate / Ship + "New video every Tuesday". The logo stays.
- **About description (draft):**
  > **Discover. Build. Automate. Ship.**
  > ShippedWithAI helps you actually use AI, whether you're a student, a professional, a founder or a developer.
  > I'm a software engineer who builds real things with AI. Every week I show you how to choose the right AI tools, build apps and agents (often without writing code), automate real work, and what actually holds up when you ship it: the wins, the limits and the mistakes.
  > No hype. No fake demos. Just AI you can use.
  > 🎬 New video every Tuesday.
- **Channel keywords (draft):** AI tools, how to use AI, AI agents, AI automation, build with AI, no code AI, Claude, ChatGPT, Gemini, vibe coding, AI for business, AI productivity, learn AI, ShippedWithAI.

## 9. Monetization: revised 3-month strategy (REC → DEC-015)
Full proposal: `strategy/proposals/2026-11-21-monetization-v2.md`. Summary:
- **FACT:** YPP needs 1,000 subs + 4,000 h (reported 8,000 h from Feb 2027). This is not realistic within 90 days for a new channel (HYPOTHESIS).
- **REC:** Month 1: offer AI build/automation services and a free resource with email capture, and use affiliates only for tools used on camera. Month 2–3: the first paid kit or template from the most-requested build. Later: sponsorships (with a media kit), memberships, courses, YPP.
- Revenue numbers are hypotheses. Only actual revenue is ever recorded as fact.

## 10. Missing tools / integrations
| Missing | Impact | Minimum fix |
|---|---|---|
| YouTube Data API key | No comments, likes or date history for competitors | Free key as an environment secret (DEC-014) |
| Transcripts | Hooks and structure can't be studied | No clean fix (blocked). Watch manually or accept title-level analysis |
| Google Trends / Reddit / HN | No search-trend or community evidence | Allow the 3 hosts (DEC-014) |
| Impressions/CTR, returning viewers | Packaging can't be judged | Weekly Studio CSV export (DEC-014) |
| TTS / voice clone | AI Shorts narration blocked | DEC-013 then DEC-008 |
| Upload | — | Manual by the creator |

## 11. Decisions requiring your approval
| ID | Decision | Recommendation |
|---|---|---|
| DEC-010 | Content pillars | Approve the 4 pillars with the §5 definitions and weights |
| DEC-011 | Segment priority | Primary PRO/BEG/BIZ, secondary DEV/SWE/FRE/ADV |
| DEC-016 | Launch formats | Approve the §5/§7 formats. No daily news. |
| DEC-012 | Shorts cadence | Option B: 3–4/week for 8 weeks, then review (or keep daily) |
| DEC-013 | Shorts voice | Your voice, or a clone of your voice with disclosure |
| DEC-008 | TTS provider | After DEC-013 |
| DEC-005 | Banner v2 | Approve v2 (logo unchanged) |
| DEC-006 | About + keywords | Approve the §8 draft (edit freely) |
| DEC-015 | Monetization v2 | Approve the direction. Pricing and services decided separately. |
| DEC-014 | Research access | API key + 3 hosts + weekly export |
| DEC-009 | Weekly research/analytics session | Start when publishing starts |

**Next step after approval:** launch calendar + first scripts (SWAI-L001, first Shorts), following `content/workflows/`.
