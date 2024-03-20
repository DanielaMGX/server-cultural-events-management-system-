from typing import Optional

from pydantic import BaseModel, EmailStr


class CreateEvent(BaseModel):
    event_type_id: int
    general_name: str
    specific_name: Optional[str]
    date_start: str
    date_finishing: str
    hour_start: str
    hour_finishing: str
    place: Optional[str]
    user_name: str
    phone: Optional[str]
    identification_type: str
    identification_value: str
    email: Optional[EmailStr]
    description: Optional[str]
    observation: Optional[str]
    duration: Optional[str]
    mounting_date: Optional[str]
    mounting_start_hour: Optional[str]
    mounting_finishing_hour: Optional[str]
    technic_contact: Optional[str]
    rider: Optional[str]
    min_to_min: Optional[str]
    communication_contact: Optional[str]
    pulep: Optional[str]
    access_data: Optional[str]
    ticket_company: Optional[str]
    age_restriction: Optional[str]
    agreement: Optional[str]


class EventDB(CreateEvent):
    id: int

    class Config:
        from_attributes = True


class UpdateEvent(BaseModel):
    event_type_id: Optional[str] = None
    state: Optional[str] = None
    date_state: Optional[str] = None
    general_name: Optional[str] = None
    specific_name: Optional[str] = None
    date_start: Optional[str] = None
    date_finishing: Optional[str] = None
    hour_start: Optional[str] = None
    hour_finishing: Optional[str] = None
    place: Optional[str] = None
    user_name: Optional[str] = None
    phone: Optional[str] = None
    identification_type: Optional[str] = None
    identification_value: Optional[str] = None
    email: Optional[EmailStr] = None
    description: Optional[str] = None
    observation: Optional[str] = None
    duration: Optional[str] = None
    mounting_date: Optional[str] = None
    mounting_start_hour: Optional[str] = None
    mounting_finishing_hour: Optional[str] = None
    technic_contact: Optional[str] = None
    rider: Optional[str] = None
    min_tomin: Optional[str] = None
    communication_contact: Optional[str] = None
    pulep: Optional[str] = None
    access_data: Optional[str] = None
    ticket_company: Optional[str] = None
    age_restriction: Optional[str] = None
    agreement: Optional[str] = None
