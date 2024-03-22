from pydantic import BaseModel, Field


class CreateResponsability(BaseModel):
    name: str = Field(...)
    description: str = Field(...)


class UpdateResponsability(BaseModel):
    name: str = Field(None)
    description: str = Field(None)


class ResponsabilityDB(CreateResponsability):
    id: int = Field(...)

    class Config:
        from_attributes = True
