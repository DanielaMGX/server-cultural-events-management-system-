
from pydantic import BaseModel, Field
from typing import List

class CreateSubevent(BaseModel):
    applies: bool = Field(...)
    responsability_id: int = Field(...)
    mode_id: int = Field(...)
    space_id: int = Field(...)

class UpdateSubevent(BaseModel):
    applies: bool = Field(None)
    responsability_id: int = Field(None)
    mode_id: int = Field(None)
    space_id: int = Field(None)

class SubeventDB(CreateSubevent):
    id: int = Field(...)

    class Config:
        orm_mode = True

class SubeventInResponse(BaseModel):
    subevent: SubeventDB

class SubeventsInResponse(BaseModel):
    subevents: List[SubeventDB]
