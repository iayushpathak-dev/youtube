# Project status

**Last updated:** 2026-11-21 · **Phase:** 0, Initialization ✅ complete → next: Phase 1, Research report (not started)

## Channel state (FACT, Windsor.ai, 2026-11-21)
0 subscribers · 0 public videos · 0 views · About description empty. Logo/banner v1 files exist (`brand/assets/`). Not confirmed uploaded.

## Done
- 2026-11-19 · Tooling declared (yt-dlp, Remotion, HyperFrames) and channel profile written.
- 2026-11-21 · Logo + banner v1 (DEC-005, PROPOSED). Initial AI-coding search scan. Draft 3-month revenue plan (DEC-007, PROPOSED).
- 2026-11-21 · Windsor.ai YouTube connector linked by the creator. Baseline analytics recorded.
- 2026-11-21 · Project knowledge system initialised (DEC-004): CLAUDE.md, INDEX.md, brand/research/strategy/content/analytics/experiments/learning/reports/status structure, decision register, content DB + validator.

## Next phase: research report (needs the creator's go-ahead to start; deliverable needs approval)
1. Competitor intelligence across all segments, latest 6 months (`research/competitors/`).
2. AI market landscape per area (`research/market/ai-landscape.md`).
3. Audience segment validation (`research/audience/`).
4. Recommendations: content pillars (DEC-010), segment priority, Shorts/long-form relationship, packaging rules, revised banner/About (DEC-005/006), revenue plan (DEC-007).
5. Only after approval: launch calendar + first scripts.

## Pending tasks
| # | Task | Owner | Blocked by |
|---|---|---|---|
| T1 | Run the Phase 1 research and write the report | Claude | Creator's go-ahead |
| T2 | Revise the banner to the new positioning | Claude | DEC-005 approval |
| T3 | Rewrite About text + channel keywords | Claude | DEC-006 / DEC-010 |
| T4 | Set up AI narration for Shorts | Claude | DEC-008 (provider + key + host allow) |
| T5 | `npm install` Remotion/HyperFrames when production starts | Claude | — |
| T6 | Decide the daily Shorts publish time | Creator | Research input |

## Pending approvals (see `status/decisions.md`)
DEC-005 visual identity v1 · DEC-006 About rewrite · DEC-007 revenue plan (needs revision) · DEC-008 TTS provider · DEC-009 weekly recurring session · DEC-010 content pillars

## Blockers / missing access (detail: `status/integrations.md`)
- YouTube per-video data (comments, likes, transcripts) blocked by the bot check → YouTube Data API key recommended.
- Google Trends, Reddit and Hacker News blocked by the network policy.
- No impressions/CTR/returning viewers via the connector → weekly Studio export.
- No TTS → DEC-008.
- Upload/scheduling is manual (the creator).

## Branch
Work is on `claude/adoring-pasteur-aywagg` (pushed). Merging to `main` needs a PR, which the creator has not yet requested.
