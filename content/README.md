# Content database

One Markdown file per content item. **The file is the record**: front matter for structured fields, body for research, script and performance.

- Shorts: `content/shorts/SWAI-S###-<slug>.md` (template `templates/short.md`)
- Long-form: `content/long/SWAI-L###-<slug>.md` (template `templates/long.md`)
- Registry: `content/registry.md`, **generated** by `python3 tools/content_index.py` (also validates IDs and fields).

## ID rules
- `SWAI-S001`, `SWAI-S002`, … for Shorts. `SWAI-L001`, … for long-form. Three digits, sequential.
- Take the next number after the highest existing ID (including KILLED items). **Never reuse an ID.**
- The file name starts with the ID. The slug may change, the ID never does.

## Fields (front matter)
| Field | Values / format |
|---|---|
| id | SWAI-S### / SWAI-L### |
| format | short \| long |
| topic | short text |
| segments | list of codes from `research/audience/segments.md` |
| pillar | pillar name (pending DEC-010) |
| objective | reach \| subscribers \| watch-time \| trust \| conversion \| test |
| hypothesis | one sentence: "If …, then … (metric)" |
| title | working title |
| hook | first line / first 3 s |
| production_status | IDEA → RESEARCHED → SCRIPTED → VOICED → EDITED → PACKAGED → PUBLISHED, or KILLED |
| approval_status | DRAFT → PROPOSED → APPROVED / REJECTED |
| publish_date | YYYY-MM-DD or empty |
| video_url | after publishing |
| experiments | list of EXP-### |
| created / updated | YYYY-MM-DD |

Body sections: Research · Competitor references · Script · Visual direction · Packaging · Performance · Lessons learned.
**Performance data for a video lives only in its own file** (INDEX row M). Channel-level data lives in `analytics/`.

## Status rules
- Nothing goes to PUBLISHED or onto the calendar as SCHEDULED without `approval_status: APPROVED`.
- A KILLED item keeps its file and gets a one-line reason in *Lessons learned*.
