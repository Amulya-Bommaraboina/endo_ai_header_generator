import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# Good default text-to-image model from Hugging Face docs
MODEL_NAME = "black-forest-labs/FLUX.1-schnell"


def generate_image(prompt: str, filename: str) -> None:
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN is missing. Add it to your .env file.")

    client = InferenceClient(api_key=HF_TOKEN)

    try:
        image = client.text_to_image(
            prompt=prompt,
            model=MODEL_NAME,
        )
        image.save(filename)
    except Exception as e:
        raise RuntimeError(f"Image generation failed: {e}") from e