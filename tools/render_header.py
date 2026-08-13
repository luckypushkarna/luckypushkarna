# tools/render_header.py
def generate_peaceful_header(output_svg="header.svg"):
    width, height = 820, 180
    
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
    <style>
        .bg {{ 
            fill: #121010; 
            rx: 10px; 
            stroke: #2a221f; 
            stroke-width: 1px; 
        }}
        .name {{ 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 26px; 
            font-weight: 400; 
            fill: #e08b68; 
            letter-spacing: 6px;
        }}
        .sub {{ 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 13px; 
            font-weight: 300; 
            fill: #a68c7c; 
            letter-spacing: 3px;
        }}
        .dot {{
            fill: #d8a054;
        }}
    </style>
    
    <rect width="100%" height="100%" class="bg"/>
    
    <!-- Minimal Peaceful Header Content -->
    <g transform="translate(0, -2)">
        <text x="50%" y="46%" dominant-baseline="middle" text-anchor="middle" class="name">LUCKY PUSHKARNA</text>
        <circle cx="50%" cy="58%" r="2" class="dot" />
        <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" class="sub">building stuff on the web</text>
    </g>
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Peaceful aesthetic header saved to {output_svg}")

if __name__ == "__main__":
    generate_peaceful_header()
