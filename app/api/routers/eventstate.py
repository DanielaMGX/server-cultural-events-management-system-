from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.eventstate import (
    CreateEventState,
    EventStateDB,
    SearchEventState,
    UpdateEventState,
)
from app.services.eventstate import service_event_state

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[EventStateDB],
    status_code=200,
    responses={
        200: {"description": "Event states found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(10),
    search: SearchEventState = Depends(SearchEventState),
):
    event_states = await service_event_state.get_all(
        skip=skip, limit=limit, payload=search.dict(exclude_none=True)
    )
    return event_states


@router.post(
    "",
    response_class=JSONResponse,
    response_model=EventStateDB,
    status_code=201,
    responses={
        201: {"description": "Event state created"},
    },
)
async def create(new_event_state: CreateEventState):
    event_state = await service_event_state.create(obj_in=new_event_state)
    return event_state


@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=EventStateDB,
    status_code=200,
    responses={
        200: {"description": "Event state found"},
        404: {"description": "Event state not found"},
    },
)
async def by_id(_id: int = Path(...)):
    event_state = await service_event_state.get_by_id(_id=_id)
    if event_state is None:
        raise HTTPException(status_code=404, detail="Event state not found")
    return event_state


@router.patch(
    "/{_id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Event state updated"},
        404: {"description": "Event state not found"},
    },
)
async def update(update_event_state: UpdateEventState, _id: int = Path(...)):
    result = await service_event_state.update(_id=_id, obj_in=update_event_state)
    if result == 0:
        raise HTTPException(status_code=404, detail="Event state not found")


@router.delete(
    "/{_id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Event state deleted"},
        404: {"description": "Event state not found"},
    },
)
async def delete(_id: int = Path(...)):
    result = await service_event_state.delete(_id=_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="Event state not found")
