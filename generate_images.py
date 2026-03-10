import os
from prompt_builder import build_prompt
from image_generator import generate_image


def main() -> None:
    with open("blog_titles.txt", "r", encoding="utf-8") as f:
        titles = [line.strip() for line in f if line.strip()]

    os.makedirs("results", exist_ok=True)

    for i, title in enumerate(titles, start=1):
        print(f"Generating image {i}/{len(titles)}: {title}")
        prompt = build_prompt(title)
        filename = os.path.join("results", f"header_{i}.png")
        generate_image(prompt, filename)
        print(f"Saved: {filename}")

    print("All images generated successfully.")


if __name__ == "__main__":
    main()