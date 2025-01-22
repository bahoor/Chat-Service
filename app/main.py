from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.routes import router
from app.models import MessageDocument  # مدل MessageDocument از Beanie

app = FastAPI()

# مقداردهی اولیه دیتابیس در زمان شروع برنامه
@app.on_event("startup")
async def startup_event():
    # اتصال به دیتابیس MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")  # آدرس MongoDB
    # مقداردهی Beanie و تنظیم مدل‌های دیتابیس
    await init_beanie(database=client["chat_db"], document_models=[MessageDocument])

# اضافه کردن روت‌ها
app.include_router(router)
