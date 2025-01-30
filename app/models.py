# app/models.py
from beanie import Document
from datetime import datetime, UTC
from pydantic import Field
def utcnow():
    return datetime.now(tz=UTC)
class MessageDocument(Document):
    sender: str
    content: str
    timestamp: datetime = Field(default_factory=utcnow)

    class Settings:
        name = "messages"