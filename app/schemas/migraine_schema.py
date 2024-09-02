# app/schemas/migraine_schema.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MigraineBase(BaseModel):
    start_time: datetime = Field(..., example="2024-01-01T15:00:00Z")
    end_time: Optional[datetime] = Field(None, example="2024-01-01T16:00:00Z")
    symptoms: List[str] = Field(..., example=["nausea", "photophobia"])
    triggers: List[str] = Field(..., example=["stress", "lack of sleep"])
    remediations: List[str] = Field(..., example=["medication", "resting in a dark room"])
    medications: List[str] = Field(..., example=["ibuprofen", "acetaminophen"])

class MigraineCreate(MigraineBase):
    pass

class MigraineDisplay(MigraineBase):
    id: str = Field(..., example="abc123")

class MigraineUpdate(BaseModel):
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    symptoms: Optional[List[str]]
    triggers: Optional[List[str]]
    remediations: Optional[List[str]]
    medications: Optional[List[str]]