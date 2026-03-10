import json


def build_prompt(title: str) -> str:
    with open("style_config.json", "r", encoding="utf-8") as f:
        style = json.load(f)

    prompt = f"""
Create a cohesive website header illustration for a women's digital health brand.

Blog title: {title}

Visual style: {style["style"]}
Color palette: {style["color_palette"]}
Art direction: {style["visual_style"]}
Lighting: {style["lighting"]}
Mood: {style["mood"]}
Composition: {style["composition"]}

Requirements:
- Keep the visual identity consistent with all other generated images
- Create a clean and professional healthcare-oriented illustration
- Avoid text in the image
- Make it suitable as a blog header
- Make it feel warm, trustworthy, modern, and medically credible
"""

    return prompt.strip()