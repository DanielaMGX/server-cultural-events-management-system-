from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.accomplishment import Accomplishment
from app.schemas.accomplishment import CreateAccomplishment, UpdateAccomplishment


class CRUDAccomplishment(
    CRUDBase[
        Accomplishment,
        CreateAccomplishment,
        UpdateAccomplishment,
    ]
):
    async def complete_accomplishment(
        self, _id: int, accomplishment: UpdateAccomplishment
    ) -> bool:
        payload = accomplishment.model_dump(exclude_unset=True)
        payload["check"] = True
        await self.model.filter(id=_id).update(**payload)
        return True


crud_accomplishment = CRUDAccomplishment(model=Accomplishment)
