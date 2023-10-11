from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.biblioteca import CreateBiblioteca, BibliotecaDB, SearchBiblioteca, UpdateBiblioteca
from app.services.biblioteca import service_biblioteca

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[BibliotecaDB],
    status_code=200,
    responses={
        200: {"description": "Bibliotecas found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(10),
    search: SearchBiblioteca = Depends(SearchBiblioteca),
):
    Bibliotecas = await service_biblioteca.get_all(
        skip=skip, limit=limit, payload=search.dict(exclude_none=True)
    )
    return Bibliotecas


@router.post(
    "",
    response_class=JSONResponse,
    response_model=BibliotecaDB,
    status_code=201,
    responses={
        201: {"description": "Biblioteca created"},
    },
)
async def create(new_Biblioteca: CreateBiblioteca):
    Biblioteca = await service_biblioteca.create(obj_in=new_Biblioteca)
    return Biblioteca


@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=BibliotecaDB,
    status_code=200,
    responses={
        200: {"description": "Biblioteca found"},
        404: {"description": "Biblioteca not found"},
    },
)
async def by_id(_id: int = Path(...)):
    Biblioteca = await service_biblioteca.get_by_id(_id=_id)
    if Biblioteca is None:
        raise HTTPException(status_code=404, detail="Biblioteca not found")
    return Biblioteca


@router.patch(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Biblioteca update"},
        404: {"description": "Biblioteca not found"},
    },
)
async def update(update_Biblioteca: UpdateBiblioteca, _id: int = Path(...)):
    await service_biblioteca.update(_id=_id, obj_in=update_Biblioteca)


@router.delete(
    "/{_id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Biblioteca delete"},
    },
)
async def delete(_id: int = Path(...)):
    Biblioteca = await service_biblioteca.delete(_id=_id)
    if Biblioteca == 0:
        raise HTTPException(status_code=404, detail="Biblioteca not found")
