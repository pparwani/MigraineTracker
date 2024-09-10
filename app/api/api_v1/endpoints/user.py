# app/api/api_v1/endpoints/user_routes.py

from fastapi import APIRouter, HTTPException, Depends, status, Body
from app.schemas.user import UserCreate, UserDisplay, User
from app.services.auth_service import create_user, authenticate_user, get_user_by_username
from app.api.dependencies import get_current_user
from app.db.mongodb_utils import get_database
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.get("/me", response_model=UserDisplay)
async def read_user(current_user: User = Depends(get_current_user)):
    return current_user