# Tools and integrations inventory

Last verified: **2026-11-21** (cloud Claude Code session). Re-verify when something fails, because access depends on the session's environment.

| Capability | Status | How | Limits / notes |
|---|---|---|---|
| GitHub (repo `iayushpathak-dev/youtube`) | ✅ Works | git push to the `claude/*` working branch; GitHub MCP tools | The repo's **default branch is `claude/gifted-gates-6r6omc`** (there is no `main`). PR #1 (initialization) was merged into it on/before 2026-11-21. Push only to the session's working branch. Merging needs a PR the creator approves. |
| YouTube public data: channel lists, search, subscriber counts | ✅ Works | `yt-dlp --flat-playlist` (videos/shorts tabs, `ytsearchN:`, `-J` for channel metadata) | Views are rounded in list mode. No upload dates in list mode. ~8% of search results come back without channel/views (2026-11-21), and an empty query can succeed on retry. |
| YouTube thumbnails | ✅ Works | `https://i.ytimg.com/vi/<id>/mqdefault.jpg` | For visual review only. Do not commit other channels' thumbnails to the repo. |
| YouTube publish dates + exact views (latest 15 uploads per channel) | ✅ Works | RSS `youtube.com/feeds/videos.xml?channel_id=…` | 15 most recent only. |
| YouTube per-video pages: transcripts, comments, likes | ❌ Blocked | yt-dlp gets "Sign in to confirm you're not a bot" | Using account cookies is **not recommended** (it risks the creator's account). Alternative: a YouTube Data API key (comments and stats, no transcripts). |
| YouTube Data API v3 | ❌ No key | `googleapis.com` reachable (returns 403 without a key) | **Recommended minimum addition:** a free API key gives competitor comments, exact stats and dates for any time range. |
| Own channel analytics | ⚠️ Partial | Windsor.ai connector (`youtube` connector, linked to the channel's Google account) | Views, watch time, avg view duration/%, likes, comments, shares, subs gained/lost, traffic source + detail (search terms), device, geography, demographics, retention curve, content type (Shorts vs long). **Not available:** impressions, thumbnail CTR, unique viewers, new vs returning viewers, Shorts "stayed to watch". **Trial:** last 30 days of history only. Connector tools load only in sessions where the creator's claude.ai connector is enabled. |
| Own channel write actions | ⚠️ Partial | Windsor.ai | update_video_details, reply/moderate/delete comment, add/remove playlist. **No upload, no scheduling, no channel branding/About edits.** Every write needs the creator's approval (CLAUDE.md §5). |
| Web research (AI market, news, docs) | ✅ Works | WebSearch tool; web-fetch agent | US-only search results. |
| Google Trends | ❌ Blocked | `trends.google.com` refused by network policy | Needs the host allowed. |
| Reddit / Hacker News (community discussion) | ❌ Blocked | `reddit.com`, `hn.algolia.com` refused by network policy | Needs the hosts allowed. Partial substitute: WebSearch. |
| Text-to-speech for Shorts | ✅ Works (2026-11-21) | **ElevenLabs connector** (claude.ai, OAuth): `creative_generate_speech`, `creative_list_voices`, `account_get_usage` | Starter plan, 40k chars/month. No tool to clone a voice from a recording, so the creator does that once on elevenlabs.io. Only loads in sessions where the connector is enabled. |
| Video production | ⚠️ Partial | ffmpeg 6.1.1 ✅, Chromium + Playwright ✅ (render HTML → PNG), Python ✅ | Remotion / HyperFrames are declared in `package.json` but **not installed** in this session (`npm install` needed; these are already-declared project dependencies). |
| Fonts | ✅ | Inter, Inter Display, JetBrains Mono installed locally | Used by the brand assets. |
| Scheduled / recurring sessions | ✅ Available | Scheduled-task tools | Not created. See DEC-009. |

## Missing access, minimum needed

1. **Competitor comments, likes and full date history**: a YouTube Data API v3 key (free, from Google Cloud) stored as an environment secret. This is the highest-value addition for the research phase.

2. **Impressions & CTR, returning viewers**: not exposed by the connector. Minimum: the creator exports *YouTube Studio → Analytics → Advanced mode → Export (CSV)* weekly and drops it in `analytics/snapshots/`, **or** a direct YouTube Analytics API OAuth connection (larger setup).
3. **Analytics history beyond 30 days**: Windsor.ai paid plan, or the weekly snapshots kept in `analytics/` (recommended: free, and builds our own history).
4. **Trend and community research**: allow `trends.google.com`, `www.reddit.com`, `hn.algolia.com` in the environment network policy (needs the creator's approval).
5. **TTS**: one provider host plus an API key secret (DEC-008).
6. **Upload/scheduling**: manual in YouTube Studio by the creator. No available integration does it.

## Checked 2026-11-21: can Claude run the ChatGPT / Gemini tests itself?
- No ChatGPT/OpenAI or Google Gemini (AI assistant) connector exists in the directory search. The "Gemini" connector listed there is the **Gemini crypto exchange**, which is unrelated. Do not connect it for this.
- An API route would be possible (OpenAI + Google AI API keys as environment secrets, plus allowing `api.openai.com` and `generativelanguage.googleapis.com`), but (1) it costs per use, (2) **API ≠ the apps viewers use** (file upload UI, browsing, canvas/app preview, default models), and (3) Claude operating the test would make Claude both a contestant and the operator, which weakens trust.
- Decision for SWAI-L001: the creator screen-records the three consumer apps (no face, no mic). Claude does everything else.
