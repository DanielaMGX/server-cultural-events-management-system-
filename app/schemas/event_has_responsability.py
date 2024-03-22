from typing import Optional

from pydantic import BaseModel, Field


class CreateEventHasResponsability(BaseModel):
    event_id: int
    responsability_by_mode_id: Optional[int] = Field(None)
    accomplishment_id: int
    specific_responsability_id: Optional[int] = Field(None)


class UpdateEventHasResponsability(BaseModel):
    ...


class EventHasResponsabilityDB(BaseModel):
    id: int
    event_id: int
    responsability_by_mode_id: Optional[int]
    accomplishment_id: int
    specific_responsability_id: Optional[int]

    class Config:
        from_attributes = True
