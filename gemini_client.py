import json

from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_OUTPUT_TOKENS


_client = None


def get_client():
    global _client

    if _client is not None:
        return _client

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Please add your Gemini API key to the .env file."
        )

    try:
        from google import genai

        _client = genai.Client(api_key=GEMINI_API_KEY)
        return _client

    except ImportError:
        raise RuntimeError(
            "google-genai package is not installed. Run: pip install -r requirements.txt"
        )


def generate_text(prompt: str) -> str:
    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "temperature": 0.3,
            "max_output_tokens": MAX_OUTPUT_TOKENS
        }
    )

    text = getattr(response, "text", None)

    if not text:
        raise RuntimeError("Gemini returned an empty response.")

    return text.strip()


def clean_json_block(text: str) -> str:
    text = text.strip()

    if text.startswith("```"):
        lines = text.splitlines()

        if lines:
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        text = "\n".join(lines)

    return text.strip()


def generate_json(prompt: str):
    raw_response = generate_text(prompt)
    cleaned_response = clean_json_block(raw_response)

    try:
        return json.loads(cleaned_response)

    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"Gemini returned invalid JSON: {error}"
        )