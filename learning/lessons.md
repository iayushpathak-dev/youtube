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
