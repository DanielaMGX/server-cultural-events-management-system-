from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.space import CreateSpace, SpaceDB, UpdateSpace
from app.services.space import service_space

router = APIRouter()

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[SpaceDB],
    status_code=200,
)
async def get_all(skip: int = Query(0), limit: int = Query(10)):
    return await service_space.get_all(skip=skip, limit=limit)

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=SpaceDB,
    status_code=201,
)
async def create(space: CreateSpace):
    return await service_space.create(obj_in=space)

@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=SpaceDB,
    status_code=200,
)
async def read(id: int):
    space = await service_space.get_by_id(id)
    if space is None:
        raise HTTPException(status_code=404, detail="Space not found")
    return space

@router.patch(
    "/{id}",
    status_code=204,
)
async def update(id: int, space: UpdateSpace):
    updated = await service_space.update(id, obj_in=space)
    if not updated:
        raise HTTPException(status_code=404, detail="Space not found")

@router.delete("/{id}", status_code=204)
async def delete(id: int):
    deleted = await service_space.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Space not found")
