from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.
Answer the student's question accurately and clearly.

Requirements:
- Use simple language.
- Explain the answer clearly.
- Use examples when useful.
- Avoid unnecessary complicated words.
- If the question is ambiguous, mention the assumption.

Student Question:
{question}
"""

    try:
        return generate_text(prompt)
    except Exception as error:
        return "Unable to answer the question right now.\n\n" f"Error: {error}"