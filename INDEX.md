# INDEX: where everything lives

One home per type of information. If you are about to create a file that duplicates one of these, update the existing one instead.

| # | Information | Location | Notes |
|---|---|---|---|
| — | Operating instructions | `CLAUDE.md` | Read first, every session |
| A | Brand identity & positioning | `brand/identity.md` | Positioning, vision, voice, audience promise |
| A | Channel settings (name, handle, About text, upload defaults) | `brand/channel-profile.md` | Mirrors what is (or should be) live in YouTube Studio |
| B | AI market research | `research/market/ai-landscape.md` | Dated, sourced entries per area |
| B | Research sources list | `research/market/sources.md` | Credible sources and how to access them |
| C | Competitor registry | `research/competitors/channels.md` | One row per channel, segment, observed stats with dates |
| C | Competitor research method | `research/competitors/README.md` | Commands, what to capture, cadence |
| C | Competitor raw snapshots | `research/competitors/snapshots/` | `YYYY-MM-DD-topic.md`, never edited after the fact |
| D | Audience segments | `research/audience/segments.md` | Needs, searches, struggles per segment |
| D | Audience insights log | `research/audience/insights-log.md` | Dated observations from comments, searches, feedback |
| E | Content strategy & pillars | `strategy/content-strategy.md` | Approved strategy only; proposals go in `strategy/proposals/` |
| E | Strategy proposals | `strategy/proposals/` | Not approved until the decision register says so |
| F | Publishing calendar | `strategy/calendar.md` | Scheduled slots → content IDs |
| G | Content database | `content/shorts/`, `content/long/` | One file per item, YAML front matter |
| G | Content registry (generated) | `content/registry.md` | `python3 tools/content_index.py` |
| G | Content schema & statuses | `content/README.md` | Field definitions and ID rules |
| H | Shorts production workflow | `content/workflows/shorts.md` | + template `content/templates/short.md` |
| I | Long-form production workflow | `content/workflows/long-form.md` | + template `content/templates/long.md` |
| J | Visual identity & creative guidelines | `brand/visual-guidelines.md` | Colours, type, asset specs |
| J | Brand assets | `brand/assets/` | Logo, banner, HTML sources (`tools/render-branding.js`) |
| K | YouTube SEO & packaging | `strategy/seo-packaging.md` | Titles, thumbnails, descriptions, tags |
| L | Channel analytics | `analytics/channel-log.md` | Dated channel-level snapshots; Shorts and long-form separate |
| L | Analytics method & metric availability | `analytics/README.md` | What can and cannot be pulled |
| M | Individual video performance | The item's own file in `content/` (section *Performance*) | Not duplicated elsewhere |
| N | Experiments & hypotheses | `experiments/register.md` | EXP-### with hypothesis, metric, result |
| O | Lessons learned | `learning/lessons.md` | LES-### linked to evidence |
| P | Strategic decisions & approvals | `status/decisions.md` | DEC-### register |
| Q | Weekly / monthly reports | `reports/weekly/`, `reports/monthly/` | Templates in `reports/README.md` |
| R | Future content opportunities | `research/opportunities.md` | Trends/topics not yet turned into content items |
| S | Project status & pending tasks | `status/STATUS.md` | Current phase, tasks, blockers, pending approvals |
| — | Tools & integrations inventory | `status/integrations.md` | What works, what's missing, minimum access needed |
| — | Scripts | `tools/` | `content_index.py`, `render-branding.js` |
