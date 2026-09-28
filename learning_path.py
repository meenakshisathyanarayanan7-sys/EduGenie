from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the following topic.

Assume the learner is a beginner.

Organize the response into:
1. Beginner Foundations
2. Intermediate Concepts
3. Advanced Concepts
4. Suggested Timeline
5. Practice Activities
6. Learning Resources

For resources, suggest useful types such as:
- Official documentation
- Books
- Educational videos
- Practice websites

Give step-by-step guidance.

Topic:
{topic}
"""

    try:
        return generate_text(prompt)

    except Exception as error:
        return "Unable to create the learning path right now.\n\n" f"Error: {error}"