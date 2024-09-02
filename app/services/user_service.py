# app/services/user_service.py

from typing import Optional
from fastapi import Depends, HTTPException
from app.schemas.user import UserCreate, UserDisplay, User
from app.db.mongodb_utils import get_database
from app.core.security import hash_password, verify_password
from bson import ObjectId
import asyncio
async def create_user(user: UserCreate, db=Depends(get_database)) -> UserDisplay:
    """Create a new user."""
    existing_user = await User.by_email(user.email)
    if existing_user is not None:
        raise HTTPException(409, "User with that email already exists")
    
    hashed = hash_password(user.password)
    user = User(email=user.email, hashed_password=hashed, username=user.username)
    await user.create()
    return user

async def get_user_by_username(username: str, db=Depends(get_database)) -> Optional[User]:
    user = await db['users'].find_one({"username": username})
    return User(**user) if user else None

async def authenticate_user(username: str, password: str) -> Optional[UserDisplay]:
    user = await get_user_by_username(username)
    if not user:
        return None
    if verify_password(password, user.hashed_password):
        return UserDisplay(**user.dict())
    return None