from typing import Any, Dict, List

from app.infra.postgres.crud.sub_event_has_responsability import (
    crud_sub_event_has_responsability,
)
from app.services.base import BaseService


class ServiceSubEventHasResponsability(BaseService):
    def __init__(self, *, crud: Any) -> None:
        super().__init__(crud=crud)
        self.__crud = crud

    async def get_by_sub_event_id(self, *, sub_event_id: int) -> List[Dict[str, Any]]:
        objs_db = await self.__crud.get_by_sub_event_id(sub_event_id=sub_event_id)
        return objs_db


service_sub_event_has_responsability = ServiceSubEventHasResponsability(
    crud=crud_sub_event_has_responsability
)
