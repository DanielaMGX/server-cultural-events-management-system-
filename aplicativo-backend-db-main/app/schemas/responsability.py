from pydantic import BaseModel, Field
from typing import List

class Createresponsability(BaseModel):
    name: str = Field(...)
    description: str = Field(...)

class Updateresponsability(BaseModel):
    name: str = Field(None)
    description: str = Field(None)

class responsabilityDB(Createresponsability):
    id: int = Field(...)

    class Config:
        orm_mode = True

class responsabilityInResponse(BaseModel):
    responsability: responsabilityDB

class ResponsibilitiesInResponse(BaseModel):
    responsibilities: List[responsabilityDB]
