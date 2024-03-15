# crud_subevent.py
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.subevent import SubEvent
from app.schemas.event import CreateSubEvent, UpdateSubEvent

class CRUDSubevent(CRUDBase[SubEvent, CreateSubEvent, UpdateSubEvent]):
    ...

crud_subevent = CRUDSubevent(model=SubEvent)
