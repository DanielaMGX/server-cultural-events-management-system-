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
    ...


crud_accomplishment = CRUDAccomplishment(model=Accomplishment)
