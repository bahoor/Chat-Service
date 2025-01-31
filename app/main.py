from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.routes import router
from app.models import MessageDocument 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient("mongodb://localhost:27017") 
    await init_beanie(database=client["chat_db"], document_models=[MessageDocument])

app.include_router(router)

