import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from tools import AGENT_TOOLS, execute_tool

load_dotenv()

# Point the standard OpenAI client to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# Set your free model
MODEL_NAME = "openai/gpt-oss-20b:free"

def run_agent(user_prompt: str):
    print(f"\nUser: {user_prompt}")
    
    messages = [
        {"role": "system", "content": "You are a helpful customer support agent. Use the provided tools to answer user queries."},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=AGENT_TOOLS,
        tool_choice="auto"
    )
    
    message = response.choices[0].message
    
    if message.tool_calls:
        messages.append(message)
        
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            tool_result = execute_tool(function_name, arguments)
            print(f"[SYSTEM] Observation: {tool_result}")
            
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": tool_result
            })
            
        final_response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )
        
        print(f"\nAgent: {final_response.choices[0].message.content}")
    else:
        print(f"\nAgent: {message.content}")

if __name__ == "__main__":
    run_agent("If I buy 14 items at $32.50 each, what is my total?")
    run_agent("Can you check the status of my order? The ID is ORD-123.")
