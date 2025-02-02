# app/routes.py
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from app.models import MessageDocument, MessageCreate
from datetime import datetime, UTC

router = APIRouter()

# ✅ Send a message
@router.post("/message", response_model=MessageDocument)
async def send_message(message: MessageCreate):
    new_message = MessageDocument(
        sender=message.sender,
        content=message.content,
        timestamp=datetime.now(tz=UTC),
    )
    await new_message.insert()
    return new_message

# ✅ Get all messages
@router.get("/message", response_model=list[MessageDocument])
async def get_messages():
    return await MessageDocument.find_all().to_list()

# ✅ Get a message by ID with error handling
@router.get("/message/{message_id}", response_model=MessageDocument)
async def get_message(message_id: PydanticObjectId):
    message = await MessageDocument.find_one(MessageDocument.id == message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message
