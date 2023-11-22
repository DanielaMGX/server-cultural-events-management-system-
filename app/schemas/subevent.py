from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime

class CreateSubevent(BaseModel):
    id: str
    applies: bool
    responsabilityId: int
    modeId: int
    spaceId: int
    eventId: str

class SubeventDB(CreateSubevent):
    id: Optional[str]
    dateStart: Optional[date]
    dateFinishing: Optional[date]
    mountingDate: Optional[date]
    mountingStartHour: Optional[str]
    mountingFinishingHour: Optional[str]

    class Config:
        orm_mode = True

class UpdateSubevent(BaseModel):
    applies: Optional[bool] = None
    responsabilityId: Optional[int] = None
    modeId: Optional[int] = None
    spaceId: Optional[int] = None
    eventId: Optional[str] = None
