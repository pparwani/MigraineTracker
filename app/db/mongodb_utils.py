# app/db/mongodb_utils.py
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, Indexed, init_beanie
from app.schemas.user import User

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls, uri: str, dbname: str):
        cls.client = AsyncIOMotorClient(uri)
        cls.db = cls.client[dbname]
        await init_beanie(database=cls.client[dbname], document_models=[User])

    @classmethod
    async def close(cls):
        if cls.client:
            cls.client.close()

# Dependency injection to use the database
def get_database():
    return MongoDB.db