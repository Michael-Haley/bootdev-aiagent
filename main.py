import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if isinstance(api_key, str):
    print("API Key loaded successfully.")
else:
    raise TypeError("API Key not found. Please set the"
    " OPENROUTER_API_KEY environment variable.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

prompt: str = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

completion = client.chat.completions.create(
    model="openrouter/free",
    messages=[
         {
        "role": "user",
        "content": prompt,
        }
    ]
)

if completion.usage != None:
    print(f"User prompt: {prompt}")
    print(f"Model: {completion.model}")
    print(f"Prompt tokens: {completion.usage.prompt_tokens}")
    print(f"Response tokens: {completion.usage.completion_tokens}")
    print(f"Response:\n{completion.choices[0].message.content}")
else:
    raise RuntimeError("API call failed.")


