# app/models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# A Pydantic model representing a message
class MessageDocument(BaseModel):
    sender: str
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True  # Updated key for Pydantic V2
