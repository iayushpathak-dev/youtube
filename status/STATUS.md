# Project status

**Channel:** AI Made Usable (@aimadeusable), renamed from ShippedWithAI on 2026-11-21 (DEC-017).

**Last updated:** 2026-11-21 · **Phase:** 2, **Launch week production** (DEC-018). Long-form SWAI-L001 on Tue 2026-11-24 19:30 IST + Shorts SWAI-S001..S007 (Sun 11-22 → Sat 11-28). All scripted, awaiting the creator's script approval + recordings.

## Channel state (FACT, Windsor.ai, 2026-11-21)
0 subscribers · 0 public videos · 0 views · About description empty. Brand v2 files ready in `brand/assets/` (v1 archived). Not yet uploaded.

## Done
- 2026-11-19 · Tooling declared (yt-dlp, Remotion, HyperFrames) and channel profile written.
- 2026-11-21 · Logo + banner v1 (DEC-005). Initial AI-coding search scan. Draft 3-month revenue plan (DEC-007).
- 2026-11-21 · Windsor.ai YouTube connector linked by the creator. Baseline analytics recorded.
- 2026-11-21 · Project knowledge system initialised (DEC-004). PR #1 merged into the default branch `claude/gifted-gates-6r6omc`.
- 2026-11-21 · **Phase 1 research completed:** `reports/research/2026-11-21-phase-1-research-report.md`.
  - 34-channel competitor deep dive + 24 segment searches (`research/competitors/`).
  - Market landscape across all areas with sources (`research/market/ai-landscape.md`).
  - Segments validated and prioritised (`research/audience/`).
  - Opportunities OPP-006..015 (`research/opportunities.md`).
  - Packaging patterns (`strategy/seo-packaging.md`).
  - Banner v2 proposal (`brand/assets/proposals/banner-v2.png`).
  - Monetization v2 proposal (`strategy/proposals/2026-11-21-monetization-v2.md`).
  - Decisions DEC-011..016 proposed. Lessons LES-004..006.
- 2026-11-21 · **Brand identity v2 final** (DEC-005/006 approved by the creator): new logo, banner, watermark, About text + keywords. Awaiting upload.

## Pending approvals (see `status/decisions.md`). Phase 2 is blocked on the first five.
| ID | Topic | Claude's recommendation |
|---|---|---|
| DEC-010 | Content pillars + weights | Build 35 / Automate 30 / Discover 25 / Ship 10 |
| DEC-011 | Segment priority | Primary PRO, BEG, BIZ |
| DEC-016 | Launch formats | Masterclass / Clearly Explained + build / honest experiment / monthly course. No daily news. |
| DEC-012 | Shorts cadence (would change DEC-002) | 3–4/week for 8 weeks, then review |
| DEC-015 | Monetization v2 (supersedes DEC-007) | Approve the direction |
| DEC-014 | Research access (API key, hosts, Studio export) | Approve |
| DEC-009 | Weekly research/analytics session | Start when publishing starts |

## Pending tasks
| # | Task | Owner | Blocked by |
|---|---|---|---|
| T1 | ✅ Week 1 calendar + scripts (L001, S001–S007) | Claude | done 2026-11-21 |
| T7 | Approve/edit the week-1 scripts | Creator | — |
| T8 | Record SWAI-L001 test (protocol in the item file) + voice for S001/S002 (needed first: Sun/Mon) | Creator | T7 |
| T9 | Edit L001 + Shorts, graphics, captions, thumbnail B (with the creator's photo) | Claude | T8 (recordings), T4 |
| T10 | Upload + schedule each video in Studio | Creator | T9 |
| T2 | In YouTube Studio: change the display name to **AI Made Usable** (handle @aimadeusable ✅ done), upload logo/banner/watermark, paste About + keywords (`brand/channel-profile.md`) | Creator | — (approved 2026-11-21) |
| T3 | Voice clone: creator makes an ElevenLabs account (Starter) + saves the API key in the secure form + records the 2-min sample (`brand/voice-clone.md`). Claude then creates the clone and test voiceovers | Creator → Claude | — (approved 2026-11-21) |
| T4 | `npm install` Remotion/HyperFrames when production starts | Claude | Phase 2 |
| T5 | Decide the daily/regular Shorts publish time | Creator | DEC-012 |
| T6 | Next competitor pass: comments/hooks, Hindi channels, thumbnails at scale | Claude | DEC-014 (API key) for comments |

## Blockers / missing access (detail: `status/integrations.md`)
- YouTube per-video data (comments, likes, transcripts) blocked by the bot check → DEC-014.
- Google Trends, Reddit and Hacker News blocked by the network policy → DEC-014.
- No impressions/CTR/returning viewers via the connector → weekly Studio export.
- No TTS/voice clone → DEC-013/008.
- Upload/scheduling is manual (the creator).

## Branch
The working branch is `claude/adoring-pasteur-aywagg`. The repo's default branch is `claude/gifted-gates-6r6omc` (no `main`). PR #1 merged. Phase 1 work is on the working branch. Merging needs a new PR when the creator asks.
