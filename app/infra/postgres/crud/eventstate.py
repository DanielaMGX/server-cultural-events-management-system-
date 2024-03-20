from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.eventstate import EventState
from app.schemas.eventstate import CreateEventState, UpdateEventState


class CRUDEventState(CRUDBase[EventState, CreateEventState, UpdateEventState]):
    async def create(self, *, obj_in: CreateEventState) -> int:
        obj_in_data = obj_in.dict()

        model = self.model(
            date_state=obj_in_data["date_state"],
            hour_state=obj_in_data["hour_state"],
            type_state=obj_in_data["type_state"],
            justification=obj_in_data["justification"],
            user_state=obj_in_data["user_state"],
            event_id=obj_in_data["event"],
        )

        await model.save()
        return model

    # async def get_all(
    #     self, *, payload: Dict[str, Any] = {}, skip: int = 0, limit: int = 10
    # ) -> List[Dict[str, Any]]:
    #     query = self.model.filter(**payload) if payload else self.model
    #     models = await query.all().offset(skip).limit(limit).order_by("id_state")

    #     results = []
    #     for model in models:
    #         event = await model.event
    #         results.append(
    #             {
    #                 "id_state": model.id_state,
    #                 "date_state": model.date_state,
    #                 "hour_state": model.hour_state,
    #                 "type_state": model.type_state,
    #                 "justification": model.justification,
    #                 "user_state": model.user_state,
    #                 "event_id": model.event_id,
    #                 "event_name": event.name,
    #             }
    #         )

    #     return results


crud_event_state = CRUDEventState(model=EventState)
