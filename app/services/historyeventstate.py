from app.infra.postgres.crud.historyeventstate import crud_history_event_state
from app.services.base import BaseService

class ServiceHistoryEventState(BaseService):
    pass

service_history_event_state = ServiceHistoryEventState(crud=crud_history_event_state)
