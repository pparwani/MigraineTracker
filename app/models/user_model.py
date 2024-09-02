# app/models/user_model.py

from typing import Optional
from pydantic import EmailStr, Field
from .base_model import MongoModel

class UserCreate(MongoModel):
    username: str = Field(..., example="john_doe")
    email: EmailStr = Field(..., example="john@example.com")
    password: str = Field(..., example="securepassword")

class UserDisplay(MongoModel):
    id: str
    username: str
    email: EmailStr
    is_active: bool = True

class UserInDB(UserDisplay):
    hashed_password: str