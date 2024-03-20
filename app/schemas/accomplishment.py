from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CreateAccomplishment(BaseModel):
    ...


class UpdateAccomplishment(BaseModel):
    file_url: Optional[str] = Field(None)
    text: Optional[str] = Field(None)
    check: Optional[bool] = Field(None)


class AccomplishmentDB(BaseModel):
    id: int
    date: datetime
    file_url: Optional[str] = Field(None)
    text: Optional[str] = Field(None)
    check: bool

    class Config:
        from_attributes = True
