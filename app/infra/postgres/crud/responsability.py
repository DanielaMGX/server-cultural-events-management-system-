from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.responsability import Responsability
from app.schemas.responsability import Createresponsability, Updateresponsability

class CRUDresponsability(CRUDBase[Responsability, Createresponsability, Updateresponsability]):
    ...

crud_responsability = CRUDresponsability(model=Responsability)
