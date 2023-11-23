from pydantic import BaseModel

class DialogueSnippet(BaseModel):
    thread_id: str
    message: str | None = None