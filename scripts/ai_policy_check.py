import openai
import os
import sys

# Azure OpenAI setup
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

def review_policy(policy_text):
    system_prompt = """You are a security reviewer for CyberArk Conjur policies.

Mark the policy as ❌ Risky only if:
- It includes `update`, `execute`, or `all` in the privileges
- AND there is no comment or annotation justifying why these are needed

Otherwise, mark it as ✅ Safe.
Explain your reasoning clearly and end with a verdict line: '❌ Risky' or '✅ Safe'."""

    response = openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": policy_text}
        ]
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ai_policy_check.py <policy_file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        content = f.read()

    result = review_policy(content)
    print("\n🔍 AI Review Result:\n")
    print(result)

    if "❌ Risky" in result:
        sys.exit(1)
    else:
        sys.exit(0)
