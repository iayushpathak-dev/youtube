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

### DEC-003: Narration
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

### DEC-006: Channel About description rewrite
- **Date:** 2026-11-21
- **Description:** The current draft About text (in `brand/channel-profile.md`) speaks only to developers ("I'm a senior frontend developer… React and Next.js"). It needs rewriting for the DEC-001 positioning. The channel's About is currently empty (FACT, Windsor.ai, 2026-11-21).
- **Recommendation:** Claude drafts a new About text and keywords once the research phase defines the content pillars, and the creator approves before it goes live.
- **Status:** PROPOSED.

### DEC-007: 3-month revenue plan
- **Date:** 2026-11-21
- **Description:** Earlier proposal (`strategy/proposals/2026-11-21-3-month-revenue-plan.md`): use YouTube as the funnel, with digital products, freelance builds, affiliates and later sponsors.
- **Evidence:** Web search 2026-11-21. YPP ad revenue needs 1,000 subs + 4,000 watch hours (12 mo) or 10M Shorts views (90 d). Multiple outlets report that from **2027-02-01** new applicants need 8,000 watch hours or 20M Shorts views. Sources: [YouTube Help](https://support.google.com/youtube/answer/72851), [Tubefilter 2026-08-10](https://www.tubefilter.com/2026/08/10/youtube-partner-program-ad-eligibility-requirements-shorts/amp/), [vidIQ](https://vidiq.com/blog/post/monetize-youtube-guide/). One source disagrees ([Analytics Insight](https://www.analyticsinsight.net/apps/youtube-partner-program-eligibility-requirements)), so verify in Studio → Earn.
- **Recommendation:** Re-evaluate after the research phase. The plan was written for a developer-only audience.
- **Status:** PROPOSED (needs revision).

### DEC-008: Text-to-speech service for Shorts narration
- **Date:** 2026-11-21
- **Description:** DEC-003 requires AI narration, and no TTS is available in the environment. `api.elevenlabs.io` is blocked by the network policy (2026-11-21).
- **Recommendation:** Pick one TTS provider after a voice test (candidates: ElevenLabs, OpenAI TTS, Google Cloud TTS). Then allow that single host and add its API key as an environment secret.
- **Status:** PROPOSED. Needs the creator's choice of provider, an account and a key.

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
