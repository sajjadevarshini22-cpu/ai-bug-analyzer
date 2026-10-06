import os
import json

from dotenv import load_dotenv
from google import genai

from prompt import create_bug_analysis_prompt


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_bug(bug_report):

    if not bug_report.strip():
        raise ValueError("Bug report cannot be empty.")

    prompt = create_bug_analysis_prompt(bug_report)

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        if not response.text:
            raise ValueError(
                "AI returned an empty response."
            )

        try:

            return json.loads(response.text)

        except json.JSONDecodeError:

            raise ValueError(
                "AI returned an invalid JSON response."
            )

    except Exception as error:

        raise RuntimeError(
            f"Unable to analyze bug: {error}"
        )