from fastapi import APIRouter, HTTPException, Depends, status, Body
from app.schemas.user import UserCreate, UserDisplay, User
from app.services.auth_service import create_user, authenticate_user, get_user_by_username
from app.api.dependencies import get_current_user
from app.db.mongodb_utils import get_database
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=UserDisplay, status_code=201)
async def register_user(user: UserCreate, db=Depends(get_database)):
    created_user = await create_user(user, db=db)
    if not created_user:
        raise HTTPException(status_code=400, detail="Error registering user")
    return created_user

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await authenticate_user(username=form_data.username, password=form_data.password)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"access_token": token, "token_type": "bearer"}