import os
import logging
from google import genai
from src.config import get_settings
from src.server import send_email

settings = get_settings()
logging.basicConfig(level=logging.INFO)

# Initialize the official Google GenAI client
client = genai.Client(api_key=settings.gemini_api_key)

def run_agent(prompt: str):
    """An autonomous agent loop using Gemini and local function calling."""
    print(f"\n[User Prompt]: {prompt}")
    
    #  pass  Python function 'send_email'  to Gemini as a tool
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config={
            'tools': [send_email],
            'system_instruction': "You are an AI assistant with access to a secure email tool. Use it when asked to send messages."
        }
    )

    # Check if Gemini decided to invoke our tool
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"[Agent Action]: Calling tool '{function_call.name}' with args {function_call.args}")
            
            if function_call.name == "send_email":
                # Execute our local python function
                result = send_email(
                    recipient=function_call.args["recipient"],
                    message=function_call.args["message"]
                )
                print(f"[Tool Response]: {result}")
    else:
        print(f"[Agent Response]: {response.text}")

if __name__ == "__main__":
    # Test execution: Instruct the agent to send an email using natural language
    run_agent("Send an email to test@example.com saying 'Hello from my local Gemini agent!'")