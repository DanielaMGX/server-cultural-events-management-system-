from app.infra.postgres.crud.event import crud_event
from app.services.base import BaseService


class ServiceEvent(BaseService):
    ...


service_event = ServiceEvent(crud=crud_event)
