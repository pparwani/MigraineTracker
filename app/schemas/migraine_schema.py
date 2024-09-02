from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from beanie import Document

class MigraineBase(BaseModel):
    start_time: int = Field(..., example=1700000000)  # Unix timestamp
    end_time: Optional[int] = Field(None, example=1700003600)  # Unix timestamp
    symptoms: List[str] = Field(..., example=["nausea", "photophobia"])
    triggers: List[str] = Field(..., example=["stress", "lack of sleep"])
    remediations: List[str] = Field(..., example=["medication", "resting in a dark room"])
    medications: List[str] = Field(..., example=["ibuprofen", "acetaminophen"])

    @field_validator('start_time', 'end_time', mode='before')
    def validate_unix_timestamp(cls, value):
        if not value:
            return None
        # Convert to integer if value is a string and check if it's a valid Unix timestamp
        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                raise ValueError("Invalid Unix timestamp: must be an integer or a string representing an integer")

        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid Unix timestamp: must be a non-negative integer")
        
        return value


class MigraineCreate(MigraineBase):
    pass

class MigraineDisplay(MigraineBase):
    id: str = Field(..., example="60c72b2f9b1d8b5f5f57e1b6")
    user_id: str = Field(..., example="60c72b2f9b1d8b5f5f57e1b6")
    
    @field_validator('id', 'user_id',mode='before')
    def convert_objectid_to_str(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value


class MigraineUpdate(BaseModel):
    start_time: Optional[int]  # Unix timestamp
    end_time: Optional[int]  # Unix timestamp
    symptoms: Optional[List[str]]
    triggers: Optional[List[str]]
    remediations: Optional[List[str]]
    medications: Optional[List[str]]

    @field_validator('start_time', 'end_time', mode='before')
    def validate_unix_timestamp(cls, value):
        if not value:
            return None
        # Convert to integer if value is a string and check if it's a valid Unix timestamp
        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                raise ValueError("Invalid Unix timestamp: must be an integer or a string representing an integer")

        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid Unix timestamp: must be a non-negative integer")
        
        return value

class Migraine(MigraineBase, Document):
    user_id: ObjectId = Field(..., alias="user_id")  # Reference to the User's ObjectId
    class Settings:
        name = "migraine_episodes"  # MongoDB collection name
    
    model_config = {
        "arbitrary_types_allowed": True,
    }

    @classmethod
    async def by_user(cls, user_id: str) -> Optional[List["MigraineDisplay"]]:
        if not ObjectId.is_valid(user_id):
            return None
        migraines = await cls.find(cls.user_id == ObjectId(user_id)).to_list()
        return [MigraineDisplay(**migraine.model_dump()) for migraine in migraines]

    @classmethod
    async def by_id(cls, id: str) -> Optional["Migraine"]:
        """Get a migraine record by ID."""
        if not ObjectId.is_valid(id):
            return None
        return await cls.find_one(cls.id == ObjectId(id))

    @classmethod
    async def insert_record(cls, new_migraine: MigraineCreate, user_id: ObjectId) -> "MigraineDisplay":
        new_record = Migraine(**new_migraine.model_dump(), user_id=user_id)
        created = await new_record.insert()
        return MigraineDisplay(**created.model_dump())