# AI Blog Header Image Generator

This project was created as part of the **Endo Health AI Solutions Engineer challenge**.

The goal of this project is to automatically generate **visually consistent blog header images** from a list of blog titles using Generative AI and API orchestration.

The system demonstrates how AI models, APIs, and automation workflows can be combined to create practical internal tools that help teams generate content faster and more efficiently.

---

# Overview

The script reads a list of blog titles and automatically generates matching header illustrations while maintaining a consistent visual identity.

The workflow ensures that all images:

- follow the same **visual style**
- use a consistent **color palette**
- match a **modern digital health aesthetic**
- are suitable for **website blog headers**

---

# Example Workflow

Blog Titles  
↓  
Prompt Builder  
↓  
Style Configuration  
↓  
Image Generation API  
↓  
Generated Images  

Each title is converted into a structured prompt that includes a fixed visual style template to maintain brand consistency.

---

# Key Features

### Prompt Engineering
Structured prompts ensure consistent design across all generated images.

### Style Consistency
A shared style configuration controls color palette, mood, and composition.

### Automation
The script generates images for multiple blog titles automatically.

### API Integration
Uses REST APIs to generate images from prompts.

### Reusable Workflow
Designed so it can easily integrate into internal content pipelines or CMS systems.

---

# Project Structure

endo_ai_header_generator/

blog_titles.txt  
generate_images.py  
image_generator.py  
prompt_builder.py  
style_config.json  
requirements.txt  
workflow_description.md  

results/  
header_1.png  
header_2.png  
header_3.png  
...

---

# Setup

Install dependencies:

pip install -r requirements.txt

Create a `.env` file in the project root:

OPENAI_API_KEY=your_api_key_here

Run the generator:

python generate_images.py

Generated images will appear in the **results/** directory.

---

# Design Considerations

To avoid producing random or inconsistent images, the system uses:

- a shared **style configuration**
- structured **prompt templates**
- consistent **composition instructions**

This ensures all generated images feel like part of the same visual system and match a unified brand identity.

---

# Possible Extensions

This tool could easily be extended to support:

- CMS integration for automated blog publishing
- internal design tooling for marketing teams
- batch content generation pipelines
- live preview via a small web interface (e.g., Streamlit)

---

# Technologies Used

Python  
REST APIs  
Prompt Engineering  
Generative AI  
JSON configuration  
Automation scripting  

---

# Author

Amulya Bommaraboina  
AI / Applied AI Engineer  
bommaraboinaamulya@gmail.com
Berlin, Germany
