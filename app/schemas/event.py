from typing import Optional
from datetime import date,datetime
from pydantic import BaseModel, EmailStr, Field

class CreateEvent(BaseModel):
    id: str
    eventType: Optional[str]
    state: str
    dateState: Optional[str]
    generalName: str
    specificName: Optional[str]
    dateStart: str
    dateFinishing: str
    hourStart: str
    hourFinishing: str
    place: Optional[str]
    userName: str
    phone: Optional[str]
    identificationType: str
    identificationValue: str
    email: Optional[EmailStr]
    description: Optional[str]
    observation: Optional[str]
    duration: Optional[str]
    mountingDate: Optional[str]
    mountingStartHour: Optional[str]
    mountingFinishingHour: Optional[str]
    technicContact: Optional[str]
    rider: Optional[str]
    minTomin: Optional[str]
    communicationContact: Optional[str]
    pulep: Optional[str]
    accessData: Optional[str]
    ticketCompany: Optional[str]
    ageRestriction: Optional[str]
    agreement: Optional[str]



class EventDB(BaseModel):
    id: Optional[str]
    event_type: Optional[str]
    state: Optional[str]
    date_state: Optional[datetime]
    general_name: Optional[str]
    specific_name: Optional[str]
    date_start: Optional[date]
    date_finishing: Optional[date]
    hour_start: Optional[str]
    hour_finishing: Optional[str]
    place: Optional[str]
    user_name: Optional[str]
    phone: Optional[str]
    identification_type: Optional[str]
    identification_value: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]
    observation: Optional[str]
    duration: Optional[str]
    mounting_date: Optional[date]
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

    class Config:
        orm_mode = True

class UpdateEvent(BaseModel):
    event_type: Optional[str] = None
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
    min_to_min: Optional[str] = None
    communication_contact: Optional[str] = None
    pulep: Optional[str] = None
    access_data: Optional[str] = None
    ticket_company: Optional[str] = None
    age_restriction: Optional[str] = None
    agreement: Optional[str] = None
