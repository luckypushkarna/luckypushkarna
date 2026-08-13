import os

ROWS = [
    ("role", "Full-Stack Engineer"),
    ("focus", "Distributed Systems & Automation"),
    ("stack", "Python · Go · React · PostgreSQL"),
    ("now", "Building self-animating terminal profile READMEs"),
    ("status", "Available for select freelance & roles")
]

def render_panel(output_svg="sysinfo.svg"):
    is_preview = os.getenv("PREVIEW") == "1"
    
    width = 460
    row_height = 28
    header_height = 40
    height = header_height + (len(ROWS) * row_height) + 20
    
    css_rules = []
    svg_rows = []
    
    for idx, (label, val) in enumerate(ROWS):
        y_pos = header_height + (idx * row_height) + 18
        delay = 0.2 + (idx * 0.3) if not is_preview else 0
        
        if not is_preview:
            css_rules.append(f"""
            .line-{idx} {{
                animation: fadeInLine 0.4s ease-out {delay:.2f}s forwards;
                opacity: 0;
            }}""")
        
        svg_rows.append(f"""
        <g class="line-{idx}">
            <text x="25" y="{y_pos}" class="label">{label}:</text>
            <text x="95" y="{y_pos}" class="val">{val}</text>
        </g>""")
        
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <style>
        .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 6px; }}
        .header-title {{ font-family: monospace; font-size: 12px; fill: #8b949e; font-weight: bold; }}
        .label {{ font-family: monospace; font-size: 13px; fill: #ff79c6; font-weight: bold; }}
        .val {{ font-family: monospace; font-size: 13px; fill: #f8f8f2; }}
        @keyframes fadeInLine {{
            from {{ opacity: 0; transform: translateX(-5px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        {''.join(css_rules) if not is_preview else ''}
    </style>
    <rect width="100%" height="100%" class="bg"/>
    
    <!-- Window Header Controls -->
    <circle cx="20" cy="20" r="5" fill="#ff5f56"/>
    <circle cx="35" cy="20" r="5" fill="#ffbd2e"/>
    <circle cx="50" cy="20" r="5" fill="#27c93f"/>
    <text x="70" y="24" class="header-title">system_info.sh</text>
    <line x1="0" y1="35" x2="{width}" y2="35" stroke="#30363d" stroke-width="1"/>
    
    {''.join(svg_rows)}
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ System Panel saved to {output_svg}")

if __name__ == "__main__":
    render_panel()
