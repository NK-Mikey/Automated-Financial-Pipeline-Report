# ================================
# AI Commentary Generator
# ================================

import anthropic # Anthropic SDK 
import os # Environment variable access

def generate_commentary(metrics: dict) -> str: 
    """Generate a plain prose portfolio summary using the Anthropic API."""

    # Authenticate using ANTHROPIC_API_KEY injected at runtime via GitHub Secrets
    client = anthropic.Anthropic(api_key = os.environ.get("ANTHROPIC_API_KEY"))

    # Structured prompt: persona + data + output constraints
    prompt = f"""You are a professional portfolio analyst writing a daily performance summary.
Here are today's portfolio metrics:

{metrics}

Write a three-sentence plain prose summary interpreting these numbers for a stakeholder.
Do not use markdown, bullet points, headers, or bold text.
Use percentage format where appropriate (e.g. 14.2% not 0.142).
Be specific about whether performance is strong, weak, or moderate and why."""

    # API reponse object
    response = client.messages.create(
        model = "claude-sonnet-4-6", # Model of API 
        max_tokens = 300, # ~225 words, sufficient for three sentences
        messages = [
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text # Extract text from first content block