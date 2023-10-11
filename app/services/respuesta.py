from app.infra.postgres.crud.respuesta import crud_respuesta
from app.services.base import BaseService


class ServiceRespuestas(BaseService):
    ...


service_respuesta = ServiceRespuestas(crud=crud_respuesta)
