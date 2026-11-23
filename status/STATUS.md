# Project status

**Channel:** AI Made Usable (@aimadeusable), renamed from ShippedWithAI on 2026-11-21 (DEC-017).

**Last updated:** 2026-11-21 · **Phase:** 2, **Launch week production**: The AI Showdown (DEC-019). Long-form SWAI-L001 (~8–9 min, game show, jokes) on Tue 2026-11-24 19:30 IST + 7 Shorts cut from it (S001 Sun 11-22 → S010 Sat 11-28). Scripted, awaiting the creator's review + recording (test **Sunday**).

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

### 2026-11-23 (late)
- **SWAI-L001 fully scored:** ChatGPT 40 · Claude 41 · **Gemini 44** (Round 5: 10/10/10).
- **DEC-023 APPROVED:** long-form moves to **Saturday**. L001 → Sat 28 Nov, L002 → Sat 5 Dec. CLAUDE.md, identity, calendar updated.
- S001 + S002 re-voiced with "Saturday" and re-rendered. **S006 (Round 2) rendered** (46 s). All three sent to the creator in chat. Drive upload is not possible from Claude (4.2 MB per-call limit), so the creator moves them to Drive `Shorts`.
- S008 (Round 4) and S009 (Round 5) rendered and sent the same evening: **5 Shorts ready** (S001, S002, S006, S008, S009).
- **Sound sync fix (2026-11-23):** `render_short.py` now cuts each scene where its own line ends: every scene carries its narration (`say`), and the cut snaps to the real pause in the voice (ffmpeg silencedetect). All 5 Shorts re-rendered (S001 is already uploaded; its old render stays on YouTube).
- **DEC-024:** Shorts start today (Mon 23: S001), S009 moves to Fri 27, S010 to Sun 29.
- **Next (when the creator says "bachi hui video bana"):** Day 1 L001 long video → Day 2 S003 → Day 3 S010. Then L002 (needs DEC-022). DEC-022 (L002 topic) needs approval this week.

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
| T8 | **Sunday 11-22:** record the AI Showdown test (protocol in SWAI-L001) + voice for S001 (clone or phone) | Creator | T7 |
| T9 | Edit L001 + Shorts, graphics, captions, thumbnail B (with the creator's photo) | Claude | T8 (recordings), T4 |
| T10 | Upload + schedule each video in Studio | Creator | T9 |
| T2 | In YouTube Studio: change the display name to **AI Made Usable** (handle @aimadeusable ✅ done), upload logo/banner/watermark, paste About + keywords (`brand/channel-profile.md`) | Creator | — (approved 2026-11-21) |
| T3 | Voice clone: ElevenLabs connector ✅ connected (Starter). The creator creates the **Instant Voice Clone** once on elevenlabs.io from the 2-min sample (`brand/voice-clone.md`). Claude then generates the Shorts voiceovers via the connector | Creator → Claude | creator's clone |
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
