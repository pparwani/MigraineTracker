# app/api/api_v1/endpoints/migraine_routes.py

from fastapi import APIRouter, HTTPException, Depends, Body
from typing import List
from app.schemas.migraine_schema import MigraineCreate, MigraineDisplay, MigraineUpdate
from app.services.migraine_service import MigraineService
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=MigraineDisplay, status_code=201)
async def create_migraine(migraine: MigraineCreate, current_user: str = Depends(get_current_user)):
    return await MigraineService.create_migraine(user_id=current_user.id, migraine_data=migraine)

@router.get("/", response_model=List[MigraineDisplay])
async def read_migraines(current_user: str = Depends(get_current_user)):
    return await MigraineService.get_all_migraines(user_id=current_user.id)

@router.get("/{migraine_id}", response_model=MigraineDisplay)
async def read_migraine(migraine_id: str, current_user: str = Depends(get_current_user)):
    migraine = await MigraineService.get_migraine(user_id=current_user.id, migraine_id=migraine_id)
    if migraine is None:
        raise HTTPException(status_code=404, detail="Migraine not found")
    return migraine

@router.put("/{migraine_id}", response_model=MigraineDisplay)
async def update_migraine(migraine_id: str, migraine: MigraineUpdate, current_user: str = Depends(get_current_user)):
    updated_migraine = await MigraineService.update_migraine(user_id=current_user.id, migraine_id=migraine_id, migraine_update=migraine)
    if updated_migraine is None:
        raise HTTPException(status_code=404, detail="Migraine not found")
    return updated_migraine

@router.delete("/{migraine_id}", response_model=bool)
async def delete_migraine(migraine_id: str, current_user: str = Depends(get_current_user)):
    result = await MigraineService.delete_migraine(user_id=current_user.id, migraine_id=migraine_id)
    if not result:
        raise HTTPException(status_code=404, detail="Migraine not found")
    return result