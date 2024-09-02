# app/services/migraine_service.py

from typing import List, Optional
from bson import ObjectId
from app.schemas.migraine_schema import MigraineCreate, MigraineUpdate, MigraineDisplay, Migraine
from app.db.mongodb_utils import get_database

class MigraineService:

    @staticmethod
    async def create_migraine(user_id: str, migraine_data: MigraineCreate) -> MigraineDisplay:
        created = await Migraine.insert_record(new_migraine=migraine_data,user_id=ObjectId(user_id))
        return MigraineDisplay(**created.model_dump())

    @staticmethod
    async def get_migraine(user_id: str, migraine_id: str) -> Optional[MigraineDisplay]:
        db = get_database()
        migraine = await db["migraines"].find_one({"_id": ObjectId(migraine_id), "user_id": user_id})
        return MigraineDisplay(**migraine) if migraine else None

    @staticmethod
    async def get_all_migraines(user_id: str) -> List[MigraineDisplay]:
        all_migraines = await Migraine.by_user(user_id=ObjectId(user_id))
        return all_migraines

    @staticmethod
    async def update_migraine(user_id: str, migraine_id: str, migraine_update: MigraineUpdate) -> Optional[MigraineDisplay]:
        db = get_database()
        update_result = await db["migraines"].update_one(
            {"_id": ObjectId(migraine_id), "user_id": user_id},
            {"$set": migraine_update.dict(exclude_unset=True)}
        )
        if update_result.modified_count:
            return await MigraineService.get_migraine(user_id, migraine_id)
        return None

    @staticmethod
    async def delete_migraine(user_id: str, migraine_id: str) -> bool:
        db = get_database()
        delete_result = await db["migraines"].delete_one({"_id": ObjectId(migraine_id), "user_id": user_id})
        return delete_result.deleted_count > 0