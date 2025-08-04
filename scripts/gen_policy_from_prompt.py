import openai
import os

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

prompt = os.environ.get("POLICY_PROMPT", "Create a host identity for app1 with read access to DB")

system_message = """You are a CyberArk Conjur policy generator.
Given a plain English description, generate a valid Conjur YAML policy.
Use constructs like: !host, !user, !group, !variable, !permit.
Be concise and correct.
"""

response = openai.ChatCompletion.create(
    engine=DEPLOYMENT_NAME,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
)

policy_yaml = response['choices'][0]['message']['content']

# Output to file
output_path = "generated/generated_policy.yml"
os.makedirs("generated", exist_ok=True)
with open(output_path, "w") as f:
    f.write(policy_yaml)

print(f"✅ Generated policy saved to {output_path}")
print(policy_yaml)
