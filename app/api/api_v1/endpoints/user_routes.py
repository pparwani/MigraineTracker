# app/api/api_v1/endpoints/user_routes.py

from fastapi import APIRouter, HTTPException, Depends, status, Body
from app.schemas.user import UserCreate, UserDisplay, User
from app.services.user_service import create_user, authenticate_user, get_user_by_username
from app.api.dependencies import get_current_user
from app.db.mongodb_utils import get_database

router = APIRouter()

@router.post("/register", response_model=UserDisplay, status_code=201)
async def register_user(user: UserCreate, db=Depends(get_database)):
    created_user = await create_user(user, db=db)
    if not created_user:
        raise HTTPException(status_code=400, detail="Error registering user")
    return created_user

@router.post("/login", response_model=UserDisplay)
async def login_user(username: str, password: str):
    user = await authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user

@router.get("/me", response_model=UserDisplay)
async def read_user(current_user: User = Depends(get_current_user)):
    return current_user