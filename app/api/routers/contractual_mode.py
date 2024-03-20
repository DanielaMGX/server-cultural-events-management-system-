from typing import List

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from app.schemas.contractual_mode import (
    ContractualModeDB,
    CreateContractualMode,
    UpdateContractualMode,
)
from app.services.contractual_mode import service_contractual_mode

router = APIRouter()


@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[ContractualModeDB],
    status_code=200,
)
async def get_all(skip: int = Query(0), limit: int = Query(10)):
    return await service_contractual_mode.get_all(skip=skip, limit=limit)


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=ContractualModeDB,
    status_code=201,
)
async def create(mode: CreateContractualMode):
    return await service_contractual_mode.create(obj_in=mode)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=ContractualModeDB,
    status_code=200,
)
async def read(id: int):
    mode = await service_contractual_mode.get_by_id(_id=id)
    if mode is None:
        raise HTTPException(status_code=404, detail="Mode not found")
    return mode


@router.patch(
    "/{id}",
    status_code=204,
)
async def update(id: int, mode: UpdateContractualMode):
    updated = await service_contractual_mode.update(_id=id, obj_in=mode)
    if not updated:
        raise HTTPException(status_code=404, detail="Mode not found")


@router.delete("/{id}", status_code=204)
async def delete(id: int):
    deleted = await service_contractual_mode.delete(_id=id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Mode not found")
