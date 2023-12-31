import os
from openai import OpenAI
from typing import Union
from fastapi import FastAPI, HTTPException
from time import sleep
from dotenv import load_dotenv

# Import functions
from gpt_api import types, functions

# Initialize FastAPI
app = FastAPI()

# Load environment variables
load_dotenv()

# Initialize OpenAI client
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
if OPENAI_API_KEY is None:
    raise HTTPException("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=OPENAI_API_KEY)

# Create or load assistant
assistant_id = functions.create_assistant(
    client
)  # this function comes from 'functions.py'


# Root route
@app.get("/")
async def read_root():
    return {"message": "🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀"}


# Start conversation thread
@app.get("/start")
async def start_conversation():
    print("Starting a new conversation...")  # Debugging line
    thread = client.beta.threads.create()
    print(f"New thread created with ID: {thread.id}")  # Debugging line
    return {"thread_id": thread.id}


# Generate response
@app.post("/chat")
async def chat(dialogueSnippet: types.DialogueSnippet):
    dialogue = dialogueSnippet.dict()
    thread_id = dialogue.get("thread_id")
    user_input = dialogue.get("message", "")

    if not thread_id:
        print("Error: Missing thread_id")  # Debugging line
        return {"error": "Missing thread_id"}, 400

    print(
        f"Received message: {user_input} for thread ID: {thread_id}"
    )  # Debugging line

    # Add the user's message to the thread
    client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=user_input
    )

    # Run the Assistant
    run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )

    # Check if the Run requires action (function call)
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id, run_id=run.id
        )
        print(f"Run status: {run_status.status}")
        if run_status.status == "completed":
            break
        sleep(1)  # Wait for a second before checking again

    # Retrieve and return the latest message from the assistant
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value

    print(f"Assistant response: {response}")  # Debugging line
    return {"response": response}
