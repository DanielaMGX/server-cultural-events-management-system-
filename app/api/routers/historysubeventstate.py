from typing import List
from fastapi import APIRouter, Depends, Query, Path, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.historysubeventstate import (
    CreateHistorySubEventState,
    HistorySubEventStateDB,
    UpdateHistorySubEventState
)
from app.services.service_historysubeventstate import service_history_subevent_state

router = APIRouter()

@router.post("/", response_model=HistorySubEventStateDB, status_code=201)
async def create_history_subevent_state(history_subevent_state: CreateHistorySubEventState):
    return await service_history_subevent_state.create(obj_in=history_subevent_state)

@router.get("/", response_model=List[HistorySubEventStateDB])
async def read_history_subevent_states(skip: int = 0, limit: int = 100):
    return await service_history_subevent_state.get_all(skip=skip, limit=limit)

@router.get("/{id}", response_model=HistorySubEventStateDB)
async def read_history_subevent_state(id: int = Path(...)):
    history_subevent_state = await service_history_subevent_state.get_by_id(_id=id)
    if not history_subevent_state:
        raise HTTPException(status_code=404, detail="HistorySubEventState not found")
    return history_subevent_state

@router.patch("/{id}", response_model=HistorySubEventStateDB)
async def update_history_subevent_state(id: int = Path(...), history_subevent_state: UpdateHistorySubEventState = Depends()):
    return await service_history_subevent_state.update(_id=id, obj_in=history_subevent_state)

@router.delete("/{id}", response_model=None)
async def delete_history_subevent_state(id: int = Path(...)):
    await service_history_subevent_state.delete(_id=id)
    return {"ok": True}
