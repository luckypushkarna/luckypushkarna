# tools/render_header.py
import base64

def generate_fixed_header(image_path="44457912_9023633.jpg", output_svg="header.svg"):
    # Read the banner image and convert to Base64 (or use your blue SVG background directly)
    try:
        with open(image_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
        img_data_uri = f"data:image/jpeg;base64,{encoded_string}"
        bg_element = f'<image href="{img_data_uri}" width="1000" height="250" preserveAspectRatio="xMidYMid slice" />'
    except:
        # Fallback if image isn't local
        bg_element = '<rect width="100%" height="100%" fill="#2b26c3"/>'

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 250" width="100%" height="250">
    <style>
        .title {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            font-size: 32px; 
            font-weight: 700; 
            fill: #ffffff; 
            letter-spacing: 3px;
            text-transform: uppercase;
        }}
        .subtitle {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            font-size: 14px; 
            font-weight: 400; 
            fill: #d0d7ff; 
            letter-spacing: 1px;
            font-style: italic;
        }}
        .glass-box {{
            fill: rgba(15, 15, 35, 0.45);
            rx: 12px;
            stroke: rgba(255, 255, 255, 0.15);
            stroke-width: 1px;
        }}
    </style>

    <!-- Background -->
    {bg_element}

    <!-- Properly proportioned Glass Container -->
    <rect x="150" y="70" width="700" height="110" class="glass-box" />

    <!-- Centered & Fitted Content -->
    <g>
        <text x="500" y="118" dominant-baseline="middle" text-anchor="middle" class="title">LUCKY PUSHKARNA</text>
        <text x="500" y="150" dominant-baseline="middle" text-anchor="middle" class="subtitle">Full-Stack Python Developer &amp; AI-Assisted Engineer</text>
    </g>
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Fixed header saved to {output_svg}")

if __name__ == "__main__":
    generate_fixed_header()
