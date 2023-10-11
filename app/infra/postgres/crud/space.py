from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.space import Space
from app.schemas.space import CreateSpace, UpdateSpace

class CRUDSpace(CRUDBase[Space, CreateSpace, UpdateSpace]):
    ...

crud_space = CRUDSpace(model=Space)
