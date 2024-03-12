from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.historysubeventstate import HistorySubEventState
from app.schemas.historysubeventstate import CreateHistorySubEventState, UpdateHistorySubEventState

class CRUDHistorySubEventState(CRUDBase[HistorySubEventState, CreateHistorySubEventState, UpdateHistorySubEventState]):
    pass

crud_history_subevent_state = CRUDHistorySubEventState(model=HistorySubEventState)
