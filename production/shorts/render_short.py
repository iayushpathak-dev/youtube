#!/usr/bin/env python3
"""Render a Short's visual track from a scene spec (JSON) into out/<ID>/.

  python3 production/shorts/render_short.py production/shorts/SWAI-S001.json [--audio voice.mp3]

Scenes -> PNG (Playwright, brand style) -> MP4 1080x1920 30fps with a slow punch-in per scene.
With --audio: scene durations are scaled to fit the voice track, and the audio is muxed in.
"""
import json, sys, subprocess, pathlib, html, argparse
ROOT = pathlib.Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser(); ap.add_argument('spec'); ap.add_argument('--audio'); a = ap.parse_args()
spec = json.load(open(a.spec)); sid = spec['id']
out = ROOT / 'out' / sid; out.mkdir(parents=True, exist_ok=True)
logo = (ROOT / 'brand/assets/logo.png').as_uri()
CSS = f"""
html,body{{margin:0;width:1080px;height:1920px;background:#0A0E14;font-family:'Inter Display',Inter,sans-serif;color:#fff;overflow:hidden}}
.s{{position:relative;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 38%,#173047 0%,#0A0E14 62%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:56px;text-align:center;padding:0 80px;box-sizing:border-box}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(#ffffff08 2px,transparent 2px),linear-gradient(90deg,#ffffff08 2px,transparent 2px);background-size:90px 90px}}
.kicker{{font-family:'JetBrains Mono';font-weight:700;font-size:44px;letter-spacing:6px;color:#7CFFB2;border:4px solid #22D3A6aa;padding:14px 30px;border-radius:18px;position:relative}}
.big{{font-weight:900;font-size:118px;line-height:1.02;letter-spacing:-3px;position:relative;text-wrap:balance}}
.big em{{font-style:normal;background:linear-gradient(90deg,#7CFFB2,#22D3A6);-webkit-background-clip:text;color:transparent}}
.sub{{font-weight:600;font-size:56px;color:#C9D4E0;position:relative}}
.tiles{{display:flex;gap:26px;position:relative}}
.t{{width:290px;height:170px;border-radius:30px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:58px;border:5px solid #ffffff22}}
.t.ChatGPT{{background:#10A37F44}}.t.Claude{{background:#D9775744}}.t.Gemini{{background:#4285F444}}
.t.solo{{width:560px;height:220px;font-size:88px}}
.lines div{{font-weight:900;font-size:130px;line-height:1.15}} .lines div:nth-child(2){{color:#7CFFB2}}
.rn{{font-family:'JetBrains Mono';font-size:54px;color:#7CFFB2;letter-spacing:4px}} .emo{{font-size:220px;line-height:1}}
.sheet{{display:grid;grid-template-columns:repeat(4,170px);gap:10px;position:relative;opacity:.9}}
.sheet div{{height:70px;background:#ffffff10;border-radius:8px}} .sheet div.l{{background:#22D3A633;display:flex;align-items:center;justify-content:center;font-size:44px}}
.board{{display:flex;flex-direction:column;gap:22px;position:relative}}
.board div{{display:flex;justify-content:space-between;width:760px;font-weight:800;font-size:64px;padding:22px 40px;border-radius:24px;background:#ffffff0d}}
.board span{{font-family:'JetBrains Mono';color:#7CFFB2}}
.brand{{position:absolute;bottom:250px;display:flex;align-items:center;gap:20px;font-weight:800;font-size:44px;opacity:.85}}
.brand img{{width:84px;height:84px;border-radius:50%}}
"""
def scene_html(s):
    b = s.get('big', ''); sub = f"<div class='sub'>{html.escape(s['sub'])}</div>" if s.get('sub') else ''
    k = s['kind']
    if k == 'title':
        body = f"<div class='kicker'>{s['kicker']}</div><div class='big'>{b}</div><div class='tiles'>" + ''.join(f"<div class='t {t}'>{t}</div>" for t in s['tiles']) + "</div>"
    elif k == 'sheet':
        cells = ''.join(f"<div class='{'l' if i in (5,10,15) else ''}'>{'🔒' if i in (5,10,15) else ''}</div>" for i in range(20))
        body = f"<div class='sheet'>{cells}</div><div class='big'>{b}</div>{sub}"
    elif k == 'stat':
        body = "<div class='lines'>" + ''.join(f"<div>{html.escape(x)}</div>" for x in s['lines']) + "</div>"
    elif k == 'joke':
        body = f"<div class='t {s['tile']} solo'>{s['tile']}</div><div class='big'>{b}</div>"
    elif k == 'round':
        body = f"<div class='rn'>ROUND {s['n']}</div><div class='emo'>{s['emoji']}</div><div class='big'>{html.escape(b)}</div>"
    elif k == 'score':
        body = "<div class='board'>" + ''.join(f"<div>{t}<span>??</span></div>" for t in ['ChatGPT','Claude','Gemini']) + f"</div><div class='big'>{b}</div>{sub}"
    else:
        body = f"<div class='big'>{b}</div>{sub}"
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s'><div class='grid'></div>{body}<div class='brand'><img src='{logo}'>AI Made Usable</div></div></body></html>"

files = []
for i, s in enumerate(spec['scenes']):
    f = out / f'scene{i:02d}.html'; f.write_text(scene_html(s), encoding='utf-8'); files.append(str(f))
subprocess.run(['node', str(ROOT / 'production/shorts/shoot.js'), *files], check=True)

durs = [s['dur'] for s in spec['scenes']]
if a.audio:
    alen = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',a.audio]).decode())
    k = (alen + 0.6) / sum(durs); durs = [d * k for d in durs]
fps = 30; parts = []
for i, d in enumerate(durs):
    n = max(1, round(d * fps)); seg = out / f'seg{i:02d}.mp4'
    subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-i',str(out/f'scene{i:02d}.png'),'-vf',
        f"scale=1188:2112,zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={fps}",
        '-frames:v',str(n),'-pix_fmt','yuv420p','-c:v','libx264','-preset','veryfast','-crf','20',str(seg)], check=True)
    parts.append(seg)
(out/'list.txt').write_text(''.join(f"file '{x.name}'\n" for x in parts))
silent = out / f'{sid}-visual.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(out/'list.txt'),'-c','copy',str(silent)], check=True)
if a.audio:
    final = out / f'{sid}-final.mp4'
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(silent),'-i',a.audio,'-filter:a','loudnorm=I=-14:TP=-1.5:LRA=11','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',str(final)], check=True)
    print('final:', final)
print('visual:', silent, f'{sum(durs):.1f}s')
