# Handoff prompt: everything done so far (as of 2026-11-21, after Phase 1)

Paste the block below into a new session to give it full context. Source of truth is still the repo; this is a summary.

```text
You are continuing work on ShippedWithAI, a YouTube channel. The GitHub repo iayushpathak-dev/youtube is the permanent memory and source of truth. Working branch: claude/adoring-pasteur-aywagg. The repo default branch is claude/gifted-gates-6r6omc (no main). PR #1 (initialization) was merged. Phase 1 research is on the working branch. FIRST: read CLAUDE.md, INDEX.md, status/STATUS.md and status/decisions.md, run git status / git log, then continue from the documented state. The creator often writes in Hinglish. Reply in their language, and write repo docs in English.

== CHANNEL ==
- Name: ShippedWithAI · Handle: @shippedwithaihq · Channel ID: UCa2_ah_ehFCOyIn_QUt8t-w · Creator based in India.
- State on 2026-11-21 (Windsor.ai, FACT): 0 subscribers, 0 videos, 0 views, About description empty.
- The creator is a senior frontend developer but wants a broad AI audience.

== APPROVED DECISIONS ==
- DEC-001 Positioning "Discover. Build. Automate. Ship." Vision: a global YouTube brand helping everyone understand, explore, use and build with AI. Audience: students, beginners, developers, software engineers, content creators, entrepreneurs, business owners, working professionals, freelancers, AI enthusiasts, advanced AI users. AI is always the central theme. (This replaced the original developer-only positioning "Real apps, built with AI, shipped to production".)
- DEC-002 Cadence (initial assumption): 1 Short every day (45–60 s) and 1 long-form every Tuesday 7:30 pm IST. Daily Shorts time not set.
- DEC-003 Narration: Shorts AI-assisted, long-form in the creator's own voice.
- DEC-004 The repo knowledge architecture (below) is implemented.

== PROPOSED, AWAITING THE CREATOR'S APPROVAL ==
- DEC-005 Visual identity v1: logo (keep) = ">_" terminal prompt in mint→teal gradient + white up-right "ship" arrow on #0A0E14. Banner 2560x1440 currently says "ShippedWithAI · Real apps, built with AI, shipped to production" with chips Claude Code / Cursor / Next.js / React. Developer-only, conflicts with DEC-001, recommend revising to "Discover. Build. Automate. Ship." + "AI for everyone, from first prompt to shipped product" + "New video every Tuesday · Shorts daily". Not confirmed uploaded to the channel.
- DEC-006 Rewrite the About description + channel keywords for the new positioning (after pillars are set).
- DEC-007 3-month revenue plan (strategy/proposals/): YouTube as the funnel. Digital products (app source code + prompt packs, ₹499–999), freelance MVP builds, affiliate links, sponsors at ~2–5K subs. Needs revision for the broad audience.
- DEC-008 Choose a TTS provider for Shorts narration (ElevenLabs / OpenAI TTS / Google TTS). Needs a host allowed + API key secret.
- DEC-009 Weekly recurring research/analytics session (start once publishing begins).
- DEC-010 Content pillars. Phase 1 recommends Build 35% / Automate 30% / Discover 25% (explainers + decision guides, NOT daily news) / Ship 10%.
- DEC-011 Segment priority: primary PRO + BEG + BIZ/STARTUP, secondary DEV/SWE/FRE/ADV, tertiary STU/CRE, avoid the ENT daily-news race.
- DEC-012 Shorts cadence: Option B (recommended) 3–4/week for 8 weeks, then decide from data. Option A keeps daily. Shorts mostly standalone one-idea tips linked to long-form.
- DEC-013 Shorts voice: the creator's own voice or a clone of it WITH YouTube AI disclosure (generic TTS weakest).
- DEC-014 Research access: YouTube Data API key + allow trends.google.com, www.reddit.com, hn.algolia.com + weekly Studio CSV export.
- DEC-015 Monetization v2 (strategy/proposals/2026-11-21-monetization-v2.md): services first, a free lead magnet + email, first paid kit month 2–3, affiliates only for tools used, sponsors/memberships/YPP later. Supersedes DEC-007 if approved.
- DEC-016 Launch formats: "Learn 80% of X" masterclass for non-devs, "Clearly Explained + build one", honest experiments, monthly full course. No daily news, no hype money promises.
- DEC-005 now has banner v2: brand/assets/proposals/banner-v2.png ("AI for everyone, explained by an engineer who ships." + Discover/Build/Automate/Ship). DEC-006 About draft is in the Phase 1 report §8.

== REPO STRUCTURE (one home per information type; see INDEX.md) ==
CLAUDE.md (rules + session protocol) · INDEX.md · README.md
status/: STATUS.md, decisions.md (DEC register), integrations.md, handoff-prompt.md
brand/: identity.md, visual-guidelines.md, channel-profile.md, assets/ (logo.png 800x800, banner.png, src/*.html)
research/: market/ai-landscape.md, market/sources.md, competitors/README.md (method), competitors/channels.md (registry), competitors/snapshots/, audience/segments.md, audience/insights-log.md, opportunities.md (OPP-001..005)
strategy/: content-strategy.md, calendar.md, seo-packaging.md, proposals/
content/: README.md (schema), templates/short.md + long.md, workflows/shorts.md + long-form.md, shorts/, long/, registry.md (generated)
analytics/: README.md (metric availability), channel-log.md (baseline row), snapshots/
experiments/register.md · learning/lessons.md (LES-001..003) · reports/weekly, reports/monthly
tools/: content_index.py (validates content items + regenerates registry), render-branding.js (HTML → PNG via Playwright)

Content IDs: SWAI-S001… (Shorts), SWAI-L001… (long-form). Never reuse an ID. One Markdown file per item with YAML front matter (id, format, topic, segments, pillar, objective, hypothesis, title, hook, production_status IDEA→RESEARCHED→SCRIPTED→VOICED→EDITED→PACKAGED→PUBLISHED/KILLED, approval_status DRAFT→PROPOSED→APPROVED/REJECTED, publish_date, video_url, experiments, created, updated). Per-video performance lives only in the item's file. No content items exist yet.

== RULES ==
- Label findings FACT (dated, sourced) or HYPOTHESIS. Never invent metrics. Update files in place, keep history.
- The creator's approval is needed for: positioning/brand changes, strategy/pillars, schedule, new major direction, significant experiments, publishing/scheduling or editing live videos, new paid services/credentials. Research, drafts, docs and commits need no approval.
- Never commit secrets, never force-push, verify pushes. After work: update docs + STATUS, run tools/content_index.py if content changed, commit, push.
- Do not claim background learning. Learning = real research written into the repo.

== TOOLS / ACCESS (verified 2026-11-21) ==
Works: GitHub push to the working branch. WebSearch. yt-dlp flat listings (channel videos/shorts tabs, ytsearchN:, -J channel metadata incl. subscriber count). YouTube RSS feed (feeds/videos.xml?channel_id=…) for exact dates + views of the latest 15 uploads. ffmpeg, Playwright/Chromium. Fonts Inter, Inter Display, JetBrains Mono. Windsor.ai YouTube connector (views, watch time, retention, subs gained/lost, traffic sources + search terms, geography, demographics, comments, Shorts vs long split. Write actions: update_video_details, comment reply/moderate/delete, playlists).
Blocked/missing: per-video YouTube pages (bot check → no transcripts, comments, likes via yt-dlp; recommend a YouTube Data API key). Google Trends, Reddit, Hacker News blocked by the network policy. The connector has no impressions/CTR/returning viewers (needs a weekly YouTube Studio CSV export) and its trial covers only the last 30 days. No TTS. No upload/scheduling (the creator uploads manually in YouTube Studio). Remotion/HyperFrames declared in package.json but not npm-installed.

== RESEARCH SO FAR ==
Phase 1 report: reports/research/2026-11-21-phase-1-research-report.md (read it first). Key FACTS (2026-11-21):
- 34-channel deep dive (research/competitors/channels.md, raw snapshot in research/competitors/snapshots/2026-11-21-phase1-channel-scan.md). The biggest AI videos are "use AI better" / "build with AI, no code" for non-developers (Jeff Su "AI Agents, Clearly Explained" 5.79M; "Use Claude better than 99%" 2.6M; "Build your first AI agent (no coding)" 877K).
- Expertise-compression titles ("Learn 80% of X", "Better than 99%", "Clearly Explained") win across ≥6 channels. Experiment titles ("I told Claude… 100 times" 870K) also do well.
- AI news is a frequency race (~10 uploads/week, medians 110–157K). Top education channels post ~0.6–1.3/week with high medians (Jeff Su ~268K).
- Shorts: across 25 channels with ≥5 Shorts, the median Short gets 11% (range 3–72%) of median long-form views. The best AI Shorts are single concrete tips.
- Top thumbnails: a face in ~18/24, ≤4 words in ~17/24, a tool logo as hero in ~8/24.
- Market: GPT-6 Astra (2026-09-03), Gemini 4 family (Argon 09-30 … Neon 11-18), Claude Opus 5.5 (09-22), Anthropic Nasdaq IPO (11-19). Claude Code 39% dev workplace use (JetBrains). ~50% of US workers use AI but only ~30% weekly (Gallup). Agents 71–88% piloted (vendor surveys), only 5% of orgs ready (Deloitte). Students 95% UK / 57% US weekly. Sora discontinued (mixed sources).
- Platform: "inauthentic content" policy (Jul 2026) demonetizes mass-produced AI content. A cloned own voice needs an AI disclosure. Views count from the first frame since 2026-08-24. YPP reported to rise to 8,000 h / 20M Shorts views from Feb 2027 (verify in Studio → Earn).
- Unverified (seen only in creator titles): Fable 5.2, GPT-6.2 Astra, Meta Muse, Seedance 2.5, Jev, Grok Bot.
- Limits: no comments/transcripts/likes (bot check), so hooks were not analysed.

== NEXT PHASE ==
Waiting for the creator's decisions on DEC-005, 006, 008–016. Only after DEC-010/011/012/013/016 are approved: Phase 2 = launch calendar (strategy/calendar.md) + first content items (SWAI-L001, first SWAI-S###) via content/workflows/. Do NOT create the calendar or scripts before approval.
```
