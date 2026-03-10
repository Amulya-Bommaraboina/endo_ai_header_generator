import os
import tempfile
from dotenv import load_dotenv
import streamlit as st

from prompt_builder import build_prompt
from image_generator import generate_image

load_dotenv()

st.set_page_config(page_title="AI Blog Header Generator", layout="wide")

st.title("AI Blog Header Generator")
st.write(
    "Generate consistent blog header illustrations from blog titles using a shared style configuration."
)

default_titles = """Living With Endometriosis: What Every Woman Should Know
How Hormones Affect Mood During PMS
Recognizing Early Signs of Menopause"""

titles_input = st.text_area(
    "Enter blog titles, one per line",
    value=default_titles,
    height=150
)

generate_button = st.button("Generate Images")

if generate_button:
    titles = [line.strip() for line in titles_input.splitlines() if line.strip()]

    if not titles:
        st.warning("Please enter at least one blog title.")
    else:
        st.info("Generating images... This may take a little while.")
        cols = st.columns(2)

        for idx, title in enumerate(titles, start=1):
            prompt = build_prompt(title)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                output_path = tmp_file.name

            try:
                generate_image(prompt, output_path)

                with cols[(idx - 1) % 2]:
                    st.subheader(f"{idx}. {title}")
                    st.image(output_path, use_container_width=True)

            except Exception as e:
                with cols[(idx - 1) % 2]:
                    st.subheader(f"{idx}. {title}")
                    st.error(f"Failed to generate image: {e}")