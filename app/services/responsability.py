from app.infra.postgres.crud.responsability import crud_responsability
from app.services.base import BaseService


class Serviceresponsability(BaseService):
    ...


service_responsability = Serviceresponsability(crud=crud_responsability)
