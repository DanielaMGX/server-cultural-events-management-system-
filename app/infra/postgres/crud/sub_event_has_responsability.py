from typing import Any, Dict, List

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.sub_event_has_responsability import SubEventHasResponsability
from app.schemas.sub_event_has_responsability import (
    CreateSubEventHasResponsability,
    UpdateSubEventHasResponsability,
)


class CRUDSubEventHasResponsability(
    CRUDBase[
        SubEventHasResponsability,
        CreateSubEventHasResponsability,
        UpdateSubEventHasResponsability,
    ]
):
    def __init__(self, *, model: SubEventHasResponsability) -> None:
        super().__init__(model=model)
        self.__model = model

    async def get_by_sub_event_id(self, *, sub_event_id: int) -> List[Dict[str, Any]]:
        objs_db = await self.__model.filter(sub_event_id=sub_event_id)
        return objs_db


crud_sub_event_has_responsability = CRUDSubEventHasResponsability(model=SubEventHasResponsability)
