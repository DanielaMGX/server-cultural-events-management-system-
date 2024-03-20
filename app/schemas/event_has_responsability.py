from pydantic import BaseModel


class CreateEventHasResponsability(BaseModel):
    event_id: int
    responsability_by_mode_id: int
    accomplishment_id: int


class UpdateEventHasResponsability(BaseModel):
    ...


class EventHasResponsabilityDB(BaseModel):
    id: int
    event_id: int
    responsability_by_mode_id: int
    accomplishment_id: int

    class Config:
        from_attributes = True
