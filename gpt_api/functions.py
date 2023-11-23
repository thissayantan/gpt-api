import json
import os
from gpt_api import prompt


def create_assistant(client):
    assistant_file_path = "assistant.json"

    if os.path.exists(assistant_file_path):
        with open(assistant_file_path, "r") as file:
            assistant_data = json.load(file)
            assistant_id = assistant_data["assistant_id"]
            print("Loaded existing assistant ID.")
    else:
        file = client.files.create(
            file=open("./knowledgebase/data.md", "rb"), purpose="assistants"
        )

        assistant = client.beta.assistants.create(
            instructions=prompt.instructions,
            model="gpt-4-1106-preview",
            tools=[{"type": "retrieval"}],
            file_ids=[file.id],
        )

        with open(assistant_file_path, "w") as file:
            json.dump({"assistant_id": assistant.id}, file)
            print("Created a new assistant and saved the ID.")

        assistant_id = assistant.id

    return assistant_id
