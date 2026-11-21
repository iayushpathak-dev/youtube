# Visual identity & creative guidelines

Status: the v1 identity is **PROPOSED** (DEC-005). The logo is recommended to keep. The banner needs a revision to match DEC-001.

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

## Logo
- A `>_` terminal prompt (mint→teal, soft glow) plus a white up-right "ship" arrow on ink. File: `brand/assets/logo.png` (800×800). Source: `brand/assets/src/logo.html`.
- YouTube crops it to a circle, so keep the mark inside the central ~70%.
- Re-render after edits: `node tools/render-branding.js`.

## Asset specs (YouTube)
| Asset | Size | Notes |
|---|---|---|
| Profile picture | 800×800 PNG | Shown as a circle, down to ~98 px |
| Banner | 2560×1440, ≤6 MB | Safe area **1546×423** in the centre holds all text and logo |
| Long-form thumbnail | 1280×720 (16:9), ≤2 MB, JPG/PNG | Readable at ~168 px wide on mobile |
| Shorts | 1080×1920 (9:16) | Keep captions out of the bottom ~20% and right ~15% (UI overlays) |
| Video watermark | 150×150 PNG | Optional, use the logo |

## Thumbnail rules (PROPOSED, to validate with data)
- One idea, ≤4 words of text, high contrast on ink.
- A face or a concrete object/result beats an abstract graphic (HYPOTHESIS, to test via `experiments/`).
- The title and thumbnail text complement each other and never repeat.

## Shorts visual style (PROPOSED)
- Burned-in captions in Inter Black, white with a mint highlight on the key word, centred in the upper-middle area.
- Hook text on screen in the first second.
- Brand corner tag `>_ ShippedWithAI` in JetBrains Mono at low opacity.
