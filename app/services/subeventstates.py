from app.infra.postgres.crud.crud_subeventstate import crud_subeventstate
from app.services.base import BaseService

class ServiceSubEventState(BaseService):
    pass

service_subeventstate = ServiceSubEventState(crud=crud_subeventstate)
