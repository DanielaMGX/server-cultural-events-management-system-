from datetime import date

from pydantic import BaseModel, Field


class CreateHistoryEventState(BaseModel):
    day: date = Field(...)
    time: str = Field(...)
    state: str = Field(...)
    justification: str = Field(None)
    event_id: int = Field(...)


class UpdateHistoryEventState(BaseModel):
    day: date = Field(None)
    time: str = Field(None)
    state: str = Field(None)
    justification: str = Field(None)


class HistoryEventStateDB(BaseModel):
    id: int = Field(...)
    day: date = Field(...)
    time: str = Field(...)
    state: str = Field(...)
    justification: str = Field(None)
    event_id: int = Field(...)

    class Config:
        from_attributes = True
