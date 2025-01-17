# app/routes.py
from fastapi import APIRouter
from app.models import MessageDocument
from datetime import datetime

router = APIRouter()

# Example endpoint to send a message
@router.post("/send-message/")
async def send_message(message: MessageDocument):
    # Here, you would typically save the message to a database
    # But for now, we're simply returning it as confirmation
    return {"message": message}
