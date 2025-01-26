# app/routes.py
from beanie import PydanticObjectId
from fastapi import APIRouter
from app.models import MessageDocument
from datetime import datetime,UTC

router = APIRouter()

# Example endpoint to send a message
@router.post("/message",response_model=MessageDocument)
async def send_message(message: MessageDocument):
    message.timestamp = datetime.now(tz=UTC)
    await message.insert()
    return message

# Endpoint to get all messages
@router.get("/message",response_model=list[MessageDocument])
async def get_messages():
    return await MessageDocument.find_all().to_list()

    
@router.get("/message/{message_id}",response_model=MessageDocument)
async def get_message(message_id:PydanticObjectId):
    return await MessageDocument.find_one(MessageDocument.id==message_id)