# Decision register

Statuses: **PROPOSED** (awaiting the creator) → **APPROVED** / **REJECTED** → **IMPLEMENTED**.
A recommendation is never an approval. An approval is recorded with its date and the creator's words or a reference to them.
Never delete entries. Mark superseded ones with `SUPERSEDED by DEC-###`.

---

### DEC-001: Brand positioning and audience
- **Date:** 2026-11-21
- **Description:** Positioning "Discover. Build. Automate. Ship." Vision: a global YouTube brand that helps everyone understand, explore, use and build with AI. The audience is broad (students → advanced AI users), not developers only. AI stays the central theme.
- **Evidence:** Creator's project initialization brief (2026-11-21).
- **Recommendation:** n/a (creator-directed).
- **Status:** APPROVED → IMPLEMENTED in `brand/identity.md`, `CLAUDE.md`.
- **Approval record:** The creator set this in the initialization brief, 2026-11-21.
- **Note:** This supersedes the developer-only positioning in the original About text (`brand/channel-profile.md`). See DEC-006.

### DEC-002: Initial publishing cadence
- **Date:** 2026-11-21
- **Description:** One Short every day (45–60 s) and one long-form video every Tuesday. The Tuesday 7:30 pm IST slot is carried over from `brand/channel-profile.md`. The daily Shorts time is not yet set.
- **Evidence:** Creator's brief, which calls these "initial operating assumptions, not permanent rules".
- **Status:** APPROVED (as an initial assumption).
- **Approval record:** Initialization brief, 2026-11-21.
- **Note:** This supersedes the "3 Shorts per week" cadence in `strategy/proposals/2026-11-21-3-month-revenue-plan.md`, which was never approved.

### DEC-003: Narration (SUPERSEDED by DEC-020 for long-form)
- **Date:** 2026-11-21
- **Description:** Shorts use AI-assisted narration. Long-form uses the creator's own voice.
- **Status:** APPROVED. Implementation is blocked: no text-to-speech service is available (see DEC-008).
- **Approval record:** Initialization brief, 2026-11-21.

### DEC-004: The repository is the permanent knowledge system
- **Date:** 2026-11-21
- **Description:** Use the knowledge architecture in `INDEX.md` and the operating rules in `CLAUDE.md`. Existing files were moved (with git history kept):
  `channel/profile.md` → `brand/channel-profile.md`, `channel/branding/` → `brand/assets/`,
  `channel/research/competitors-2026-11.md` → `research/competitors/snapshots/2026-11-21-search-scan.md`,
  `channel/plan-3-months.md` → `strategy/proposals/2026-11-21-3-month-revenue-plan.md`.
- **Status:** APPROVED → IMPLEMENTED.
- **Approval record:** Initialization brief, 2026-11-21 ("choose a clean, logical directory structure").

### DEC-005: Visual identity v1 (logo and banner)
- **Date:** 2026-11-21
- **Description:** A dark terminal-style mark (`>_` prompt plus a "ship" arrow) on #0A0E14 with a mint/teal gradient. The banner reads "ShippedWithAI · Real apps, built with AI, shipped to production" with the chips Claude Code / Cursor / Next.js / React.
- **Evidence:** Created 2026-11-21 (`brand/assets/`). It has not been confirmed whether it was uploaded to the channel.
- **Recommendation:** Keep the logo. **Revise the banner before upload**: its tagline and chips are developer-only, which conflicts with DEC-001. Proposed banner text: "Discover. Build. Automate. Ship." plus "AI for everyone, from first prompt to shipped product" and "New video every Tuesday · Shorts daily".
- **Status:** PROPOSED.
- **Approval record:** none.
- **Update 2026-11-21 (Phase 1):** Banner v2 rendered as a proposal: `brand/assets/proposals/banner-v2.png` ("AI for everyone, explained by an engineer who ships." + chips Discover / Build / Automate / Ship + "New video every Tuesday"). It leaves out "Shorts daily" until DEC-012 is decided. Logo unchanged. Evidence for the "engineer" framing: AUD-002. Still PROPOSED. Report §8.

