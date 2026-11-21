# Analytics: method

## Where data lives
- Channel level, over time: `analytics/channel-log.md` (dated rows, **Shorts and long-form in separate tables**).
- Per video: the item's own file in `content/` (Performance section). Not duplicated here.
- Raw exports (Studio CSVs, connector dumps): `analytics/snapshots/YYYY-MM-DD-<what>.csv|md`.

## Sources and metric availability (verified 2026-11-21)
| Metric | Windsor.ai connector field | Available? |
|---|---|---|
| Views / engaged views | `views`, `engaged_views` | ✅ |
| Watch time | `estimated_minutes_watched` | ✅ |
| Avg view duration / % viewed | `average_view_duration`, `average_view_percentage` | ✅ |
| Retention curve | `audience_watch_ratio`, `relative_retention_performance` by `elapsed_video_time_ratio` (filter one video) | ✅ |
| Subscribers gained/lost | `subscribers_gained`, `subscribers_lost` (per video) · `*_channel` (per day) | ✅ |
| Subscriber total | `subscriber_count` (snapshot) | ✅ |
| Likes / comments / shares | `likes`, `comments`, `shares` | ✅ |
| Comment text | `comment_text`, `comment_author`, `comment_video_id` | ✅ (needs manage permission) |
| Traffic sources / search terms | `traffic_source`, `traffic_source_detail` | ✅ |
| Geography / device / demographics | `country`, `device_type`, `viewer_age_group`, `viewer_gender` | ✅ (demographics as % only) |
| Shorts vs long-form split | `creator_content_type` | ✅ |
| Subscribed vs not | `subscribed_status` | ✅ |
| **Impressions, thumbnail CTR** | — | ❌ Studio export only |
| **Unique / new / returning viewers** | — | ❌ Studio export only |
| History > 30 days | — | ❌ on the Windsor trial. Our own dated log in this folder is the long-term history. |

Rules: always record the pull date and window. Never estimate a missing metric. Mark it `n/a (no access)`.

## Cadence (once publishing starts; recurring session pending DEC-009)
- Each video: +48 h, +7 d, +28 d pulls into its content file.
- Weekly: channel row in `channel-log.md` + weekly report.
- Weekly (creator, ~2 min): Studio → Analytics → Advanced mode → Export → put the CSV in `analytics/snapshots/` for impressions/CTR/returning viewers.
