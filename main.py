import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("RuntimeError: Key was not found")
client = genai.Client(api_key=api_key)



def main():
    parser = argparse.ArgumentParser(description="Chat Bot takes prompt from user")
    parser.add_argument("user_prompt", type=str, help="Type in a prompt please")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    #my_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."   
    response = client.models.generate_content(
    model = 'gemini-2.5-flash', 
    contents = messages
    )

    
    if response.usage_metadata is None:
        raise RuntimeError("RuntimeError: Usage metadata was not found")
    else:
        print(f"User prompt: {args}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("Response: ")
        print(response.text)

if __name__ == "__main__":
    main()
