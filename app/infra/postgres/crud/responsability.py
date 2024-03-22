from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.responsability import Responsability
from app.schemas.responsability import CreateResponsability, UpdateResponsability


class CRUDresponsability(
    CRUDBase[Responsability, CreateResponsability, UpdateResponsability]
):
    ...


crud_responsability = CRUDresponsability(model=Responsability)
