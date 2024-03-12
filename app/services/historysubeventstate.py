from app.infra.postgres.crud.crud_historysubeventstate import crud_history_subevent_state
from app.services.base import BaseService

class ServiceHistorySubEventState(BaseService):
    pass

service_history_subevent_state = ServiceHistorySubEventState(crud=crud_history_subevent_state)
