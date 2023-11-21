import os
from openai import OpenAI
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

# Initialize FastAPI
app = FastAPI()

# Load environment variables
load_dotenv()

# Initialize OpenAI client
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
if OPENAI_API_KEY is None:
    raise Exception("OPENAI_API_KEY environment variable is not set")
  
client = OpenAI(api_key=OPENAI_API_KEY)

# Create or load assistant
# assistant_id = functions.create_assistant(client)  # this function comes from "functions.py"


@app.get("/")
async def read_root():
    return {"message": "🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀"}


