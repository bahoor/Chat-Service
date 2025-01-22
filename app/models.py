# app/models.py
from beanie import Document
from typing import Optional
from datetime import datetime


class MessageDocument(Document):
    sender: str
    content: str
    timestamp: datetime
    class Settings:
        collection = "messages"