# Channel analytics log

Append a row per pull. Source column: `windsor` | `studio-export` | `public`.

## Channel totals
| Pulled | Source | Subscribers | Public videos | Lifetime views | Notes |
|---|---|---|---|---|---|
| 2026-11-21 | windsor | 0 | 0 | 0 | Baseline before launch. The About description is empty. |

## Long-form (window totals)
| Pulled | Window | Videos in window | Views | Watch time (h) | Avg view duration | Avg % viewed | Subs + | Subs − | Impressions | CTR | Top traffic source |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Shorts (window totals)
| Pulled | Window | Shorts in window | Views | Engaged views | Avg % viewed | Likes | Shares | Subs + | Subs − | Top traffic source |
|---|---|---|---|---|---|---|---|---|---|---|

## 2026-11-25 (first check after launch)
Source: creator's YouTube Studio app screenshot, 25 Nov 2026 08:07 IST. Windsor.ai returned **no rows** for 23–25 Nov (YouTube Analytics lag; trial plan can't force-refresh).
- FACT: Overview (last 28 days, lagged): 257 views, 0.8 h watch time. Top content: S001 "I made ChatGPT, Claude and Gemini fight over a spreadsheet" 257.
- FACT: Real time: 478 views in the last 48 h; S001 307 of them. The rest (~171) is mostly S002 (published 24 Nov 18:30).
- FACT: S001 comments: 2 viewers (@hasanabdelhamid "GEMINI!!!", @proxsher Gemini pick with image).
- Estimate (HYPOTHESIS, from lagged totals): 0.8 h ≈ 48 min over 257 views ≈ 11 s per view on a 41 s Short ≈ **~27% average viewed**. Low for Shorts. Likely cause: the first 1–2 s is a title card, not a moment. Verify with Windsor `average_view_percentage` once the data lands (~27 Nov).
- Next check: 27–28 Nov via Windsor (views, average_view_percentage, likes, shares, subscribers_gained per video). Compare S001/S002 (no music) with S006+ (music) after 7 days each.
