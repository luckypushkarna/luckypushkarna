from PIL import Image
import numpy as np

GLYPHS = " '.,:;~+*xXO#"  # Light to dark ramp

def generate_ascii_svg(image_path="assets/photo-ready.png", output_svg="portrait.svg", cols=70):
    img = Image.open(image_path).convert('L')
    
    # Maintain character aspect ratio (~1:2 character dimension ratio)
    w, h = img.size
    aspect_ratio = h / w
    rows = int(cols * aspect_ratio * 0.48)
    
    img = img.resize((cols, rows), Image.Resampling.LANCZOS)
    pixels = np.array(img)
    
    # Map pixel values (0-255) to character indices
    glyph_indices = (pixels / 256.0 * len(GLYPHS)).astype(int)
    
    cell_w, cell_h = 8, 14
    svg_w, svg_h = cols * cell_w + 20, rows * cell_h + 20
    
    css_rules = []
    text_rows = []
    
    for r in range(rows):
        row_str = "".join([GLYPHS[glyph_indices[r, c]] for c in range(cols)])
        # Escape XML entities
        row_str = row_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&#160;")
        
        delay = r * 0.04  # 40ms stagger per row
        css_rules.append(f"""
        .row-{r} {{
            animation: revealRow 0.1s ease-out {delay:.2f}s forwards;
            opacity: 0;
        }}""")
        
        y_pos = 20 + (r * cell_h)
        text_rows.append(f'<text x="10" y="{y_pos}" class="row-{r}">{row_str}</text>')
        
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
    <style>
        text {{
            font-family: 'Courier New', Courier, monospace;
            font-size: 12px;
            font-weight: bold;
            fill: #39d353;
            white-space: pre;
        }}
        @keyframes revealRow {{
            from {{ opacity: 0; transform: translateY(-2px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        {''.join(css_rules)}
    </style>
    <rect width="100%" height="100%" fill="#0d1117" rx="6"/>
    {''.join(text_rows)}
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ ASCII Portrait saved to {output_svg}")

if __name__ == "__main__":
    generate_ascii_svg()
