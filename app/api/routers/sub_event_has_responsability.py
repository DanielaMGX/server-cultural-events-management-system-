from typing import List

from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse

from app.schemas.sub_event_has_responsability import SubEventHasResponsabilityDB,UpdateSubEventHasResponsability
from app.services.sub_event_has_responsability import service_sub_event_has_responsability

router = APIRouter()


@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[SubEventHasResponsabilityDB],
    status_code=200,
    responses={
        200: {"description": "Events found"},
    },
)
async def get_by_event_id(
    event_id: int = Query(...),
):
    events = await service_sub_event_has_responsability.get_by_sub_event_id(event_id=event_id)
    return events




@router.patch(
    "/{_id}",
    status_code=204,
    responses={
        204: {"description": "Event updated"},
    },
)
async def update(update_event_has_responsability: UpdateSubEventHasResponsability, _id: int = Path(...)):
    updated = await service_sub_event_has_responsability.update(_id=_id, obj_in=update_event_has_responsability)
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")

