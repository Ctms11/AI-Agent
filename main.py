import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("RuntimeError: Key was not found")
client = genai.Client(api_key=api_key)



def main():
    parser = argparse.ArgumentParser(description="Chat Bot takes prompt from user")
    parser.add_argument("user_prompt", type=str, help="Type in a prompt please")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    #my_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."   
    response = client.models.generate_content(
    model = 'gemini-2.5-flash', 
    contents = messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

    if not response.function_calls:

        if response.usage_metadata is None:
            raise RuntimeError("RuntimeError: Usage metadata was not found")
        elif args.verbose is True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print("Response: ")
            print(response.text)
        else:
            print("Response: ")
            print(response.text)       
    elif response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")

if __name__ == "__main__":
    main()
