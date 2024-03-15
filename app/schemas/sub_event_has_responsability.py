from typing import Optional

from pydantic import BaseModel, Field


class CreateSubEventHasResponsability(BaseModel):
    sub_event_id: int
    responsability_id: int
    state: str


class UpdateSubEventHasResponsability(BaseModel):
    state: Optional[str] = Field(None)
    deliverable: Optional[str] = Field(None)


class SubEventHasResponsabilityDB(BaseModel):
    id: int
    sub_event_id: int
    responsability_id: int
    state: str
    deliverable: Optional[str] = Field(None)

    class Config:
        from_attributes = True
