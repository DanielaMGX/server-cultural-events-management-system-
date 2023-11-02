
from app.infra.postgres.crud.subevent import crud_subevent
from app.services.base import BaseService

class ServiceSubevent(BaseService):
    ...

service_subevent = ServiceSubevent(crud=crud_subevent)
