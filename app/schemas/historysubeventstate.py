from datetime import datetime
from pydantic import BaseModel, Field

class CreateHistorySubEventState(BaseModel):
    change_date: datetime = Field(...)
    state: str = Field(...)
    reason: str = Field(None)
    changed_by: str = Field(...)
    subevent_id: int = Field(...)

class UpdateHistorySubEventState(BaseModel):
    change_date: datetime = Field(None)
    state: str = Field(None)
    reason: str = Field(None)
    changed_by: str = Field(None)

class HistorySubEventStateDB(BaseModel):
    id: int = Field(...)
    change_date: datetime = Field(...)
    state: str = Field(...)
    reason: str = Field(None)
    changed_by: str = Field(...)
    subevent_id: int = Field(...)

    class Config:
        orm_mode = True
