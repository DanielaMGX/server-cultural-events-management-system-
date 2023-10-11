from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class CreateresponsabilityByMode(BaseModel):
    applies: bool = Field(...)
    responsability: int = Field(...)
    space: int = Field(...)
    mode:  int = Field(...)


class SearchresponsabilityByMode(BaseModel):
    applies: Optional[bool] = Field(None)
    responsability: Optional[int] = Field(None)
    space_id: Optional[int] = Field(None)
    mode_id: Optional[int] = Field(None)

class UpdateresponsabilityByMode(BaseModel):
    applies: Optional[bool] = Field(None)
    responsability: Optional[int] = Field(None)
    space_id: Optional[int] = Field(None)


class responsabilityByModeDB(BaseModel):
    applies: bool = Field(...)
    responsability_id: int = Field(...)
    mode_id: int = Field(...)
    space_id: int = Field(...)
    id: int = Field(...)
    responsability_name: Optional[str] = Field(None)  
    mode_name: Optional[str] = Field(None)  
    space_name: Optional[str] = Field(None)  

    class Config:
        orm_mode = True

class responsabilityByModeInResponse(BaseModel):
    responsability_by_mode: responsabilityByModeDB


class ResponsibilitiesByModeInResponse(BaseModel):
    responsibilities_by_mode: List[responsabilityByModeDB]
