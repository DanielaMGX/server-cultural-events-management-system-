
from typing import List,Dict
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response
from asyncio import gather
from app.schemas.event import CreateSubEvent, SubEventDB, UpdateSubEvent
from app.schemas.sub_event_has_responsability import CreateSubEventHasResponsability
from app.services.subevent import service_subevent
from app.services.sub_event_has_responsability import service_sub_event_has_responsability
from app.services.responsability import service_responsability
router = APIRouter()

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[SubEventDB],
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
    status_code=204,
    responses={
        204: {"description": "Subevent created"},
    },
)
async def create_subevent(subevent: CreateSubEvent):
    sub_event_id=await service_subevent.create(obj_in=subevent)
    # TODO: aca se debe buscar las responsabilidades que aplican para el evento
    responsabilities:List[Dict] = await service_responsability.get_all(skip=0, limit=99999)
    tasks = []
    for responsability in responsabilities:
        event_has_responsability = CreateSubEventHasResponsability(
            sub_event_id=sub_event_id, responsability_id=responsability.get("id"), state="Pendiente"
        )
        tasks.append(
            service_sub_event_has_responsability.create(obj_in=event_has_responsability)
        )
    await gather(*tasks)

@router.get(
    "/{_id}",
    response_class=JSONResponse,
    response_model=SubEventDB,
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
async def update_subevent(update_subevent: UpdateSubEvent, _id: int = Path(...)):
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
