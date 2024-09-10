# app/api/dependencies.py

from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_token
from app.schemas.user import UserDisplay, User
from app.db.mongodb_utils import get_database
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = verify_token(token, credentials_exception)
    _id = payload.get("sub")
    if _id is None:
        raise credentials_exception
    user = await User.by_id(user_id=_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDisplay(**user.model_dump())