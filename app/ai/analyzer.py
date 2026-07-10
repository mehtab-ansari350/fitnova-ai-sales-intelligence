import json

from app.ai.llm import ask_gemini
from app.ai.prompts import SALES_ANALYSIS_PROMPT


def analyze_sales_call(transcript: str):
    """
    Analyze transcript using Gemini.
    """

    prompt = SALES_ANALYSIS_PROMPT.replace(
        "<<TRANSCRIPT>>",
        transcript
    )

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        print("Gemini returned invalid JSON:")
        print(response)
        raise