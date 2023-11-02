
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.subevent import CreateSubevent, SubeventDB, UpdateSubevent
from app.services.subevent import service_subevent

router = APIRouter()

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[SubeventDB],
    status_code=200,
    responses={
        200: {"description": "Subevents found"},
    },
)
async def get_all_subevents(
    skip: int = Query(0),
    limit: int = Query(10),
):
    subevents = await service_subevent.get_all(skip=skip, limit=limit)
    return subevents

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=SubeventDB,
    status_code=201,
    responses={
        201: {"description": "Subevent created"},
    },
)
async def create_subevent(subevent: CreateSubevent):
    subevent_db = await service_subevent.create(obj_in=subevent)
    return subevent_db

@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=SubeventDB,
    status_code=200,
    responses={
        200: {"description": "Subevent found"},
        404: {"description": "Subevent not found"},
    },
)
async def get_subevent_by_id(_id: int = Path(...)):
    subevent = await service_subevent.get_by_id(_id=_id)
    if subevent is None:
        raise HTTPException(status_code=404, detail="Subevent not found")
    return subevent

@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Subevent updated"},
        404: {"description": "Subevent not found"},
    },
)
async def update_subevent(update_subevent: UpdateSubevent, _id: int = Path(...)):
    updated = await service_subevent.update(_id=_id, obj_in=update_subevent)
    if not updated:
        raise HTTPException(status_code=404, detail="Subevent not found")

@router.delete(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Subevent deleted"},
        404: {"description": "Subevent not found"},
    },
)
async def delete_subevent(_id: int = Path(...)):
    deleted = await service_subevent.delete(_id=_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Subevent not found")
