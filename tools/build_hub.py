#!/usr/bin/env python3
"""Build the mobile Control Center page (hub/index.html) from repo files.

Usage: python3 tools/build_hub.py
Publish: Artifact tool with file_path hub/index.html and files {assets/...: brand/... }.
The page is generated: edit the source Markdown files, not hub/index.html.
"""
import html, pathlib, re, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/iayushpathak-dev/youtube/blob/claude/adoring-pasteur-aywagg/"


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t


def md(text):
    """Small Markdown renderer: headings, paragraphs, lists, tables, code, quotes."""
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("```"):
            j = i + 1; buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j]); j += 1
            code = html.escape("\n".join(buf))
            out.append(f'<div class="code"><button class="copy" type="button">Copy</button><pre>{code}</pre></div>')
            i = j + 1; continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            head, body = cells[0], [r for r in cells[1:] if not set("".join(r)) <= set("-: ")]
            t = '<div class="tbl"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(t + "</tbody></table></div>"); continue
        m = re.match(r"^(#{1,4})\s+(.*)", l)
        if m:
            lvl = min(len(m.group(1)) + 1, 5)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", l):
            tag = "ol" if re.match(r"^\s*\d+\.", l) else "ul"; items = []
            while i < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                item = re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i])
                item = item.replace("[ ] ", "☐ ").replace("[x] ", "☑ ")
                items.append(f"<li>{inline(item)}</li>"); i += 1
            out.append(f"<{tag}>{''.join(items)}</{tag}>"); continue
        if l.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").rstrip()); i += 1
            paras = "</p><p>".join(inline(b) for b in buf if b)
            out.append(f"<blockquote><p>{paras}</p></blockquote>"); continue
        if not l.strip() or l.strip() == "---":
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||```|>|\s*([-*]|\d+\.)\s)", lines[i]):
            buf.append(lines[i]); i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


def front(path):
    t = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); fm[k.strip()] = v.strip().strip('"')
        t = t[m.end():]
    return fm, t


def section_of(text, heading):
    i = text.find(heading)
    if i < 0:
        return ""
    j = text.find("\n## ", i + len(heading))
    return text[i + len(heading): j if j > 0 else None]


def read(p):
    return (ROOT / p).read_text(encoding="utf-8")


status = read("status/STATUS.md")
profile = read("brand/channel-profile.md")
calendar = read("strategy/calendar.md")
voice = read("brand/voice-clone.md")

about = re.search(r"## Description \(About\).*?```\n(.*?)```", profile, re.S).group(1).strip()
keywords = section_of(profile, "## Channel keywords").strip()

items = []
for folder in ("long", "shorts"):
    for p in sorted((ROOT / "content" / folder).glob("SWAI-*.md")):
        fm, body = front(p)
        if fm.get("production_status") == "KILLED":
            continue
        items.append((fm, body, p.relative_to(ROOT).as_posix()))
items.sort(key=lambda x: (x[0].get("publish_date", ""), x[0].get("id", "")))

def chip(s):
    cls = {"APPROVED": "ok", "PUBLISHED": "ok", "PROPOSED": "warn", "SCRIPTED": "info", "DRAFT": "muted"}.get(s, "muted")
    return f'<span class="chip {cls}">{html.escape(s)}</span>'

script_html = []
for fm, body, rel in items:
    d = fm.get("publish_date", "")
    try:
        dl = datetime.date.fromisoformat(d).strftime("%a %d %b")
    except ValueError:
        dl = d
    kind = "Long video" if fm.get("format") == "long" else "Short"
    script_html.append(f'''<details class="item" id="{fm.get('id','').lower()}">
<summary><span class="when">{dl}</span><span class="kind {'long' if kind=='Long video' else ''}">{kind}</span>
<span class="ttl">{html.escape(fm.get('title',''))}</span>
<span class="meta">{html.escape(fm.get('id',''))} {chip(fm.get('production_status',''))} {chip(fm.get('approval_status',''))}</span></summary>
<div class="body"><p class="hook"><strong>Hook:</strong> {inline(fm.get('hook',''))}</p>{md(body)}
<p class="src"><a href="{REPO}{rel}" target="_blank" rel="noopener">Open on GitHub ↗</a></p></div></details>''')

today = datetime.date.today().isoformat()
page = f'''<title>AI Made Usable HQ</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: one narrow reading column for phones, sticky chip nav, collapsible scripts. Brand: ink + mint. */
:root {{
  --bg:#F5F8F7; --panel:#FFFFFF; --fg:#0B1218; --muted:#55636E; --line:#DCE5E2;
  --accent:#0E9F7E; --accent-ink:#FFFFFF; --soft:#E2F5EF;
  --ok:#1C7C4A; --okbg:#DDF3E6; --warn:#8A5A00; --warnbg:#FFF0CC; --info:#1F5FA8; --infobg:#E1ECF8;
  --sans:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif; --mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#0A0E14; --panel:#111923; --fg:#E8EEF2; --muted:#93A3B0; --line:#1F2C38;
  --accent:#7CFFB2; --accent-ink:#06110C; --soft:#12261F;
  --ok:#7CE0A6; --okbg:#123022; --warn:#FFD27A; --warnbg:#33280F; --info:#9CC4FF; --infobg:#14243A; color-scheme:dark }} }}
:root[data-theme="dark"] {{
  --bg:#0A0E14; --panel:#111923; --fg:#E8EEF2; --muted:#93A3B0; --line:#1F2C38;
  --accent:#7CFFB2; --accent-ink:#06110C; --soft:#12261F;
  --ok:#7CE0A6; --okbg:#123022; --warn:#FFD27A; --warnbg:#33280F; --info:#9CC4FF; --infobg:#14243A; color-scheme:dark }}
* {{ box-sizing:border-box }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.55 var(--sans); }}
body::before {{ content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); z-index:10; background:var(--bg) }}
.wrap {{ max-width:760px; margin:0 auto; padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); padding-block:20px 64px }}
header.top h1 {{ font-size:26px; line-height:1.15; margin:0; letter-spacing:-.4px; text-wrap:balance }}
header.top h1 span {{ color:var(--accent) }}
header.top .sub {{ color:var(--muted); margin:6px 0 0; font-size:14px }}
nav {{ position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:var(--bg); margin:16px calc(-1 * max(16px,env(safe-area-inset-left,0px))) 0; padding:10px max(16px,env(safe-area-inset-left,0px)); display:flex; gap:8px; overflow-x:auto; border-bottom:1px solid var(--line); scrollbar-width:none }}
nav a {{ flex:none; text-decoration:none; color:var(--fg); background:var(--panel); border:1px solid var(--line); border-radius:999px; padding:6px 12px; font-size:13px; font-weight:600 }}
nav a:focus-visible, button:focus-visible, summary:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px }}
section {{ padding-top:24px; scroll-margin-top:64px }}
section > h2 {{ font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); margin:0 0 10px }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:14px 16px }}
.checks label {{ display:flex; gap:10px; align-items:flex-start; padding:9px 0; border-bottom:1px solid var(--line) }}
.checks label:last-child {{ border-bottom:0 }}
.checks input {{ width:20px; height:20px; accent-color:var(--accent); margin-top:2px; flex:none }}
.checks .who {{ font-size:12px; color:var(--muted) }}
.gallery {{ display:grid; grid-template-columns:1fr 1fr; gap:12px }}
.gallery figure {{ margin:0; min-width:0 }}
.gallery figure.wide {{ grid-column:1/-1 }}
.gallery img {{ display:block; width:100%; border-radius:10px; border:1px solid var(--line); background:#0A0E14 }}
.gallery img.round {{ border-radius:50%; max-width:180px; margin:0 auto }}
.gallery figcaption {{ font-size:12px; color:var(--muted); margin-top:6px; text-align:center }}
.hint {{ font-size:13px; color:var(--muted) }}
.code {{ position:relative; margin:10px 0 }}
.code pre {{ margin:0; background:var(--soft); border:1px solid var(--line); border-radius:10px; padding:12px; padding-top:34px; white-space:pre-wrap; word-break:break-word; font:13px/1.5 var(--mono) }}
.copy {{ position:absolute; top:6px; right:6px; font:600 12px var(--sans); background:var(--accent); color:var(--accent-ink); border:0; border-radius:8px; padding:5px 10px; cursor:pointer }}
.tbl {{ overflow-x:auto; margin:10px 0 }}
table {{ border-collapse:collapse; width:100%; font-size:13.5px }}
th, td {{ text-align:left; vertical-align:top; padding:7px 8px; border-bottom:1px solid var(--line) }}
th {{ color:var(--muted); font-weight:600; font-size:12px }}
td {{ min-width:90px }}
code {{ font:12.5px var(--mono); background:var(--soft); padding:1px 5px; border-radius:5px; word-break:break-word }}
blockquote {{ margin:10px 0; padding:4px 14px; border-left:3px solid var(--accent); color:var(--fg) }}
details.item {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; margin-bottom:10px }}
details.item summary {{ list-style:none; cursor:pointer; padding:12px 14px; display:grid; grid-template-columns:auto 1fr; gap:2px 10px }}
details.item summary::-webkit-details-marker {{ display:none }}
.when {{ font:500 12px var(--mono); color:var(--muted) }}
.kind {{ font-size:12px; font-weight:700; color:var(--muted); justify-self:end }}
.kind.long {{ color:var(--accent) }}
.ttl {{ grid-column:1/-1; font-weight:700; font-size:15.5px; line-height:1.3 }}
.meta {{ grid-column:1/-1; display:flex; gap:6px; align-items:center; flex-wrap:wrap; font:500 11.5px var(--mono); color:var(--muted) }}
.chip {{ font:600 11px var(--sans); padding:2px 8px; border-radius:999px }}
.chip.ok {{ color:var(--ok); background:var(--okbg) }} .chip.warn {{ color:var(--warn); background:var(--warnbg) }}
.chip.info {{ color:var(--info); background:var(--infobg) }} .chip.muted {{ color:var(--muted); background:var(--soft) }}
details.item .body {{ padding:0 14px 14px; border-top:1px solid var(--line); min-width:0 }}
.body h3 {{ font-size:16px; margin:18px 0 6px }} .body h4, .body h5 {{ font-size:14px; margin:14px 0 4px }}
.hook {{ background:var(--soft); border-radius:10px; padding:10px 12px; margin-top:12px }}
.src {{ font-size:13px }}
a {{ color:var(--accent) }}
.doc h2, .doc h3 {{ font-size:16px; margin:16px 0 6px }}
.doc h2:first-child {{ display:none }}
footer {{ margin-top:32px; font-size:12px; color:var(--muted) }}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior:auto }} }}
@media (min-width:640px) {{ .gallery {{ grid-template-columns:1fr 1fr 1fr }} header.top h1 {{ font-size:32px }} }}
</style>

<div class="wrap">
<header class="top">
  <h1>AI <span>Made</span> Usable HQ</h1>
  <p class="sub">@aimadeusable · Discover. Build. Automate. Ship. · Updated {today}</p>
</header>
<nav aria-label="Sections">
  <a href="#next">Next steps</a><a href="#week">This week</a><a href="#scripts">Scripts</a><a href="#brand">Brand kit</a><a href="#voice">Voice</a><a href="#status">Status</a>
</nav>

<section id="next"><h2>Your next steps</h2>
<div class="panel checks" id="checks">
  <label><input type="checkbox" id="c1"><span>Record the 2-minute voice sample (script in <a href="#voice">Voice</a>)<br><span class="who">You · phone, quiet room</span></span></label>
  <label><input type="checkbox" id="c2"><span>Create the Instant Voice Clone on elevenlabs.io, named <code>AI Made Usable - Creator</code><br><span class="who">You · 5 minutes</span></span></label>
  <label><input type="checkbox" id="c3"><span>Upload logo, banner, watermark and paste the About + keywords in YouTube Studio<br><span class="who">You · see <a href="#brand">Brand kit</a></span></span></label>
  <label><input type="checkbox" id="c4"><span>Read and approve this week's scripts (or tell Claude what to change)<br><span class="who">You · see <a href="#scripts">Scripts</a></span></span></label>
  <label><input type="checkbox" id="c5"><span>Record the Tuesday test in ChatGPT, Claude and Gemini (protocol inside SWAI-L001)<br><span class="who">You · by Monday</span></span></label>
  <label><input type="checkbox" id="c6"><span>Send recordings to Claude for editing, thumbnails and voiceovers<br><span class="who">You → Claude</span></span></label>
</div>
<p class="hint">Ticks are saved on this device only.</p>
</section>

<section id="week"><h2>This week</h2><div class="panel doc">{md(calendar)}</div></section>

<section id="scripts"><h2>Scripts</h2>{"".join(script_html)}</section>

<section id="brand"><h2>Brand kit</h2>
<div class="panel">
<div class="gallery">
  <figure><img class="round" src="assets/logo.png" alt="AI Made Usable logo: green arrow with two sparks"><figcaption>Profile picture · 800×800</figcaption></figure>
  <figure><img class="round" src="assets/watermark.png" alt="Round video watermark"><figcaption>Video watermark · 300×300</figcaption></figure>
  <figure class="wide"><img src="assets/banner.png" alt="Channel banner: AI Made Usable"><figcaption>Banner · 2560×1440</figcaption></figure>
</div>
<p class="hint">To save an image on your phone: open it, then long-press → Save image.</p>
<h3>About description</h3>
<div class="code"><button class="copy" type="button">Copy</button><pre>{html.escape(about)}</pre></div>
<h3>Channel keywords</h3>
<div class="code"><button class="copy" type="button">Copy</button><pre>{html.escape(keywords)}</pre></div>
<h3>Where it goes in YouTube Studio</h3>
<ol><li><strong>Customization → Basic info:</strong> Name <code>AI Made Usable</code>, paste the description.</li>
<li><strong>Customization → Profile:</strong> Picture = logo, Banner image = banner.</li>
<li><strong>Customization → Branding:</strong> Video watermark, display time "Entire video".</li>
<li><strong>Settings → Channel:</strong> paste the keywords. Then <strong>Publish</strong>.</li></ol>
</div></section>

<section id="voice"><h2>Voice</h2><div class="panel doc">{md(voice)}</div></section>

<section id="status"><h2>Project status</h2><div class="panel doc">{md(status)}</div></section>

<footer>Generated from the GitHub repo by <code>tools/build_hub.py</code>. <a href="https://github.com/iayushpathak-dev/youtube/tree/claude/adoring-pasteur-aywagg" target="_blank" rel="noopener">Open the repo ↗</a></footer>
</div>

<script>
document.querySelectorAll('.copy').forEach(function(b){{
  b.addEventListener('click',function(){{
    var pre=b.parentNode.querySelector('pre');
    var done=function(){{b.textContent='Copied';setTimeout(function(){{b.textContent='Copy'}},1500)}};
    try {{ navigator.clipboard.writeText(pre.innerText).then(done,function(){{sel(pre)}}) }} catch(e) {{ sel(pre) }}
  }});
}});
function sel(el){{ var r=document.createRange(); r.selectNodeContents(el); var s=getSelection(); s.removeAllRanges(); s.addRange(r); }}
document.querySelectorAll('#checks input').forEach(function(c){{
  try {{ c.checked = localStorage.getItem('hq-'+c.id)==='1' }} catch(e) {{}}
  c.addEventListener('change',function(){{ try {{ localStorage.setItem('hq-'+c.id, c.checked?'1':'0') }} catch(e) {{}} }});
}});
</script>
'''
out = ROOT / "hub" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"wrote {out.relative_to(ROOT)} ({len(page)//1024} KB), {len(items)} content items")
