from datetime import date, time
from pydantic import BaseModel, Field

class CreateHistoryEventState(BaseModel):
    date: date = Field(...)
    time: time = Field(...)
    state: str = Field(...)
    justification: str = Field(None)
    event_id: int = Field(...)

class UpdateHistoryEventState(BaseModel):
    date: date = Field(None)
    time: time = Field(None)
    state: str = Field(None)
    justification: str = Field(None)

class HistoryEventStateDB(BaseModel):
    id: int = Field(...)
    date: date = Field(...)
    time: time = Field(...)
    state: str = Field(...)
    justification: str = Field(None)
    event_id: int = Field(...)

    class Config:
        orm_mode = True
