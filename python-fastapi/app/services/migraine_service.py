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
        migraine = await Migraine.by_id(migraine_id=migraine_id, user_id=user_id)
        return migraine

    @staticmethod
    async def get_all_migraines(user_id: str) -> List[MigraineDisplay]:
        all_migraines = await Migraine.by_user(user_id=user_id)
        return all_migraines

    @staticmethod
    async def update_migraine(user_id: str, migraine_id: str, migraine_update: MigraineUpdate) -> Optional[MigraineDisplay]:
        if not ObjectId.is_valid(user_id) or not ObjectId.is_valid(migraine_id):
            return None
        updated = await Migraine.update_record(migraine_update, user_id=user_id, migraine_id=migraine_id)
        return updated

    @staticmethod
    async def delete_migraine(user_id: str, migraine_id: str) -> Optional[bool]:
        if not ObjectId.is_valid(user_id) or not ObjectId.is_valid(migraine_id):
            return None
        deleted = await Migraine.delete_record(user_id=user_id, migraine_id=migraine_id)
        return deleted