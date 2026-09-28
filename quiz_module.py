from gemini_client import generate_json


def generate_quiz(source: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the educational content below.

Each question must contain exactly 4 options.

Return ONLY valid JSON.

Use exactly this structure:
[
  {{
    "question": "Question text",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "A",
    "explanation": "Short explanation"
  }}
]

Rules:
- Exactly 3 questions.
- Exactly 4 options for every question.
- answer must be A, B, C, or D.
- Questions must be related to the input.
- Options should be plausible.
- Do not add Markdown.
- Do not add extra text outside JSON.

Educational Content:
{source}
"""

    try:
        data = generate_json(prompt)

        if not isinstance(data, list):
            raise ValueError("Quiz response must be a list.")

        if len(data) != 3:
            raise ValueError("Quiz must contain exactly 3 questions.")

        for question in data:
            required_fields = [
                "question",
                "options",
                "answer",
                "explanation"
            ]

            for field in required_fields:
                if field not in question:
                    raise ValueError(f"Missing field: {field}")

            if len(question["options"]) != 4:
                raise ValueError(
                    "Every question must contain 4 options."
                )

            if question["answer"] not in ["A", "B", "C", "D"]:
                raise ValueError(
                    "Answer must be A, B, C, or D."
                )

        return data

    except Exception as error:
        return {"error": str(error)}