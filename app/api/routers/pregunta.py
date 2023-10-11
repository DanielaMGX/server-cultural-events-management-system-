from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.pregunta import CreatePregunta, PreguntaDB, SearchPregunta, UpdatePregunta
from app.services.pregunta import service_pregunta

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[PreguntaDB],
    status_code=200,
    responses={
        200: {"description": "preguntas found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(10),
    search: SearchPregunta = Depends(SearchPregunta),
):
    preguntas = await service_pregunta.get_all(
        skip=skip, limit=limit, payload=search.dict(exclude_none=True)
    )
    return preguntas


@router.post(
    "",
    response_class=JSONResponse,
    response_model=PreguntaDB,
    status_code=201,
    responses={
        201: {"description": "pregunta created"},
    },
)
async def create(new_pregunta: CreatePregunta):
    pregunta = await service_pregunta.create(obj_in=new_pregunta)
    return pregunta


@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=PreguntaDB,
    status_code=200,
    responses={
        200: {"description": "pregunta found"},
        404: {"description": "pregunta not found"},
    },
)
async def by_id(_id: int = Path(...)):
    pregunta = await service_pregunta.get_by_id(_id=_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="pregunta not found")
    return pregunta


@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "pregunta update"},
        404: {"description": "pregunta not found"},
    },
)
async def update(update_pregunta: UpdatePregunta, _id: int = Path(...)):
    await service_pregunta.update(_id=_id, obj_in=update_pregunta)


@router.delete(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "pregunta delete"},
    },
)
async def delete(_id: int = Path(...)):
    pregunta = await service_pregunta.delete(_id=_id)
    if pregunta == 0:
        raise HTTPException(status_code=404, detail="pregunta not found")
