# tools/render_header.py
import base64

def generate_fixed_header(image_path="44457912_9023633.jpg", output_svg="header.svg"):
    try:
        with open(image_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
        img_data_uri = f"data:image/jpeg;base64,{encoded_string}"
        bg_element = f'<image href="{img_data_uri}" width="1000" height="250" preserveAspectRatio="xMidYMid slice" />'
    except:
        bg_element = '<rect width="100%" height="100%" fill="#2b26c3"/>'

    title_text = "Lucky Pushkarna"
    subtitle_text = "Full-Stack Python Developer &amp; AI-Assisted Engineer"

    # Typewriter timing
    title_chars = len(title_text)
    subtitle_chars = len(subtitle_text)
    title_duration = title_chars * 0.08  # seconds
    subtitle_delay = title_duration + 0.3
    subtitle_duration = subtitle_chars * 0.03

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 250" width="100%" height="250">
    <defs>
        <clipPath id="title-clip">
            <rect x="150" y="70" width="0" height="60">
                <animate attributeName="width" from="0" to="700" begin="0.2s" dur="{title_duration}s" fill="freeze" calcMode="linear" />
            </rect>
        </clipPath>
        <clipPath id="subtitle-clip">
            <rect x="150" y="130" width="0" height="50">
                <animate attributeName="width" from="0" to="700" begin="{subtitle_delay}s" dur="{subtitle_duration}s" fill="freeze" calcMode="linear" />
            </rect>
        </clipPath>
    </defs>
    <style>
        .title {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Inter', Roboto, Helvetica, Arial, sans-serif;
            font-size: 38px;
            font-weight: 600;
            fill: #ffffff;
            letter-spacing: 1.5px;
        }}
        .subtitle {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Inter', Roboto, Helvetica, Arial, sans-serif;
            font-size: 15px;
            font-weight: 300;
            fill: #d0d7ff;
            letter-spacing: 0.8px;
        }}
        .glass-box {{
            fill: rgba(15, 15, 35, 0.45);
            stroke: rgba(255, 255, 255, 0.15);
            stroke-width: 1px;
        }}
        .caret {{
            fill: #ffffff;
            opacity: 0;
        }}
        .caret-title {{
            animation: blink 0.8s step-end infinite, showCaret 0.1s {title_duration + 0.2}s forwards, hideCaret 0.1s {subtitle_delay}s forwards;
        }}
        .caret-sub {{
            animation: blink 0.8s step-end infinite, showCaret 0.1s {subtitle_delay}s forwards;
        }}
        @keyframes blink {{
            50% {{ opacity: 0; }}
        }}
        @keyframes showCaret {{
            to {{ opacity: 1; }}
        }}
        @keyframes hideCaret {{
            to {{ opacity: 0; }}
        }}
    </style>

    <!-- Background -->
    {bg_element}

    <!-- Glass Container -->
    <rect x="150" y="70" width="700" height="110" rx="14" ry="14" class="glass-box" />

    <!-- Title with typewriter reveal -->
    <g clip-path="url(#title-clip)">
        <text x="500" y="115" dominant-baseline="middle" text-anchor="middle" class="title">{title_text}</text>
    </g>

    <!-- Subtitle with typewriter reveal -->
    <g clip-path="url(#subtitle-clip)">
        <text x="500" y="152" dominant-baseline="middle" text-anchor="middle" class="subtitle">{subtitle_text}</text>
    </g>
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Fixed header saved to {output_svg}")

if __name__ == "__main__":
    generate_fixed_header()
