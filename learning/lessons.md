# Lessons learned

Append-only. A lesson needs evidence (data, link or content ID). If a later lesson overturns one, mark the old one `SUPERSEDED by LES-###` and keep it.

```
### LES-### · YYYY-MM-DD · area (content | packaging | audience | production | process | tools)
- Evidence:
- Lesson:
- Applies to / changes:
```

### LES-001 · 2026-11-21 · tools
- Evidence: yt-dlp per-video requests return "Sign in to confirm you're not a bot". Flat channel/search listings, `-J` channel metadata and RSS feeds work.
- Lesson: Plan competitor research around list data + RSS. Comments, likes and history need a YouTube Data API key. Transcripts are not available.
- Applies to: `research/competitors/README.md`, `status/integrations.md`.

### LES-002 · 2026-11-21 · production
- Evidence: Logo render. An SVG gradient with the default `objectBoundingBox` units makes a perfectly horizontal or vertical line disappear (its bounding box has zero height), and a default filter region clips the glow.
- Lesson: In brand SVGs, use `gradientUnits="userSpaceOnUse"` and an explicit `filterUnits="userSpaceOnUse"` region. Always look at the rendered PNG before shipping it.
- Applies to: `brand/assets/src/`, future Remotion/HTML graphics.

### LES-003 · 2026-11-21 · process
- Evidence: Analytics connector field list (Windsor.ai, 2026-11-21).
- Lesson: Impressions/CTR and returning viewers are not available via the connector, so packaging decisions need a weekly Studio export. Without it, CTR-based conclusions must not be made.
- Applies to: `analytics/README.md`.

### LES-004 · 2026-11-21 · tools
- Evidence: Phase 1 searches: 49 of 600 `ytsearch` results came back with no channel or view metadata, and two whole queries returned nothing on the first run but worked on retry.
- Lesson: Retry empty searches once. Count and report metadata-less results instead of silently dropping them.
- Applies to: `research/competitors/README.md`.

### LES-005 · 2026-11-21 · process
- Evidence: Competitor titles referenced model names (e.g. "Fable 5.2", "GPT-6.2 Astra", "Seedance 2.5") that web search could not confirm, while others (GPT-6 Astra, Gemini 4, Opus 5.5) were confirmed by primary sources.
- Lesson: Creator titles are evidence of **attention**, not of **facts**. Verify any product/version claim with a primary or reputable source before using it in a script.
- Applies to: all scripts (research step), `research/market/ai-landscape.md`.

### LES-006 · 2026-11-21 · analysis
- Evidence: A first draft of the Phase 1 report said "32 channels, Shorts ~3–35% of long-form". Recomputing from the data gave 25 channels (≥5 Shorts), median 11%, range 3–72%.
- Lesson: Recompute every summary statistic from the saved data before it goes into a report or decision. Never paraphrase numbers from memory.
- Applies to: reports, decision evidence.

### LES-007 · 2026-11-21 · production
- Evidence: Banner v3 looked fine at full size, but the 1546×423 safe-area crop showed the logo circle touching the left edge.
- Lesson: Always check banners at the safe-area crop (the phone view), not just at full size. Centre content with margin inside 1546×423.
- Applies to: `brand/assets/src/banner.html`, any future banner.
