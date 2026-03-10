# Workflow Overview

This project automatically generates blog header illustrations from a list of blog titles using a structured AI workflow.

## Workflow Steps

1. Blog titles are loaded from a text file.
2. A reusable prompt template combines each title with a shared visual style configuration.
3. The prompt is sent to an image generation model through an API-based workflow.
4. Images are generated and saved locally in the results directory.
5. A shared style configuration ensures that all outputs maintain a cohesive visual identity across the full set of blog headers.

## Design Approach

The workflow is designed to avoid random or inconsistent outputs by using:

- a structured prompt template
- a fixed visual style configuration
- automated batch processing for multiple blog titles

This makes the solution reproducible and easy to adapt for content pipelines, internal tooling, or CMS-based workflows.

## Technical Notes

The implementation is designed to work end-to-end with a valid image generation API key.

During development, I initially planned to use the OpenAI image generation API. Due to billing restrictions on that provider during packaging, I adapted the implementation to use Hugging Face inference with token-based authentication instead.

This demonstrates a flexible, provider-agnostic approach to AI tooling, where the workflow can be adjusted to different model providers while keeping the same core automation and prompt-engineering logic.