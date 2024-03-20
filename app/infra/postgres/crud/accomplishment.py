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
    ) -> int:
        model = await self.model.get(id=_id)
        payload = accomplishment.model_dump(exclude_unset=True)
        payload["check"] = True
        await model.update_from_dict(payload).save()
        return True


crud_accomplishment = CRUDAccomplishment(model=Accomplishment)
