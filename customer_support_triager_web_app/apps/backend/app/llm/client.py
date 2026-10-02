import json

from openai import OpenAI

from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
from app.llm.prompts import build_response_prompt

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


def _require_client():
    if client is None:
        raise RuntimeError("OPENAI_API_KEY is not configured.")


def analyze_ticket(complaint, domain):
    _require_client()

    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions=(
            "You are a customer support triage system. "
            "Use only the supplied departments and intents. "
            "Do not invent categories."
        ),
        input=json.dumps({
            "domain": domain["name"],
            "departments": domain["departments"],
            "intents": domain["intents"],
            "complaint": complaint,
        }),
        text={
            "format": {
                "type": "json_schema",
                "name": "ticket_analysis",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "enum": domain["departments"],
                        },
                        "intent": {
                            "type": "string",
                            "enum": domain["intents"],
                        },
                        "urgency": {
                            "type": "string",
                            "enum": [
                                "Critical", "High", "Medium", "Low"
                            ],
                        },
                        "sentiment": {
                            "type": "string",
                            "enum": ["Positive", "Negative"],
                        },
                    },
                    "required": [
                        "department",
                        "intent",
                        "urgency",
                        "sentiment",
                    ],
                    "additionalProperties": False,
                },
            }
        },
    )

    return json.loads(response.output_text)


def generate_response(
    complaint,
    department,
    intent,
    urgency,
    domain,
):
    _require_client()

    prompt = build_response_prompt(
        complaint,
        department,
        intent,
        urgency,
        domain,
    )

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text
