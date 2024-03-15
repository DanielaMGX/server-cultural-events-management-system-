from typing import List, Optional

from pydantic import BaseModel, Field


class CreateEventState(BaseModel):
    date_state: str = Field(...)
    hour_state: str = Field(...)
    type_state: str = Field(...)
    justification: Optional[str] = Field(None)
    user_state: str = Field(...)
    event_id: int = Field(...)


class SearchEventState(BaseModel):
    date_state: Optional[str] = Field(None)
    hour_state: Optional[str] = Field(None)
    type_state: Optional[str] = Field(None)
    justification: Optional[str] = Field(None)
    user_state: Optional[str] = Field(None)
    event_id: Optional[int] = Field(None)


class UpdateEventState(BaseModel):
    date_state: Optional[str] = Field(None)
    hour_state: Optional[str] = Field(None)
    type_state: Optional[str] = Field(None)
    justification: Optional[str] = Field(None)
    user_state: Optional[str] = Field(None)


class EventStateDB(BaseModel):
    id: int = Field(...)
    date_state: str = Field(...)
    hour_state: str = Field(...)
    type_state: str = Field(...)
    justification: Optional[str] = Field(None)
    user_state: str = Field(...)
    event_id: int = Field(...)

    class Config:
        from_attributes = True


class EventStateInResponse(BaseModel):
    event_state: EventStateDB


class EventStatesInResponse(BaseModel):
    event_states: List[EventStateDB]
