from typing import List
from fastapi import APIRouter, Depends, Path, HTTPException
from app.schemas.historyeventstate import (
    CreateHistoryEventState,
    HistoryEventStateDB,
    UpdateHistoryEventState
)
from app.services.historyeventstate import service_history_event_state

router = APIRouter()

@router.post("/", response_model=HistoryEventStateDB)
async def create_history_event_state(history_event_state: CreateHistoryEventState):
    return await service_history_event_state.create(obj_in=history_event_state)

@router.get("/", response_model=List[HistoryEventStateDB])
async def read_history_event_states():
    return await service_history_event_state.get_all()

@router.get("/{id}", response_model=HistoryEventStateDB)
async def read_history_event_state(id: int = Path(...)):
    history_event_state = await service_history_event_state.get_by_id(_id=id)
    if not history_event_state:
        raise HTTPException(status_code=404, detail="HistoryEventState not found")
    return history_event_state

@router.patch("/{id}", response_model=HistoryEventStateDB)
async def update_history_event_state(id: int, history_event_state: UpdateHistoryEventState):
    return await service_history_event_state.update(_id=id, obj_in=history_event_state)

@router.delete("/{id}")
async def delete_history_event_state(id: int = Path(...)):
    await service_history_event_state.delete(_id=id)
    return {"ok": True}