### DEC-006: Channel About description rewrite
- **Date:** 2026-11-21
- **Description:** The current draft About text (in `brand/channel-profile.md`) speaks only to developers ("I'm a senior frontend developer… React and Next.js"). It needs rewriting for the DEC-001 positioning. The channel's About is currently empty (FACT, Windsor.ai, 2026-11-21).
- **Recommendation:** Claude drafts a new About text and keywords once the research phase defines the content pillars, and the creator approves before it goes live.
- **Status:** PROPOSED.
- **Update 2026-11-21 (Phase 1):** Draft About text + keywords in the Phase 1 report §8. Still PROPOSED.

### DEC-007: 3-month revenue plan
- **Date:** 2026-11-21
- **Description:** Earlier proposal (`strategy/proposals/2026-11-21-3-month-revenue-plan.md`): use YouTube as the funnel, with digital products, freelance builds, affiliates and later sponsors.
- **Evidence:** Web search 2026-11-21. YPP ad revenue needs 1,000 subs + 4,000 watch hours (12 mo) or 10M Shorts views (90 d). Multiple outlets report that from **2027-02-01** new applicants need 8,000 watch hours or 20M Shorts views. Sources: [YouTube Help](https://support.google.com/youtube/answer/72851), [Tubefilter 2026-08-10](https://www.tubefilter.com/2026/08/10/youtube-partner-program-ad-eligibility-requirements-shorts/amp/), [vidIQ](https://vidiq.com/blog/post/monetize-youtube-guide/). One source disagrees ([Analytics Insight](https://www.analyticsinsight.net/apps/youtube-partner-program-eligibility-requirements)), so verify in Studio → Earn.
- **Recommendation:** Re-evaluate after the research phase. The plan was written for a developer-only audience.
- **Status:** PROPOSED (needs revision).
- **Update 2026-11-21 (Phase 1):** Revised as DEC-015 (`strategy/proposals/2026-11-21-monetization-v2.md`). Recommend marking DEC-007 SUPERSEDED by DEC-015 if DEC-015 is approved.

### DEC-008: Text-to-speech service for Shorts narration
- **Date:** 2026-11-21
- **Description:** DEC-003 requires AI narration, and no TTS is available in the environment. `api.elevenlabs.io` is blocked by the network policy (2026-11-21).
- **Recommendation:** Pick one TTS provider after a voice test (candidates: ElevenLabs, OpenAI TTS, Google Cloud TTS). Then allow that single host and add its API key as an environment secret.
- **Status:** PROPOSED. Needs the creator's choice of provider, an account and a key.
- **Update 2026-11-21 (Phase 1):** See DEC-013. Policy research shows that a cloned **own** voice requires an AI disclosure, generic TTS does not inherently require one, and mass-produced repetitive AI content is not monetizable (Jul 2026 "inauthentic content" update). The provider choice depends on DEC-013.

### DEC-009: Recurring weekly research and analytics session
- **Date:** 2026-11-21
- **Description:** A scheduled weekly session (suggested: Wednesday) that pulls channel analytics, scans competitors, writes `reports/weekly/YYYY-Www.md` and updates the knowledge files.
- **Recommendation:** Start it once publishing begins, so there is data to analyse.
- **Status:** PROPOSED.

### DEC-010: Draft content pillars
- **Date:** 2026-11-21
- **Description:** Four pillars mapped to the positioning. **Discover** (AI news, tools and models explained), **Build** (making real things with AI, from no-code to code), **Automate** (AI workflows and agents for work and business), **Ship** (taking it live: launching, earning, real results).
- **Evidence:** Derived from DEC-001 only. Not yet backed by research.
- **Recommendation:** Validate or revise in the research phase before approval.
- **Status:** PROPOSED.
- **Update 2026-11-21 (Phase 1):** Research supports the four pillars with re-scoped definitions and weights: **Build 35%, Automate 30%, Discover 25% (explainers and decision guides, not a daily news race), Ship 10%**. Evidence and definitions: Phase 1 report §5. Still PROPOSED.

### DEC-011: Segment priority
- **Date:** 2026-11-21
- **Description:** Primary: working professionals (PRO), beginners (BEG) and entrepreneurs/business owners (BIZ/STARTUP), served with "build and automate with AI, explained by an engineer". Secondary: developers/engineers (DEV/SWE, credibility anchor), freelancers (FRE, anti-hype), advanced users (ADV, deep long-form). Tertiary: students (STU), creators (CRE). Avoid: the daily AI-news race (ENT).
- **Evidence:** `research/audience/segments.md`, AUD-001..003, `research/competitors/channels.md`. Phase 1 report §4.
- **Status:** PROPOSED.

### DEC-012: Shorts cadence and Shorts ↔ long-form relationship (proposes changing DEC-002)
- **Date:** 2026-11-21
- **Description:** Option A (keep DEC-002): 7 Shorts/week. **Option B (recommended):** 3–4 Shorts/week for the first 8 weeks, then decide from our own data (H-SHORT-1). In both options Shorts are mostly **standalone one-idea tips/demos** that point to a related long-form, plus 1–2 cut-downs per long-form.
- **Evidence:** In 25 competitor channels with ≥5 recent Shorts, the median Short gets 11% (range 3–72%) of the median long-form views. 23 of 25 are below 34%. AIR (18K channels) suggests Shorts at 25–40% of uploads in education/business niches. Metricool links ~5 Shorts/month with +46% views. Neither study is peer-reviewed. The inauthentic-content policy penalises repetitive mass production. Phase 1 report §6.
- **Status:** PROPOSED. Changing the schedule requires the creator's approval.

### DEC-013: Shorts narration approach
- **Date:** 2026-11-21
- **Description:** Options: (a) generic AI TTS voice, (b) a clone of the creator's own voice (consistent brand voice; requires the YouTube AI disclosure per policy), (c) the creator records Shorts too (~2 min/Short). **Recommendation: (b) with disclosure, or (c)**, because one recognisable voice across formats builds trust. Every Short must carry original insight or a real demo, never templated mass output.
- **Evidence:** `research/market/ai-landscape.md` → Platform & monetization (disclosure, inauthentic content). India industry comment on faceless AI voice-over content (opinion). Phase 1 report §6.
- **Status:** PROPOSED. Changes how DEC-003 is implemented, not the decision itself.

### DEC-014: Research access: YouTube Data API key + network hosts
- **Date:** 2026-11-21
- **Description:** (1) A free YouTube Data API v3 key as an environment secret (comments, exact stats, date history). (2) Allow `trends.google.com`, `www.reddit.com`, `hn.algolia.com`. (3) A weekly YouTube Studio CSV export by the creator once publishing starts (impressions/CTR/returning viewers).
- **Evidence:** Phase 1 couldn't read any comments or transcripts (bot check), and 49 of 600 search results lacked metadata. `status/integrations.md`.
- **Status:** PROPOSED.

### DEC-015: Monetization strategy v2
- **Date:** 2026-11-21
- **Description:** Services first (AI builds/automation for founders and small businesses), a free lead magnet + email list in month 1, the first paid kit in month 2–3, affiliates only for tools used on camera, sponsorships and memberships later, and no optimisation for YPP in the first 90 days. `strategy/proposals/2026-11-21-monetization-v2.md`.
- **Evidence:** YPP thresholds and reported Feb-2027 increase. Audience needs (AUD-002/003). Phase 1 report §9.
- **Status:** PROPOSED. Supersedes DEC-007 if approved.

### DEC-016: Content formats for launch
- **Date:** 2026-11-21
- **Description:** Long-form formats: (1) "Learn 80% of X" tool masterclass for non-developers, (2) "Clearly Explained + build one" (concept + a working example), (3) honest experiment/test ("I let AI do X — an engineer's verdict"), (4) a monthly full course. Shorts: one-tip demos, "which AI for which job", myth-vs-reality. **Not:** daily news reaction, hype money promises.
- **Evidence:** Phase 1 report §5–7, `strategy/seo-packaging.md`.
- **Status:** PROPOSED.

### DEC-005 / DEC-006 resolution: brand identity v2 + About text
- **Date:** 2026-11-21
- **Description:** New logo (ship arrow + AI sparks), banner v3 ("AI for everyone, explained by an engineer who ships." · Discover/Build/Automate/Ship · New video every Tuesday), watermark, final About description (596 chars) + keywords. v1 archived in `brand/assets/archive/v1/`. `brand/assets/proposals/banner-v2.png` is kept as the intermediate proposal.
- **Approval record:** The creator, 2026-11-21: "so now you need to write description and create logo and banner for this" (following the Phase 1 report).
- **Status:** DEC-005 and DEC-006 → **APPROVED → IMPLEMENTED** in the repo (`brand/channel-profile.md`, `brand/assets/`). **Going live is pending the creator's upload in YouTube Studio.** Claude verifies the About via Windsor.ai after the upload.
- **Update 2026-11-21:** The creator supplied their own About text ("finalize this …"). Claude made light edits only: removed Markdown `**` (YouTube doesn't render it), reduced the repeated "explore", and changed "honest experiences" to "honest takes". Final text in `brand/channel-profile.md`. Note: "Shorts daily" matches DEC-002. If DEC-012 Option B is approved, update this line.

### DEC-017: Channel name change
- **Date:** 2026-11-21
- **Description:** The creator wants to rename because "ShippedWithAI" is crowded. Evidence: `research/competitors/snapshots/2026-11-21-channel-name-check.md`. No exact-name channel was found, but @shippedwithai is taken, two near-identical small channels exist, and "shipped with AI" search overlaps with AI dropshipping.
- **Options (handle free as of 2026-11-21, no similar channel names found):** "AI Made Usable" (@aimadeusable) · "Real AI Work" (@realaiwork) · "AI First Lab" (@aifirstlab) · "Ship This AI" (@shipthisai) · or keep ShippedWithAI.
- **Recommendation:** **AI Made Usable**. It states the promise ("Just useful AI") for every segment, is distinct in search, and doesn't overlap with dropshipping. The tagline "Discover. Build. Automate. Ship." and the logo mark still fit.
- **Impact if changed:** banner text, About first lines, repo docs, CLAUDE.md identity, handle. The logo mark and watermark are unaffected. Renaming is cheapest now (0 videos).
- **Status:** PROPOSED. A major brand change needs the creator's explicit choice.
- **Approval record:** The creator, 2026-11-21: "aimadeusable and AI Made Usable". → **APPROVED → IMPLEMENTED** in the repo (banner re-rendered, About, keywords, CLAUDE.md, identity, profile, handoff). The positioning/tagline, logo and watermark are unchanged. **Pending:** the creator changes the name + handle in YouTube Studio. Handle verified claimed 2026-11-21 (youtube.com/@aimadeusable → our channel ID). The public display name still showed "ShippedWithAI" at that check.

### DEC-018: Start production of week 1 (launch)
- **Date:** 2026-11-21
- **Description:** The creator asked to start: a long-form for Tuesday 2026-11-24 plus multiple Shorts. Claude created SWAI-L001 (ChatGPT vs Claude vs Gemini, 5 verifiable tasks) and SWAI-S001..S007 (daily per DEC-002) using its recommended defaults for the still-PROPOSED DEC-010/011/016. The Shorts voice for week 1 is the creator's own recording (DEC-013 option c) because no TTS exists.
- **Approval record:** The creator, 2026-11-21: "so lets create a video that we published on tuesday but we create shorts multiple so that we start". This approves **starting production**. It does not approve the individual scripts (each item is approval_status PROPOSED) or DEC-010/011/012/013/016 as permanent strategy.
- **Status:** APPROVED → IN PROGRESS.

### DEC-008 / DEC-013 resolution: creator voice clone via ElevenLabs
- **Date:** 2026-11-21
- **Description:** Shorts narration = an ElevenLabs Instant Voice Clone of the creator's own voice (DEC-013 option b), with the YouTube "altered content" disclosure on every clone-narrated Short. Long-form stays in the real voice. Details and rules: `brand/voice-clone.md`.
- **Evidence:** Starter ≈ $6/mo with cloning + commercial licence (third-party guides, Nov 2026. Verify on elevenlabs.io). Disclosure rule from YouTube Help (14328491). Alternatives considered: Murf AI (Indian-accent stock voices), Resemble, CAMB.AI.
- **Approval record:** The creator, 2026-11-21: "so lets set up a ai voice tool jo meri voice use krega". This approves the tool and the cloning of their own voice. **The paid plan is the creator's purchase.**
- **Status:** APPROVED → IN PROGRESS (waiting for the account, API key via secure form, and voice sample).

### DEC-019: First video format, length and tone
- **Date:** 2026-11-21
- **Description:** SWAI-L001 becomes **"The AI Showdown"**: a game-show format, ~8–9 min (not 15–25), casual tone with AI jokes, and the same verifiable test. All 7 launch-week Shorts are cut from it (S001 teaser, S002/S003/S006/S008/S009 one round each, S010 cheat sheet). The off-topic drafts S004/S005/S007 are KILLED (IDs retired, ideas kept as OPP-007/016/017).
- **Evidence:** `research/competitors/snapshots/2026-11-21-l001-format-research.md`. Humour-led "I tested AI" videos 5–10M. Successful direct comparisons 7–13 min (Parker Prompts 211K at 8:51).
- **Approval record:** The creator, 2026-11-21: "first video kya hogi uski research kr… us video ke 7 shorts bana dena or 1 long video jyada long nhi boring nhi hona chaheye interesting and Mazza aana chaheye… casual jokes… AI based jokes".
- **Status:** APPROVED (direction) → IMPLEMENTED in the scripts. The scripts themselves still await the creator's review (approval_status PROPOSED).
- **Humour rules (brand voice):** jokes target what happened on screen or our own struggles, never claims about companies or people. No fake fails. Keep the learning point in every round.

### DEC-020: Faceless channel, all narration in the creator's voice clone (changes DEC-003)
- **Date:** 2026-11-21
- **Description:** No face on camera in any video. **All narration, long-form included, uses the creator's ElevenLabs voice clone.** Claude produces every video (graphics, edit, captions, SFX, voice generation via the connector). The creator only (1) creates the voice clone once, (2) screen-records the AI apps for tests (no face, no mic), and (3) uploads in YouTube Studio.
- **Supersedes:** DEC-003 ("long-form in the creator's own voice") and the face-cam/REACT notes in SWAI-L001 v2.
- **Policy notes:** YouTube "altered content" disclosure = **Yes** on every clone-narrated video (own-voice clone). Inauthentic-content risk is mitigated by original tests, original scripts and real screen recordings. Never templated mass output.
- **Approval record:** The creator, 2026-11-21: "Video tu banayega na Kyu ki face wace wala kuch nhi hai bas voice aayegi Woh bhi ai tool meri voice mai krega".
- **Status:** APPROVED → IMPLEMENTING.

### DEC-021: Shorts-only launch week; first long-form moves to Tue 2026-12-01; keep a two-week buffer
- **Date:** 2026-11-23
- **Approval record:** The creator: "kalse shorts dalenge next tuesday we upload long video and next tuesday ke liye bhi content decide kr is week sirf shorts dalenge… after this tuesday we have next 2 tuesday content videos and shorts".
- **Status:** APPROVED → calendar updated (`strategy/calendar.md`).

### DEC-022: Topic for SWAI-L002 (Tue 2026-12-08)
- **Recommendation:** "Build your first useful AI agent, no code (an engineer's honest test)" (OPP-007). Evidence: Jeff Su "AI Agents, Clearly Explained" 5.79M, Metics "Build Your First AI Agent (No Coding)" 877K. It fits the Automate pillar and is the natural next step after the showdown. Alternative: OPP-008 "Learn 80% of Claude Code for non-developers".
- **Status:** PROPOSED.
