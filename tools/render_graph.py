import json

LEVELS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]  # Terminal Green Ramp

def render_graph(json_path="assets/contributions.json", output_svg="graph.svg"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    cell_size = 11
    cell_gap = 3
    padding_x, padding_y = 20, 30
    
    weeks = len(data) // 7
    svg_w = padding_x * 2 + (weeks * (cell_size + cell_gap))
    svg_h = padding_y * 2 + (7 * (cell_size + cell_gap)) + 15
    
    css_rules = []
    rect_elements = []
    
    for idx, day in enumerate(data):
        col = idx // 7
        row = idx % 7
        
        x = padding_x + col * (cell_size + cell_gap)
        y = padding_y + row * (cell_size + cell_gap)
        
        color = LEVELS[min(day["level"], len(LEVELS) - 1)]
        delay = col * 0.03  # Wave sequence animate per week column
        
        css_rules.append(f"""
        .c-{idx} {{
            animation: popIn 0.3s ease-out {delay:.2f}s forwards;
            transform-origin: {x + 5}px {y + 5}px;
            opacity: 0;
        }}""")
        
        rect_elements.append(
            f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
            f'rx="2" fill="{color}" class="c-{idx}" />'
        )

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
    <style>
        .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 6px; }}
        .title {{ font-family: monospace; font-size: 12px; fill: #8b949e; font-weight: bold; }}
        @keyframes popIn {{
            from {{ opacity: 0; transform: scale(0.3); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
        {''.join(css_rules)}
    </style>
    <rect width="100%" height="100%" class="bg"/>
    <text x="{padding_x}" y="18" class="title">$ git log --contributions --year=latest</text>
    {''.join(rect_elements)}
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Animated contribution graph saved to {output_svg}")

if __name__ == "__main__":
    render_graph()
