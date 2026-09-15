import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if isinstance(api_key, str):
    print("API Key loaded successfully.")
else:
    raise TypeError(
        "API Key not found. Please set the OPENROUTER_API_KEY environment variable."
    )

parser = argparse.ArgumentParser(description="AI Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt to AI")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages: list[ChatCompletionMessageParam] = [
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

if response.usage != None:
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Model: {response.model}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print(f"Response:\n{response.choices[0].message.content}")
    else:
        print(f"Response:\n{response.choices[0].message.content}")
else:
    raise RuntimeError("API call failed.")
