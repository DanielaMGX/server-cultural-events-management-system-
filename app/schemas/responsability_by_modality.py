from typing import Optional

from pydantic import BaseModel, Field


class CreateresponsabilityByMode(BaseModel):
    applies: bool = Field(...)
    responsability: int = Field(...)
    space: int = Field(...)
    mode: int = Field(...)


class SearchresponsabilityByMode(BaseModel):
    applies: Optional[bool] = Field(None)
    responsability: Optional[int] = Field(None)
    space_id: Optional[int] = Field(None)
    mode_id: Optional[int] = Field(None)


class UpdateresponsabilityByMode(BaseModel):
    applies: Optional[bool] = Field(None)
    responsability: Optional[int] = Field(None)
    space_id: Optional[int] = Field(None)


class ResponsabilityByModeDB(BaseModel):
    applies: bool = Field(...)
    responsability_id: int = Field(...)
    mode_id: int = Field(...)
    space_id: int = Field(...)
    id: int = Field(...)
    responsability__name: Optional[str] = Field(None, alias="responsability_name")
    mode__name: Optional[str] = Field(None, alias="mode_name")
    space__name: Optional[str] = Field(None, alias="space_name")

    class Config:
        from_attributes = True
        populate_by_name = True
