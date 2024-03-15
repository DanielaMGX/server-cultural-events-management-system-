from typing import Any, Dict, List

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.event_has_responsability import EventHasResponsability
from app.schemas.event_has_responsability import (
    CreateEventHasResponsability,
    UpdateEventHasResponsability,
)


class CRUDEventHasResponsability(
    CRUDBase[
        EventHasResponsability,
        CreateEventHasResponsability,
        UpdateEventHasResponsability,
    ]
):
    def __init__(self, *, model: EventHasResponsability) -> None:
        super().__init__(model=model)
        self.__model = model

    async def get_by_event_id(self, *, event_id: int) -> List[Dict[str, Any]]:
        objs_db = await self.__model.filter(event_id=event_id)
        return objs_db


crud_event_has_responsability = CRUDEventHasResponsability(model=EventHasResponsability)
