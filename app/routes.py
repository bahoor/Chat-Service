# app/routes.py
from fastapi import APIRouter
from app.models import MessageDocument
from datetime import datetime

router = APIRouter()

# Example endpoint to send a message
@router.post("/send-message/")
async def send_message(message: MessageDocument):
    await message.insert()
    return {"message": message}

# Endpoint to get all messages
@router.get("/get-messages/")
async def get_messages():
    try:
        messages = await MessageDocument.find_all().to_list()
        print(f"Fetched messages: {messages}")
        return {"messages": messages}
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return {"error": "Failed to fetch messages"}
