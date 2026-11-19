"""기술 스택 패널 이미지 생성. ROWS만 고치고 실행하면 stack.png가 다시 만들어진다.
실행: Playwright가 설치된 Python으로 `python render_panel.py` (Microsoft Edge 사용)
"""
import sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

ROWS = [
    ("Digital Forensics", ["KAPE", "FTK Imager", "EZ Tools", "RegRipper", "Timeline Explorer", "HxD"]),
    ("Detection & Response", ["Splunk / SPL", "Sigma", "Snort", "ModSecurity", "Wireshark"]),
    ("Reverse Engineering", ["IDA", "x32dbg", "GDB", "pwndbg", "pwntools", "PEview", "UPX"]),
    ("Offensive Security", ["Burp Suite", "Nmap", "sqlmap", "Hydra", "WPScan"]),
    ("Infrastructure & Cloud", ["Linux", "Windows Server", "AWS", "VMware ESXi", "pfSense", "VyOS", "OpenTofu"]),
    ("Development & Data", ["FastAPI", "React", "SQLite", "Elasticsearch", "Neo4j", "Git", "Postman", "Talend"]),
    ("Languages", ["Python", "C", "C++", "TypeScript", "SQL", "x86/x64 Assembly"]),
]

CSS = """
html,body{margin:0;background:transparent}
.panel{width:720px;box-sizing:border-box;padding:10px 26px;background:#FFFFFF;border:1px solid #E7E7E7;border-radius:12px;
 font-family:'Pretendard Variable',Pretendard,sans-serif;letter-spacing:-0.01em;word-break:keep-all;color:#52525B}
.row{display:grid;grid-template-columns:176px 1fr;gap:14px;align-items:start;padding:12px 0;border-top:1px solid #F0F0F0}
.row:first-child{border-top:0}
.lab{font-size:14.5px;font-weight:600;color:#27272A;line-height:1.35;padding-top:5px}
.tools{display:flex;flex-wrap:wrap;gap:6px}
.tools em{font-style:normal;font-size:13.5px;font-weight:450;line-height:1;padding:7px 10px;border-radius:6px;background:#FFFFFF;border:1px solid #E7E7E7}
"""


def html():
    rows = "".join(
        f'<div class="row"><div class="lab">{lab}</div><div class="tools">{"".join(f"<em>{x}</em>" for x in tools)}</div></div>'
        for lab, tools in ROWS)
    return ('<!doctype html><meta charset=utf-8>'
            '<link rel=stylesheet href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">'
            f'<style>{CSS}</style><div class=panel>{rows}</div>')


out = pathlib.Path(__file__).resolve().parent
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(device_scale_factor=2, viewport={"width": 760, "height": 800})
    f = out / "panel.html"
    f.write_text(html(), encoding="utf-8")
    pg.goto(f.as_uri())
    pg.wait_for_timeout(900)
    pg.locator(".panel").screenshot(path=str(out / "stack.png"), omit_background=True)
    b.close()
    f.unlink()
print("ok")
