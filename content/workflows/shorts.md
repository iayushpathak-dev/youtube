# Shorts production workflow (daily, 45–60 s)

| Step | Who | Output | Status after |
|---|---|---|---|
| 1. Pick from opportunities / recent research. Assign the next `SWAI-S###` from the template | Claude | Item file | IDEA |
| 2. Research: facts, links, 3 competitor Shorts on the topic | Claude | Research + references sections | RESEARCHED |
| 3. Hook + 120–150-word script + on-screen plan | Claude | Script table | SCRIPTED |
| 4. Approval of title/hook/script (can be batched weekly) | Creator | `approval_status: APPROVED` | — |
| 5. AI narration (blocked until a TTS provider is approved, DEC-008) | Claude | `out/SWAI-S###/voice.wav` (git-ignored) | VOICED |
| 6. Visuals + captions + edit (ffmpeg / Remotion, 1080×1920) | Claude | `out/SWAI-S###/final.mp4` | EDITED |
| 7. Title, description, hashtags, related video | Claude | Packaging section | PACKAGED |
| 8. Upload + schedule in YouTube Studio | Creator (no upload integration) | Live video | PUBLISHED |
| 9. Set `video_url` and `publish_date`, update the calendar | Claude | — | — |
| 10. Performance pull at +48 h and +7 d → Performance table; lesson if notable | Claude | Performance, LES-### | — |

Quality bar: the hook lands in the first 1–2 s, there is one idea per Short, captions are readable, it ends with a payoff, and every claim is fact-checked with a source in Research.
