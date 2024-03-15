from typing import Optional

from pydantic import BaseModel, Field


class CreateEventHasResponsability(BaseModel):
    event_id: int
    responsability_id: int
    state: str


class UpdateEventHasResponsability(BaseModel):
    state: Optional[str] = Field(None)
    deliverable: Optional[str] = Field(None)


class EventHasResponsabilityDB(BaseModel):
    id: int
    event_id: int
    responsability_id: int
    state: str
    deliverable: Optional[str] = Field(None)

    class Config:
        from_attributes = True
