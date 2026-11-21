# Handoff prompt: everything done so far (as of 2026-11-21)

Paste the block below into a new session to give it full context. Source of truth is still the repo; this is a summary.

```text
You are continuing work on ShippedWithAI, a YouTube channel. The GitHub repo iayushpathak-dev/youtube is the permanent memory and source of truth. Working branch: claude/adoring-pasteur-aywagg (latest commit 9bd00ad, "Initialize ShippedWithAI project knowledge system"; not merged to main). FIRST: read CLAUDE.md, INDEX.md, status/STATUS.md and status/decisions.md, run git status / git log, then continue from the documented state. The creator often writes in Hinglish. Reply in their language, and write repo docs in English.

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
- DEC-010 Draft content pillars: Discover (AI news/tools explained), Build (making real things with AI, no-code to code), Automate (workflows/agents for work & business), Ship (launching, earning, real results).

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
- 2026-11-21 search scan (AI-coding queries only): top performers are Claude Code / Cursor tutorials and courses, e.g. Tech With Tim "Claude Code - Full Tutorial for Beginners" 2.04M views, Productive Dude full course 1.24M, Fireship "Cursor 2.0…" 1.07M, Mosh 521K, Jason Lee "$400K/mo App with Claude Code" 423K. Framework-first titles from small channels flopped ("Cursor AI + Next.js" 277 views). Hypotheses: lead titles with the tool, promise an outcome, full courses do best, a senior-dev "what AI got wrong" review angle is under-served. Coverage is skewed to developers; other segments not yet researched.
- YouTube monetization (FACT 2026-11-21): YPP ads = 1,000 subs + 3 uploads in 90 days + 4,000 public watch hours/12 months or 10M Shorts views/90 days. The lower tier is 500 subs + 3,000 h or 3M Shorts views. Several outlets report that from 2027-02-01 new applicants need 8,000 h or 20M Shorts views (one source disagrees; verify in Studio → Earn).

== NEXT PHASE (not started; needs the creator's go-ahead) ==
Phase 1 research report: (1) competitors across ALL audience segments, latest 6 months (positioning, frequency, top Shorts/long-form, titles, thumbnails, formats); (2) AI market landscape per area; (3) validate audience segments; (4) recommendations for pillars (DEC-010), segment priority, Shorts↔long-form relationship, packaging rules, revised banner/About (DEC-005/006), revenue plan (DEC-007). Only after approval: the launch calendar and first scripts. Do NOT generate the calendar or scripts before that.
```
