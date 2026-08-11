import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Load environment variables from the .env file
load_dotenv()
DEFAULT_MODEL="openai/gpt-oss-20b:free"
# Initialize the OpenAI client
# It will automatically look for the OPENAI_API_KEY in the environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file or environment variables.")
    sys.exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def chat_cli():
    print("🤖 LLM Streaming CLI App (Type 'exit' or 'quit' to stop)")
    print("-" * 50)
    
    # Store conversation history to maintain context
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    while True:
        try:
            # Get user prompt
            user_prompt = input("\nYou: ")
            
            # Exit conditions
            if user_prompt.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            if not user_prompt.strip():
                continue

            # Add user message to history
            messages.append({"role": "user", "content": user_prompt})
            
            print("AI: ", end="", flush=True)

            # Call the OpenAI API with streaming enabled
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", # You can change this to gpt-4o or gpt-4-turbo
                messages=messages,
                temperature=0.7,
                stream=True
            )

            # Process and print the stream chunks
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    chunk_text = chunk.choices[0].delta.content
                    print(chunk_text, end="", flush=True)
                    full_response += chunk_text
            
            print() # Print a newline when the stream finishes
            
            # Add the assistant's full response back to the message history
            messages.append({"role": "assistant", "content": full_response})

        except OpenAIError as e:
            print(f"\n[OpenAI API Error]: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\n[Unexpected Error]: {e}")

if __name__ == "__main__":
    chat_cli()
