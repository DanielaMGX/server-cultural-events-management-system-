
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.event import CreateEvent, EventDB, UpdateEvent
from app.services.event import service_event

router = APIRouter()

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[EventDB],
    status_code=200,
    responses={
        200: {"description": "Events found"},
    },
)
async def get_all_events(
    skip: int = Query(0),
    limit: int = Query(10),
):
    events = await service_event.get_all(skip=skip, limit=limit)
    return events

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=EventDB,
    status_code=201,
    responses={
        201: {"description": "Event created"},
    },
)
async def create_event(event: CreateEvent):
    event_db = await service_event.create(obj_in=event)
    return event_db

@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=EventDB,
    status_code=200,
    responses={
        200: {"description": "Event found"},
        404: {"description": "Event not found"},
    },
)
async def get_event_by_id(_id: int = Path(...)):
    event = await service_event.get_by_id(_id=_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Event updated"},
        404: {"description": "Event not found"},
    },
)
async def update_event(update_event: UpdateEvent, _id: int = Path(...)):
    updated = await service_event.update(_id=_id, obj_in=update_event)
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")

@router.delete(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Event deleted"},
        404: {"description": "Event not found"},
    },
)
async def delete_event(_id: int = Path(...)):
    deleted = await service_event.delete(_id=_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
