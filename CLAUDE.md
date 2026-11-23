# CLAUDE.md: AI Made Usable operating instructions

This repository is the **permanent memory and source of truth** for the **AI Made Usable** YouTube channel (formerly ShippedWithAI, renamed 2026-11-21, DEC-017).
Anything not written here is not known to the next session. Read this file in full at the start of every session.

## 1. Project identity (approved, DEC-001)

- **Name:** AI Made Usable · **Handle:** @aimadeusable (claimed and verified 2026-11-21; previously @shippedwithaihq) · **Channel ID:** UCa2_ah_ehFCOyIn_QUt8t-w
- **Positioning:** *Discover. Build. Automate. Ship.*
- **Vision:** Build a global YouTube brand that helps everyone understand, explore, use and build with AI.
- **Audience:** students, beginners, developers, software engineers, content creators, entrepreneurs,
  business owners, working professionals, freelancers, AI enthusiasts, advanced AI users.
  AI is always the central theme.
- Full detail: `brand/identity.md`.

## 2. Operating assumptions (approved as initial assumptions, DEC-002 / DEC-003)

- One YouTube Short every day, 45–60 s, AI-assisted narration.
- One long-form video every **Saturday** (DEC-023, changed from Tuesday on 2026-11-23). **Faceless; all narration (long + Shorts) in the creator's ElevenLabs voice clone** (DEC-020). Claude produces the videos. The creator screen-records AI-app tests and uploads.
- These can only change with the creator's approval (see §5).

## 3. Session protocol

**At the start of every session:**
1. Read this file and `INDEX.md`.
2. Run `git status` and `git log --oneline -15` to see recent changes.
3. Read `status/STATUS.md`, including its pending tasks and blockers.
4. Read `status/decisions.md` and note every PROPOSED decision awaiting approval.
5. Read the knowledge files the task touches (use `INDEX.md` to find them).
6. Continue from the documented state. Do not restart work that is already recorded.

**After meaningful work:**
1. Update the relevant documentation in place. Never create a parallel copy of an existing database.
2. Save new research and learnings with **dates and source links**.
3. Update `status/STATUS.md` (what changed, what's next, blockers).
4. Record new approvals needed in `status/decisions.md` as PROPOSED.
5. If content items changed, run `python3 tools/content_index.py` to regenerate and validate `content/registry.md`.
6. Review `git diff`, then commit with a descriptive message and push to the working branch.
7. Verify the push (`git status` shows up to date with the remote). Never claim a push you didn't verify.
8. If scripts, calendar, status, brand or voice files changed, rebuild and republish the mobile Control Center: `python3 tools/build_hub.py`, then publish `hub/index.html` to https://claude.ai/artifact/B5BxntDZ8SeH6M4VqC7gRe (files: assets/logo.png, banner.png, watermark.png from `brand/assets/`). The creator uses it from their phone.

## 4. Knowledge rules

- **Facts vs hypotheses.** Label every finding as `FACT` (observed, sourced, dated) or
  `HYPOTHESIS` (inference, needs testing). Conclusions cite the facts they rest on.
- **Never invent data.** Do not invent subscriber growth, private analytics, CTR or anything else you
  could not retrieve. If data is unavailable, say so and name the access that's missing
  (`status/integrations.md`).
- **Update, don't duplicate.** Each type of information has exactly one home (`INDEX.md`).
  Add to it, and keep history: append dated entries, and mark old conclusions superseded instead of deleting them.
- **Recency.** Competitor and market research prioritises the most recent six months. Always record the
  date the data was observed. View and subscriber counts change.
- **Learning is explicit.** There is no background learning. Learning happens only when a session does real
  research or analysis and writes it down here. Never claim otherwise.

## 5. Decisions and approvals

The register is `status/decisions.md`, with statuses PROPOSED → APPROVED / REJECTED → IMPLEMENTED.

**The creator's explicit approval is required before:**
- changing brand positioning or making a major brand change (name, logo, banner, About text)
- changing the approved content strategy or content pillars
- changing the publishing schedule
- choosing a major new content direction
- running significant experiments
- publishing or scheduling any video, or changing a published video's metadata
- installing new paid or external services, or adding credentials

**Claude may do without asking** (within approved boundaries): research, analysis, reports, idea
development, draft scripts, documentation updates, recommendations, small operational tasks, and
committing and pushing to the working branch.

A recommendation is never an approved decision. An approval is recorded with its date and the creator's words.

## 6. Content system

- Every content item is one Markdown file with YAML front matter:
  - Shorts: `content/shorts/SWAI-S###-slug.md`
  - Long-form: `content/long/SWAI-L###-slug.md`
- IDs are sequential and **never reused**, even if an item is killed. Killed items keep their file with status `KILLED`.
- Templates: `content/templates/`. Workflows: `content/workflows/`. Schema and status values: `content/README.md`.
- `content/registry.md` is generated by `tools/content_index.py`. Never edit it by hand.
- Do not write scripts far in advance. Ideas evolve with research and real performance data.

## 7. Safety and git rules

- Never commit API keys, tokens, passwords, cookies or OAuth credentials. Credentials go through the
  environment's secret mechanism, never into files.
- Never force-push, rewrite history or delete project information without approval.
- Media files (`*.mp4`, `*.mov`, `*.wav`) and render output (`out/`) are git-ignored. Final assets that must be
  kept (logo, banner, thumbnails) are committed as PNG/JPG.
- Report blockers exactly (which tool, which host, which permission). Do not pretend an action succeeded.

## 8. Tools and integrations

The current inventory and gaps are in `status/integrations.md`. Check it before assuming any access.
Key points:
- Public YouTube research: `yt-dlp` list-level data + RSS (works). Per-video pages (comments, transcripts, likes) are **blocked**.
- Channel analytics: Windsor.ai YouTube connector (read analytics; edit video details, comments and playlists; **no upload**;
  no impressions/CTR/returning viewers; trial = last 30 days).
- Web research: the WebSearch tool.
- Do not install new tools or services without approval.

## 9. Language

The creator often writes in Hinglish. Reply in the language they use. Repository documents are written in English.
