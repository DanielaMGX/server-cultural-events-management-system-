from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.historyeventstate import HistoryEventState
from app.schemas.historyeventstate import CreateHistoryEventState, UpdateHistoryEventState

class CRUDHistoryEventState(CRUDBase[HistoryEventState, CreateHistoryEventState, UpdateHistoryEventState]):
    pass

crud_history_event_state = CRUDHistoryEventState(model=HistoryEventState)
