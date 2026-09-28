from config import USE_LOCAL_EXPLAINER, LOCAL_MODEL_NAME
from gemini_client import generate_text

_local_pipeline = None


def local_explanation(topic: str) -> str:
    global _local_pipeline

    try:
        from transformers import pipeline

        if _local_pipeline is None:
            _local_pipeline = pipeline(
                "text2text-generation",
                model=LOCAL_MODEL_NAME
            )

        prompt = (
            "Explain the following educational topic to a beginner "
            "using simple language and one example: " + topic
        )

        result = _local_pipeline(
            prompt,
            max_new_tokens=220,
            do_sample=False
        )

        return result[0]["generated_text"].strip()

    except Exception:
        return ""


def explain_concept(topic: str) -> str:
    if USE_LOCAL_EXPLAINER:
        result = local_explanation(topic)

        if result:
            return result

    prompt = f"""
Explain the following topic to a beginner.

Use this structure:
1. Meaning
2. Main points
3. Simple example
4. One-line recap

Use very simple educational language.

Topic:
{topic}
"""

    try:
        return generate_text(prompt)

    except Exception as error:
        return "Unable to explain the topic right now.\n\n" f"Error: {error}"