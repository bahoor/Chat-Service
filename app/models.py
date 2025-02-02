# app/models.py
from pydantic import BaseModel
from beanie import Document
from datetime import datetime, UTC
from pydantic import Field

class MessageCreate(BaseModel):
    sender: str
    content: str

def utcnow():
    return datetime.now(tz=UTC)
class MessageDocument(Document):
    sender: str
    content: str
    timestamp: datetime = Field(default_factory=utcnow)

    class Settings:
        name = "messages"