from datetime import date
from typing import Optional

from pydantic import BaseModel



class CreateSubevent(BaseModel):
    id: str
    applies: bool
    responsability_id: int
    mode_id: int
    space_id: int
    event_id: str


class SubeventDB(CreateSubevent):
    id: Optional[str]
    date_start: Optional[date]
    date_finishing: Optional[date]
    mounting_date: Optional[date]
    mounting_start_hour: Optional[str]
    mounting_finishing_hour: Optional[str]

    class Config:
        from_attributes = True


class UpdateSubevent(BaseModel):
    applies: Optional[bool] = None
    responsability_id: Optional[int] = None
    mode_id: Optional[int] = None
    space_id: Optional[int] = None
    event_id: Optional[str] = None
