# Competitor intelligence: method

## Files
- `channels.md`: the registry. One row per channel. Updated in place, with every stat dated.
- `snapshots/YYYY-MM-DD-<topic>.md`: raw scan output plus notes for one research pass. Never edited afterwards. A later scan gets a new file.
- Conclusions that hold across scans go into `strategy/seo-packaging.md`, `research/audience/`, or `learning/lessons.md`. Snapshots are not the place for them.

## What to capture per channel (latest 6 months first)
Positioning · audience segment(s) · publishing frequency (long vs Shorts) · top recent long-form and Shorts by views ·
title patterns · thumbnail patterns · hooks (first 5–15 s, from transcripts) · storytelling structure · formats ·
engagement (likes/comments ratio where public) · comment themes · topics drawing interest.
Subscriber counts only as observed on the date. **Never infer growth curves or private metrics.**

## Commands (public data, verified 2026-11-21)
```bash
# Channel metadata: subscriber count + description (works)
yt-dlp --flat-playlist --playlist-end 1 -J "https://www.youtube.com/@HANDLE/videos" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['channel'],d['channel_follower_count'])"
# Upload list: views (rounded), duration, title, newest first. No dates in this mode. (works)
yt-dlp --flat-playlist --playlist-end 50 --print "%(view_count)s | %(duration)s | %(title)s" "https://www.youtube.com/@HANDLE/videos"
yt-dlp --flat-playlist --playlist-end 50 --print "%(view_count)s | %(title)s" "https://www.youtube.com/@HANDLE/shorts"
# Exact publish dates + exact views for the latest 15 uploads (long + Shorts) via RSS (works)
curl -s "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID"
# Search results for a query (works)
yt-dlp --flat-playlist --print "%(channel)s | %(view_count)s | %(title)s" "ytsearch20:QUERY"
```
**Blocked (2026-11-21):** per-video pages hit YouTube's "Sign in to confirm you're not a bot" check, so
**transcripts/auto-captions, comments, like counts and exact upload dates beyond the RSS window are not retrievable**.
Hooks and storytelling can therefore only be studied from titles, thumbnails and (if approved) a YouTube Data API key, which provides
comments and stats but not transcripts. See `status/integrations.md`.

## Cadence
- Full competitor pass: monthly (`reports/monthly/`).
- Quick scan of top channels' last 7 days: weekly (`reports/weekly/`).
