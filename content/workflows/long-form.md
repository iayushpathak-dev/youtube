# Long-form production workflow (weekly, Tuesday)

| Step | Who | Output | Status after |
|---|---|---|---|
| 1. Choose topic (opportunity + evidence). Assign the next `SWAI-L###` | Claude proposes, creator approves the topic | Item file | IDEA |
| 2. Research + competitor teardown (titles, structure, gaps) | Claude | Research + references | RESEARCHED |
| 3. Outline → full script for the creator's voice, with screen/graphic cues | Claude | Script | SCRIPTED |
| 4. Script approval | Creator | `approval_status: APPROVED` | — |
| 5. Voice recording (the creator reads the script; phone is fine) | Creator | Audio file shared with Claude | VOICED |
| 6. Builds/demos, screen captures, graphics, edit | Claude | `out/SWAI-L###/final.mp4` (git-ignored) | EDITED |
| 7. Packaging: title, thumbnail (1280×720), description, chapters, end screen | Claude drafts, creator approves | Packaging + thumbnail in `content/long/assets/` | PACKAGED |
| 8. Upload + schedule (Tue 19:30 IST) | Creator | Live video | PUBLISHED |
| 9. Derive Shorts candidates from the long-form | Claude | New SWAI-S items (IDEA) | — |
| 10. Performance pulls at +48 h, +7 d, +28 d (+ Studio export for CTR) | Claude / creator export | Performance table, LES-### | — |

Lead time target: topic approved by Thursday → script by Saturday → voice by Sunday → edit Mon → publish Tue.
(PROPOSED. Confirm once the workflow is exercised.)
