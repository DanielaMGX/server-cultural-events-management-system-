from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.respuesta import CreateRespuesta, RespuestaDB, SearchRespuesta, UpdateRespuesta
from app.services.respuesta import service_respuesta

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[RespuestaDB],
    status_code=200,
    responses={
        200: {"description": "Respuestas found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(10),
    search: SearchRespuesta = Depends(SearchRespuesta),
):
    Respuestas = await service_respuesta.get_all(
        skip=skip, limit=limit, payload=search.dict(exclude_none=True)
    )
    return Respuestas


@router.post(
    "",
    response_class=JSONResponse,
    response_model=RespuestaDB,
    status_code=201,
    responses={
        201: {"description": "Respuesta created"},
    },
)
async def create(new_Respuesta: CreateRespuesta):
    Respuesta = await service_respuesta.create(obj_in=new_Respuesta)
    return Respuesta


@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=RespuestaDB,
    status_code=200,
    responses={
        200: {"description": "Respuesta found"},
        404: {"description": "Respuesta not found"},
    },
)
async def by_id(_id: int = Path(...)):
    Respuesta = await service_respuesta.get_by_id(_id=_id)
    if Respuesta is None:
        raise HTTPException(status_code=404, detail="Respuesta not found")
    return Respuesta


@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Respuesta update"},
        404: {"description": "Respuesta not found"},
    },
)
async def update(update_Respuesta: UpdateRespuesta, _id: int = Path(...)):
    await service_respuesta.update(_id=_id, obj_in=update_Respuesta)


@router.delete(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Respuesta delete"},
    },
)
async def delete(_id: int = Path(...)):
    Respuesta = await service_respuesta.delete(_id=_id)
    if Respuesta == 0:
        raise HTTPException(status_code=404, detail="Respuesta not found")
