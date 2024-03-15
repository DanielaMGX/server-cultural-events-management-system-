from typing import List

from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.responsability import (
    Createresponsability,
    Updateresponsability,
    responsabilityDB,
)
from app.services.responsability import service_responsability

router = APIRouter()


@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[responsabilityDB],
    status_code=200,
    responses={
        200: {"description": "Responsibilities found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(10),
):
    responsibilities = await service_responsability.get_all(skip=skip, limit=limit)
    return responsibilities


@router.post(
    "/",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "responsability created"},
    },
)
async def create(responsability: Createresponsability):
    await service_responsability.create(obj_in=responsability)


@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=responsabilityDB,
    status_code=200,
    responses={
        200: {"description": "responsability found"},
        404: {"description": "responsability not found"},
    },
)
async def by_id(_id: int = Path(...)):
    responsability = await service_responsability.get_by_id(_id=_id)
    if responsability is None:
        raise HTTPException(status_code=404, detail="responsability not found")
    return responsability


@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "responsability updated"},
        404: {"description": "responsability not found"},
    },
)
async def update(update_responsability: Updateresponsability, _id: int = Path(...)):
    updated = await service_responsability.update(_id=_id, obj_in=update_responsability)
    if not updated:
        raise HTTPException(status_code=404, detail="responsability not found")


@router.delete(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "responsability deleted"},
        404: {"description": "responsability not found"},
    },
)
async def delete(_id: int = Path(...)):
    deleted = await service_responsability.delete(_id=_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="responsability not found")
