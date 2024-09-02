# app/schemas/user_schema.py

from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from beanie import Document

class UserBase(BaseModel):
    username: str = Field(..., example="john_doe")
    email: str = Field(..., example="john@example.com")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, example="password")

class UserDisplay(UserBase):
    is_active: bool = Field(default=True, example=True)

class UserUpdate(UserBase):
    password: str = Field(None, min_length=6)
    
class User(UserDisplay, Document):
    hashed_password: str
    
    class Settings:
        name = "users"  # MongoDB collection name

    @classmethod
    async def by_email(cls, email: str) -> Optional["User"]:
        """Get a user by email."""
        return await cls.find_one(cls.email == email)
    
    @classmethod
    async def by_username(cls, username: str) -> Optional["User"]:
        """Get a user by username."""
        return await cls.find_one(cls.username == username)
        
    