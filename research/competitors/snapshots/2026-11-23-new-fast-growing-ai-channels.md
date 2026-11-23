# New, fast-growing AI channels (snapshot 2026-11-23)

Requested by the creator (2026-11-23): "learn from channels in the same domain that grew in the last 3 months".

## Method (and its limits)
- 10 YouTube searches (40 results each, `yt-dlp ytsearch40`, observed 2026-11-23): "chatgpt vs claude vs gemini", "best ai tools 2026", "ai agent no code tutorial", "claude code tutorial", "ai automation n8n", "ai tools you didn't know", "gemini 4 tips", "ai side hustle 2026", "vibe coding app", "ai for students". 193 unique channels.
- RSS (`feeds/videos.xml`) for each: the latest 15 uploads with dates and views. 150 channels had their 15th-latest upload after 2026-05-23 (active).
- For those 150: subscriber count and number of long videos (`/videos` tab), Shorts count (`/shorts` tab; partly incomplete because the job hit its time limit).
- **Channel age:** only certain when a channel has 15 uploads or fewer (then RSS shows its very first upload). For larger channels the start date is unknown. There is **no subscriber history** (Social Blade-type sites are not reachable), so "grew in 3 months" = subscribers reached within the known upload window.
- Excluded: big established channels (covered in `2026-11-21-phase1-channel-scan.md`), lifestyle vlogs (e.g. meshtimes), and channels whose views don't match their subscribers (AI Captain: 158K subs but its top video has 12K views, so the subscriber count is not organic-looking; not used as evidence).

## Confirmed new channels (FACT: all uploads visible in RSS, 2026-11-23)
| Channel | First upload | Long videos | Shorts | Subs | Top videos (views · length) |
|---|---|---|---|---|---|
| **InRecord** | 2026-10-16 | 8 | 0 | 32,900 | "How Modders Unlocked a $5,000 Chip Inside Normal Nvidia GPUs" 688K · 8:19 · "The Dark Reality of 'Vibe Coded' Clone Apps" 501K · 8:55 · "How Modders Used AI to Turn the PS5 Into a PC App" 421K · 8:09 |
| **AI by Alex** | 2026-09-27 | 12 | 0 | 58,600 | "Best AI Humanizer 2026: Walter Writes AI Tested" 55K · 5:20 · "Top 5 AI video generators in 2026" 50K · 5:26 · "5 AI tools that can save students hours every week in 2026" 33K · 5:45 |
| **Theo - Dawnspire Academy** | 2026-06-27 | 6 | 0 | 14,700 | "Build AI Agent Teams Better Than 99% of People" 22K · 9:41 · "I Ranked Every AI Agent Tool from Best to Worst (for Beginners)" 13K · 13:48 · "Every AI Agent Term Explained Like You're 5" 12K · 9:50 · "Building Your First AI Agent Is Actually Pretty Easy" 12K · 9:26 |

## Probably new (HYPOTHESIS: few long videos, all of the latest 15 since Sep 2026; true start date unknown)
| Channel | Long videos | Shorts | Subs | Top videos (views · length) |
|---|---|---|---|---|
| **James Blue** | 58 | 0 | 44,100 | "How to Study Anything with NotebookLM (Full System)" 349K · 9:18 · "7 AI Certifications Worth More than a Degree in 2026" 221K · 12:20 |
| **Matteo AI** | 24 | 0 | 11,100 | "ChatGPT-6 Astra Just Unlocked AI Motion Graphics" 133K · 12:07 · "I Gave Claude AI Full Control Of Blender (It Went Crazy)" 77K · 9:31 |
| **Ed Hill \| AI Automation** | 46 | 173 | 87,400 | "I Built an AI Voice Agent That Never Misses a Call (No Code)" 398K · 22:06 · "I Rebuilt a $12M AI App in 20 Minutes with No Code" 211K · 11:04 |

## External context (WebSearch, 2026-11-23)
- Branzly tracked 364 faceless channels from 15 Sep to 1 Nov 2026. Its fastest faceless grower above 100K was a finance channel (Casual Finance), not AI. https://www.branzly.com/youtube-insights/fastest-growing-faceless-youtube-channels
- Outlierkit ranks "AI tools tutorials" as the top-growing niche for 2026, but gives no clear method (treat as weak). https://outlierkit.com/resources/articles/top-10-most-profitable-youtube-niches-in-2026/

## What we learn (HYPOTHESES, each with the facts it rests on)
1. **New AI channels grew on long-form, not Shorts.** All three confirmed new channels have **0 Shorts**. James Blue and Matteo AI show 0 Shorts too. Only Ed Hill uses many Shorts. → Our Shorts are for discovery, but the Saturday long video is the main growth driver. Keep its quality highest.
2. **A story or curiosity frame beats a plain tutorial.** InRecord reached 32.9K subs from **8 videos** (avg ~300K views) with "How X did Y" / "The dark reality of Y" titles. → Frame our tests as stories ("I made 3 AIs…", "The AI that faked my streak").
3. **One concrete outcome per title, with the year.** "5 AI tools that can save students hours every week in 2026", "AI voice agent that never misses a call", "Study anything with NotebookLM". → Every title names who it's for and what they get.
4. **Beginner AI agents is a proven new-channel topic.** Theo's whole channel (6 videos, 14.7K subs) is "first AI agent", "explained like you're 5", "ranked for beginners". Ed Hill's "Build Your First AI Agent in 18 Minutes | No-Code" has 91K. → Supports DEC-022 (L002: "Build your first useful AI agent, no code").
5. **"I gave AI X" experiments travel.** "I Gave Claude AI Full Control Of Blender (It Went Crazy)" 77K on an 11K channel. → Fits our format: hand the AI a real job and show what happens.
6. **Students and careers are a strong audience.** "How to Study Anything with NotebookLM" 349K and "AI Certifications Worth More than a Degree" 221K. → A student-focused test ("I let 3 AIs study for my exam") is a strong future topic.
7. **Length:** the winning videos run **5–13 min** (InRecord ~8–9 min). Our 6-min L001 is inside the range. Future long videos can go to 8–10 min when the content supports it.
8. **Cadence:** AI by Alex posted 12 videos in ~8 weeks and InRecord 8 in ~5 weeks (FACT from RSS dates), so 1–2 long videos a week. We plan 1. More is a later decision for the creator.

## Next checks
- Re-run this scan in ~4 weeks (same queries) to measure each channel's subscriber change. That gives real growth data instead of a single snapshot.
- Look at thumbnails of the InRecord and AI by Alex top videos (i.ytimg.com works) before designing the L002 thumbnail.
