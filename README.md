# AI Made Usable

**Discover. Build. Automate. Ship.** A YouTube channel (formerly ShippedWithAI) helping everyone understand, explore, use and build with AI.

This repository is the channel's operating system and permanent memory.

- Start here: [`CLAUDE.md`](CLAUDE.md) (operating rules) → [`INDEX.md`](INDEX.md) (where everything lives) → [`status/STATUS.md`](status/STATUS.md) (current state)
- Decisions: [`status/decisions.md`](status/decisions.md)
- Latest research: [`reports/research/2026-11-21-phase-1-research-report.md`](reports/research/2026-11-21-phase-1-research-report.md)

## Tooling
```bash
pip install -r requirements.txt   # yt-dlp (public YouTube research), pandas
npm install                       # Remotion + HyperFrames (motion graphics, captions)
```
FFmpeg is used for audio/video processing. Helper scripts are in `tools/`:
- `python3 tools/content_index.py`: validate content items and regenerate `content/registry.md`
- `node tools/render-branding.js`: render `brand/assets/src/*.html` → PNG
