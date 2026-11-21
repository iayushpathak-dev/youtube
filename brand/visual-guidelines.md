# Visual identity & creative guidelines

Status: **identity v2 final** (DEC-005, produced at the creator's request on 2026-11-21). v1 is archived in `brand/assets/archive/v1/`.

## Palette
| Token | Hex | Use |
|---|---|---|
| ink | `#0A0E14` | Primary background |
| ink-raised | `#132030` | Radial highlight / panels |
| mint | `#7CFFB2` | Accent gradient start, highlights |
| teal | `#22D3A6` | Accent gradient end, outlines |
| white | `#FFFFFF` | Headlines |
| mist | `#C9D4E0` | Secondary text |

The accent gradient is mint → teal at 90° for text and diagonal for marks. Keep at most one accent colour per frame.

## Typography
- Headlines: **Inter Display** ExtraBold/Black, tight tracking (−2 to −4 px at large sizes).
- Body / captions: **Inter** Medium/SemiBold.
- Code, terminal, labels: **JetBrains Mono**.
- All three are open-source (OFL) and installed in the build environment.

## Logo (v2, 2026-11-21)
- A bold up-right **"ship" arrow** (mint→teal gradient, soft glow) with two white **AI sparks**, on ink. It reads as "launch/ship + AI" for any audience (v1's `>_` prompt read developer-only).
- Files: `brand/assets/logo.png` (800×800), `brand/assets/watermark.png` (300×300, transparent). Source: `brand/assets/src/logo.html`.
- Checked as a circle crop at 200, 98 and 40 px (legible at all three). Keep the mark inside the central ~70%.
- Banner: `brand/assets/banner.png`. Checked at the 1546×423 all-device safe crop (logo and text have margin).
- Re-render after edits: `node tools/render-branding.js`.

## Asset specs (YouTube)
| Asset | Size | Notes |
|---|---|---|
| Profile picture | 800×800 PNG | Shown as a circle, down to ~98 px |
| Banner | 2560×1440, ≤6 MB | Safe area **1546×423** in the centre holds all text and logo |
| Long-form thumbnail | 1280×720 (16:9), ≤2 MB, JPG/PNG | Readable at ~168 px wide on mobile |
| Shorts | 1080×1920 (9:16) | Keep captions out of the bottom ~20% and right ~15% (UI overlays) |
| Video watermark | 300×300 transparent PNG (min 150×150, ≤1 MB) | `brand/assets/watermark.png`: round ink badge (88% opacity) + teal ring + mark. Transparent corners, so no box shows over video. Checked on light and dark footage. |

## Thumbnail rules (PROPOSED, to validate with data)
- One idea, ≤4 words of text, high contrast on ink.
- A face or a concrete object/result beats an abstract graphic (HYPOTHESIS, to test via `experiments/`).
- The title and thumbnail text complement each other and never repeat.

## Shorts visual style (PROPOSED)
- Burned-in captions in Inter Black, white with a mint highlight on the key word, centred in the upper-middle area.
- Hook text on screen in the first second.
- Brand corner tag `>_ ShippedWithAI` in JetBrains Mono at low opacity.
