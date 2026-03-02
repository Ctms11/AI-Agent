import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("RuntimeError: Key was not found")
client = genai.Client(api_key=api_key)



def main():
    parser = argparse.ArgumentParser(description="Chat Bot takes prompt from user")
    parser.add_argument("user_prompt", type=str, help="Type in a prompt please")
    args = parser.parse_args()

    #my_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."   
    response = client.models.generate_content(
    model = 'gemini-2.5-flash', 
    contents = args.user_prompt
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
