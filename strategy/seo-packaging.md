# YouTube SEO & packaging

Rules here are labelled FACT (platform limits, documented behaviour) or HYPOTHESIS (to validate via `experiments/`).

## Platform limits (FACT)
- Title: max 100 characters. Mobile shows roughly the first 40–50, so front-load the key words.
- Description: max 5,000 characters. The first ~2 lines show above the fold.
- Tags: max 500 characters total. Low ranking weight; mainly helps with misspellings.
- Hashtags: up to 3 shown above the title. Over 60 in a description and all are ignored.
- Shorts: vertical, up to 3 minutes (ours: 45–60 s by DEC-002).

## Title patterns (HYPOTHESIS, from the 2026-11-21 AI-coding search scan)
- H-SEO-1: Lead with the tool or topic people search ("Claude Code …"), not the framework.
- H-SEO-2: Promise a concrete outcome ("Build & Deploy", "Start to Finish", "in 10 Minutes").
- H-SEO-3: Money/result framing ("$X app", "$50K website") lifts clicks for BIZ/BEG audiences.
- H-SEO-4: Full-course / "learn X% in N minutes" formats over-perform for tutorials.
These came from developer queries only. The 2026-11-21 Phase 1 cross-segment scan (below) confirms 1, 2 and 4 beyond developers.

## Cross-segment patterns (Phase 1, 2026-11-21, 34 channels + 24 searches)
FACT observations (see `research/competitors/snapshots/2026-11-21-phase1-channel-scan.md`):
- **Expertise-compression titles** recur across ≥6 channels with 0.5–5.8M views: "Learn 80% of X in N Minutes", "Use X Better Than 99% of People", "X, Clearly Explained", "1000+ hours of … in 15 minutes".
- **Experiment titles** with a number: "I Told Claude to 'Make it better' 100 Times" (870K), "I Spent 100 Hours Using GPT-6 Astra" (766K), "I Tried 100+ GitHub Repos" (460K).
- **Reassurance/urgency titles**: "You're not behind (yet): …" (3.4–3.5M, two channels).
- **Full courses** (2–15 h) produce the largest single numbers (Satish Dhawale 5.8M, JS Mastery 1.4M, Nate Herk 2.06M).
- News channels publish ~10/week with medians of 110–157K, which is a frequency game.
- Thumbnails of the top 24 long-form videos (one per channel): a **face in ~18/24**, **≤4 words of text in ~17/24**, the **tool's logo as hero object in ~8/24** (Claude asterisk, OpenAI knot). Minimal text-only thumbnails work for strong brands (AI Explained "GPT-6", 859K).

Hypotheses to test on our channel (→ `experiments/register.md`):
- H-SEO-5: Expertise-compression titles outperform "tutorial" titles for BEG/PRO.
- H-SEO-6: "Senior engineer" framing lifts CTR for builder topics versus no framing.
- H-VIS-2: The creator's face + one tool logo + ≤3 words beats screenshots.
- Do not copy hype patterns that misrepresent ("$1000 this weekend", "AGI"). Brand rule: the promise must be delivered in the video.

## Packaging checklist (per item)
- [ ] Title ≤60 chars preferred, keyword in the first 40
- [ ] Thumbnail text ≤4 words, complements the title (`brand/visual-guidelines.md`)
- [ ] First 2 description lines restate the promise plus the keyword
- [ ] Chapters for long-form (timestamps, first at 0:00, ≥3 chapters, ≥10 s each)
- [ ] 3 relevant hashtags
- [ ] End screen + pinned comment with the next step
- [ ] Shorts: linked related video set where relevant
