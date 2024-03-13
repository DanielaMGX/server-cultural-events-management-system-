from typing import List
from fastapi import APIRouter, Depends, Query, Path, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.subeventstate import (
    CreateSubEventState,
    SubEventStateDB,
    UpdateSubEventState
)
from app.services.subeventstate import service_subeventstate

router = APIRouter()

@router.post("/", response_model=SubEventStateDB, status_code=201)
async def create_subevent_state(subevent_state: CreateSubEventState):
    return await service_subeventstate.create(obj_in=subevent_state)

@router.get("/", response_model=List[SubEventStateDB])
async def read_subevent_states(skip: int = 0, limit: int = 100):
    return await service_subeventstate.get_all(skip=skip, limit=limit)

@router.get("/{id}", response_model=SubEventStateDB)
async def read_subevent_state(id: int = Path(...)):
    subevent_state = await service_subeventstate.get_by_id(_id=id)
    if not subevent_state:
        raise HTTPException(status_code=404, detail="SubEventState not found")
    return subevent_state

@router.patch("/{id}", response_model=SubEventStateDB)
async def update_subevent_state(id: int = Path(...), subevent_state: UpdateSubEventState = Depends()):
    return await service_subeventstate.update(_id=id, obj_in=subevent_state)

@router.delete("/{id}", response_model=None)
async def delete_subevent_state(id: int = Path(...)):
    await service_subeventstate.delete(_id=id)
    return {"ok": True}
