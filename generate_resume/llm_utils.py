import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

# Get raw key from .env
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("❌ API key not found in .env file!")

# ✅ DO NOT add "Bearer " prefix manually — DashScope doesn't want it
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # ✅ correct
)

def polish_experience_bullet(bullet, role=None, skills=None):
    prompt = f"Improve this resume bullet point to make it more impactful and specific:\nBullet: \"{bullet}\""
    if role:
        prompt += f"\nTarget role: {role}"
    if skills:
        prompt += f"\nRelevant skills: {', '.join(skills)}"

    try:
        response = client.chat.completions.create(
            model="qwen-plus",  # or "qwen-vl-max-latest" if using vision
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error communicating with Qwen:", str(e))
        return bullet
