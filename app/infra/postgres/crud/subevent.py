# crud_subevent.py
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.subevent import SubEvent
from app.schemas.subevent import CreateSubevent, UpdateSubevent

class CRUDSubevent(CRUDBase[SubEvent, CreateSubevent, UpdateSubevent]):
    ...

crud_subevent = CRUDSubevent(model=SubEvent)
