import sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

ROWS = [
    ("Digital Forensics", True, ["KAPE", "FTK Imager", "EZ Tools", "RegRipper", "Timeline Explorer", "HxD"]),
    ("Detection & Response", True, ["Splunk / SPL", "Sigma", "Snort", "ModSecurity", "Wireshark"]),
    ("Reverse Engineering", False, ["IDA", "x32dbg", "GDB", "pwndbg", "pwntools", "PEview", "UPX"]),
    ("Offensive Security", False, ["Burp Suite", "Nmap", "sqlmap", "Hydra", "WPScan"]),
    ("Infrastructure & Cloud", False, ["Linux", "Windows Server", "AWS", "VMware ESXi", "pfSense", "VyOS", "OpenTofu"]),
    ("Development & Data", False, ["FastAPI", "React", "SQLite", "Elasticsearch", "Neo4j", "Git", "Postman", "Talend"]),
    ("Languages", False, ["Python", "C", "C++", "TypeScript", "SQL", "x86/x64 Assembly"]),
]
THEMES = {
    "light": dict(bg="#FAFAFA", border="#E4E4E7", title="#18181B", text="#3F3F46", chip="#FFFFFF", chipb="#E4E4E7", acc="#047857", card=True),
    "dark": dict(bg="transparent", border="#30363D", title="#F4F4F5", text="#D4D4D8", chip="#161B22", chipb="#30363D", acc="#34D399", card=False),
}


def html(t):
    rows = []
    for lab, core, tools in ROWS:
        dot = "<i></i>" if core else "<b></b>"
        chips = "".join(f"<em>{x}</em>" for x in tools)
        cls = "core" if core else ""
        rows.append(f'<div class="row"><div class="lab">{dot}<span class="{cls}">{lab}</span></div><div class="tools">{chips}</div></div>')
    card = f"border:1px solid {t['border']};border-radius:14px;padding:18px 24px;" if t["card"] else "padding:4px 2px;"
    return f"""<!doctype html><meta charset=utf-8>
<link rel=stylesheet href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
<style>
html,body{{margin:0;background:transparent}}
.panel{{width:720px;box-sizing:border-box;{card}background:{t['bg']};font-family:'Pretendard Variable',Pretendard,sans-serif;letter-spacing:-0.01em;word-break:keep-all;color:{t['text']}}}
.row{{display:grid;grid-template-columns:184px 1fr;gap:16px;align-items:start;padding:13px 0;border-top:1px solid {t['border']}}}
.row:first-child{{border-top:0}}
.lab{{display:flex;align-items:center;gap:10px;font-size:15px;font-weight:600;color:{t['title']};line-height:1.35;padding-top:5px}}
.lab i,.lab b{{width:7px;height:7px;border-radius:50%;flex:none}}
.lab i{{background:{t['acc']}}}
.lab b{{visibility:hidden}}
.lab .core{{color:{t['acc']}}}
.tools{{display:flex;flex-wrap:wrap;gap:7px}}
.tools em{{font-style:normal;font-size:14px;font-weight:450;line-height:1;padding:7px 10px;border-radius:6px;background:{t['chip']};border:1px solid {t['chipb']}}}
</style><div class=panel>{''.join(rows)}</div>"""


out = pathlib.Path(__file__).resolve().parent
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    for name, t in THEMES.items():
        pg = b.new_page(device_scale_factor=2, viewport={"width": 760, "height": 800})
        f = out / f"panel-{name}.html"
        f.write_text(html(t), encoding="utf-8")
        pg.goto(f.as_uri())
        pg.wait_for_timeout(900)
        pg.locator(".panel").screenshot(path=str(out / f"skills-{name}.png"), omit_background=True)
    b.close()
print("ok")
