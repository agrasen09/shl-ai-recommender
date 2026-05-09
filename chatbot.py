import os
from dotenv import load_dotenv
import google.generativeai as genai

from retriever import search_assessments

# Load environment variables
load_dotenv()
print("API KEY:", os.getenv("GEMINI_API_KEY"))

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def chatbot_response(messages):

    latest_message = messages[-1]["content"]

    latest_lower = latest_message.lower()

    # =========================
    # OFF TOPIC PROTECTION
    # =========================

    off_topic = [
        "weather",
        "cricket",
        "football",
        "movie",
        "bitcoin",
        "politics"
    ]

    for word in off_topic:

        if word in latest_lower:

            return {
                "reply": "I can only help with SHL assessments and hiring evaluation recommendations.",
                "recommendations": [],
                "end_of_conversation": False
            }

    # =========================
    # VAGUE QUERY
    # =========================

    if len(latest_lower.split()) < 4:

        return {
            "reply": (
                "Could you provide more details about the role, required skills, experience level, or assessment type?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # =========================
    # RETRIEVE ASSESSMENTS
    # =========================

    results = search_assessments(latest_message)

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item.get("category", "Assessment")
        })

    # =========================
    # CREATE LLM PROMPT
    # =========================

    assessment_names = "\n".join(
        [f"- {item['name']}" for item in recommendations]
    )

    prompt = f"""
    You are an SHL assessment recommendation assistant.

    User hiring requirement:
    {latest_message}

    Recommended SHL assessments:
    {assessment_names}

    Write a professional conversational response explaining why these assessments are suitable.

    Keep response concise and professional.
    """

    # Generate Gemini response
    response = model.generate_content(prompt)

    reply = response.text

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": True
    }