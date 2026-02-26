import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_Key")
client = genai.Client(api_key=api_key)

if api_key is None:
    raise Exception("RuntimeError")
def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
