from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage.

Requirements:
- Keep the important information.
- Keep important definitions.
- Keep important steps.
- Remove unnecessary repetition.
- Use simple language.
- Format the result using bullet points.
- Do not add information that is not present in the original passage.

Educational Passage:
{text}
"""

    try:
        return generate_text(prompt)

    except Exception as error:
        return "Unable to summarize the text right now.\n\n" f"Error: {error}"