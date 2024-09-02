# app/models/migraine_model.py

from typing import List, Optional
from datetime import datetime
from pydantic import Field
from .base_model import MongoModel

class MigraineCreate(MongoModel):
    start_time: datetime = Field(..., example="2024-08-31T13:00:00Z")
    end_time: Optional[datetime] = Field(None, example="2024-08-31T14:30:00Z")
    symptoms: List[str] = Field(..., example=["nausea", "sensitivity to light"])
    possible_triggers: List[str] = Field(..., example=["stress", "lack of sleep"])
    remediations: List[str] = Field(..., example=["lying down", "dark room"])
    medications_taken: List[str] = Field(..., example=["ibuprofen"])

class MigraineDisplay(MigraineCreate):
    id: str
    user_id: str

class MigraineUpdate(MongoModel):
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    symptoms: Optional[List[str]]
    possible_triggers: Optional[List[str]]
    remediations: Optional[List[str]]
    medications_taken: Optional[List[str]]