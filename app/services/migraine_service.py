# app/services/migraine_service.py

from typing import List, Optional
from bson import ObjectId
from app.models.migraine_model import MigraineCreate, MigraineUpdate, MigraineDisplay
from app.db.mongodb_utils import get_database

class MigraineService:

    @staticmethod
    async def create_migraine(user_id: str, migraine_data: MigraineCreate) -> MigraineDisplay:
        db = get_database()
        migraine_dict = migraine_data.dict()
        migraine_dict["user_id"] = user_id  # Add user reference
        new_migraine = await db["migraines"].insert_one(migraine_dict)
        created_migraine = await db["migraines"].find_one({"_id": new_migraine.inserted_id})
        return MigraineDisplay(**created_migraine)

    @staticmethod
    async def get_migraine(user_id: str, migraine_id: str) -> Optional[MigraineDisplay]:
        db = get_database()
        migraine = await db["migraines"].find_one({"_id": ObjectId(migraine_id), "user_id": user_id})
        return MigraineDisplay(**migraine) if migraine else None

    @staticmethod
    async def get_all_migraines(user_id: str) -> List[MigraineDisplay]:
        db = get_database()
        migraines = await db["migraines"].find({"user_id": user_id}).to_list(None)
        return [MigraineDisplay(**migraine) for migraine in migraines]

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