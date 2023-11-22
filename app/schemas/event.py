from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime

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

class EventDB(CreateEvent):
    id: Optional[str]
    dateState: Optional[datetime]
    dateStart: Optional[date]
    dateFinishing: Optional[date]
    mountingDate: Optional[date]
    mountingStartHour: Optional[str]
    mountingFinishingHour: Optional[str]

    class Config:
        orm_mode = True

class UpdateEvent(BaseModel):
    eventType: Optional[str] = None
    state: Optional[str] = None
    dateState: Optional[str] = None
    generalName: Optional[str] = None
    specificName: Optional[str] = None
    dateStart: Optional[str] = None
    dateFinishing: Optional[str] = None
    hourStart: Optional[str] = None
    hourFinishing: Optional[str] = None
    place: Optional[str] = None
    userName: Optional[str] = None
    phone: Optional[str] = None
    identificationType: Optional[str] = None
    identificationValue: Optional[str] = None
    email: Optional[EmailStr] = None
    description: Optional[str] = None
    observation: Optional[str] = None
    duration: Optional[str] = None
    mountingDate: Optional[str] = None
    mountingStartHour: Optional[str] = None
    mountingFinishingHour: Optional[str] = None
    technicContact: Optional[str] = None
    rider: Optional[str] = None
    minTomin: Optional[str] = None
    communicationContact: Optional[str] = None
    pulep: Optional[str] = None
    accessData: Optional[str] = None
    ticketCompany: Optional[str] = None
    ageRestriction: Optional[str] = None
    agreement: Optional[str] = None
