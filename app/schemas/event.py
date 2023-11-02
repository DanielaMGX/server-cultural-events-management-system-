
from pydantic import BaseModel, Field
from typing import List

class CreateEvent(BaseModel):
    name: str = Field(...)
    contractual_mode_id: int = Field(None)
    space_id: int = Field(None)

class UpdateEvent(BaseModel):
    name: str = Field(None)
    contractual_mode_id: int = Field(None)
    space_id: int = Field(None)

class EventDB(CreateEvent):
    id: int = Field(...)

    class Config:
        orm_mode = True

class EventInResponse(BaseModel):
    event: EventDB

class EventsInResponse(BaseModel):
    events: List[EventDB]
