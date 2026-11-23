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
.cliptop{{position:absolute;top:150px;display:flex;flex-direction:column;align-items:center;gap:24px}}
.cap{{font-weight:800;font-size:60px;line-height:1.1;max-width:920px}} .cap em{{font-style:normal;color:#7CFFB2}}
.clipbox{{position:absolute;top:560px;left:40px;width:1000px;height:1000px;border-radius:28px;border:4px solid #22D3A666;box-sizing:border-box}}
.badge{{position:absolute;top:1610px;font-family:'JetBrains Mono';font-weight:800;font-size:96px;color:#06110C;background:#7CFFB2;padding:10px 44px;border-radius:24px}}
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
    elif k == 'clip':
        badge = f"<div class='badge'>{html.escape(s['score'])}</div>" if s.get('score') else ''
        cap = f"<div class='cap'>{s['caption']}</div>" if s.get('caption') else ''
        body = f"<div class='cliptop'><div class='t {s['label']}'>{s['label']}</div>{cap}</div><div class='clipbox'></div>{badge}"
    elif k == 'score':
        brd = s.get('board', {}); body = "<div class='board'>" + ''.join(f"<div>{t}<span>{brd.get(t, '??')}</span></div>" for t in ['ChatGPT','Claude','Gemini']) + f"</div><div class='big'>{b}</div>{sub}"
    else:
        body = f"<div class='big'>{b}</div>{sub}"
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s'><div class='grid'></div>{body}{'' if k == 'clip' else f"<div class='brand'><img src='{logo}'>AI Made Usable</div>"}</div></body></html>"

files = []
for i, s in enumerate(spec['scenes']):
    f = out / f'scene{i:02d}.html'; f.write_text(scene_html(s), encoding='utf-8'); files.append(str(f))
subprocess.run(['node', str(ROOT / 'production/shorts/shoot.js'), *files], check=True)

durs = [s['dur'] for s in spec['scenes']]
if a.audio:
    alen = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',a.audio]).decode())
    says = [s.get('say') for s in spec['scenes']]
    if all(says):
        # Word-sync: each scene carries the narration it covers ("say"). Expected cut = character
        # share of the voice length, snapped to the nearest real pause in the audio (silencedetect).
        import re
        log = subprocess.run(['ffmpeg','-hide_banner','-i',a.audio,'-af','silencedetect=n=-32dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
        st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
        en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', log)]
        pauses = [(s + e) / 2 for s, e in zip(st, en) if 0.3 < s < alen - 0.3]
        lens = [len(re.sub(r'[^A-Za-z0-9]', '', t)) for t in says]; tot = sum(lens)
        lead = en[0] if st and st[0] < 0.05 and en else 0.0
        tail = st[-1] if st and len(st) > len(en) or (st and en and en[-1] >= alen - 0.05) else alen
        cuts, acc, prev = [0.0], 0, 0.0
        for L in lens[:-1]:
            acc += L; exp = lead + (tail - lead) * acc / tot
            near = [p for p in pauses if abs(p - exp) < 1.6 and p > prev + 0.8]
            c = min(near, key=lambda p: abs(p - exp)) if near else exp
            cuts.append(c); prev = c
        cuts.append(alen + 0.6)
        durs = [b - a_ for a_, b in zip(cuts, cuts[1:])]
        print('sync cuts:', ' '.join(f'{c:.2f}' for c in cuts))
    else:
        k = (alen + 0.6) / sum(durs); durs = [d * k for d in durs]
fps = 30; parts = []
for i, d in enumerate(durs):
    n = max(1, round(d * fps)); seg = out / f'seg{i:02d}.mp4'
    sc = spec['scenes'][i]
    if sc['kind'] == 'clip':
        src = str(ROOT / sc['src'])
        sdur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src]).decode())
        st = sc.get('start', 0); en = sc.get('end') or sdur
        speed = max((en - st) / d, 0.25)
        x, y, w, h = sc['crop']
        chain = f"[1:v]trim={st}:{en},setpts=(PTS-STARTPTS)/{speed:.4f},fps={fps}"
        if sc.get('blur'):
            for bi, (bx, by, bw, bh) in enumerate(sc['blur']):
                chain += f",split[m{bi}][b{bi}];[b{bi}]crop={bw}:{bh}:{bx}:{by},boxblur=luma_radius=8:luma_power=3:chroma_radius=4:chroma_power=3[bb{bi}];[m{bi}][bb{bi}]overlay={bx}:{by}"
        chain += f",crop={w}:{h}:{x}:{y},scale=992:992:force_original_aspect_ratio=decrease,pad=992:992:(ow-iw)/2:(oh-ih)/2:color=0x0A0E14,tpad=stop_mode=clone:stop_duration=30[c];[0:v][c]overlay=44:564,format=yuv420p"
        subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-framerate',str(fps),'-i',str(out/f'scene{i:02d}.png'),'-i',src,
            '-filter_complex',chain,'-frames:v',str(n),'-r',str(fps),'-c:v','libx264','-preset','veryfast','-crf','20','-an',str(seg)], check=True)
        parts.append(seg); continue
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
