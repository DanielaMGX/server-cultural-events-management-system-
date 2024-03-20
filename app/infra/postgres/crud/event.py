# crud_event.py
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.event import Event
from app.schemas.event import CreateEvent, UpdateEvent


class CRUDEvent(CRUDBase[Event, CreateEvent, UpdateEvent]):
    ...


crud_event = CRUDEvent(model=Event)
