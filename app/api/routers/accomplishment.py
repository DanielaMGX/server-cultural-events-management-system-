from typing import List

from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.accomplishment import AccomplishmentDB, UpdateAccomplishment
from app.services.accomplishment import service_accomplishment

router = APIRouter()


@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[AccomplishmentDB],
    status_code=200,
    responses={
        200: {"description": "Accomplishments found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(10),
):
    events = await service_accomplishment.get_all(skip=skip, limit=limit)
    return events


@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=AccomplishmentDB,
    status_code=200,
    responses={
        200: {"description": "Accomplishment found"},
        404: {"description": "Accomplishment not found"},
    },
)
async def get_by_id(_id: int = Path(...)):
    event = await service_accomplishment.get_by_id(_id=_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Accomplishment completed"},
        404: {"description": "Accomplishment not found"},
    },
)
async def complete(update_accomplishment: UpdateAccomplishment, _id: int = Path(...)):
    updated = await service_accomplishment.complete_accomplishment(
        _id=_id, accomplishment=update_accomplishment
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Accomplishment not found")


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
async def delete(_id: int = Path(...)):
    deleted = await service_accomplishment.delete(_id=_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
