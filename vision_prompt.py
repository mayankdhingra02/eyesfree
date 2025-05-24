import openai
import os
import base64
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_image_to_gpt(image_path, prompt_text):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{base64_image}" }}
                ],
            }
        ],
        max_tokens=500
    )

    return response["choices"][0]["message"]["content"]
