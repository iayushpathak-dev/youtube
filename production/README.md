# Production tools

- `shorts/render_short.py SPEC.json [--audio voice.mp3]`: renders a Short (1080×1920, 30 fps) from a scene spec in brand style. With `--audio`, scenes stretch to fit the voice track and the audio is loudness-normalised (−14 LUFS) and muxed. Output: `out/<ID>/` (git-ignored).
- `shorts/shoot.js`: HTML → PNG screenshots (Node Playwright), used by the renderer.
- Scene specs: `shorts/SWAI-S###.json` (kinds: title, sheet, stat, joke, round, score, big).
