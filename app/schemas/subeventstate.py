from pydantic import BaseModel, Field

class CreateSubEventState(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    status: str = Field(...)
    subevent_id: int = Field(...)

class UpdateSubEventState(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    status: str = Field(None)

class SubEventStateDB(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    status: str = Field(...)
    subevent_id: int = Field(...)

    class Config:
        orm_mode = True
