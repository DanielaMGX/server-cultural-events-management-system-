from pydantic import BaseModel, Field


class Createresponsability(BaseModel):
    name: str = Field(...)
    description: str = Field(...)


class Updateresponsability(BaseModel):
    name: str = Field(None)
    description: str = Field(None)


class responsabilityDB(Createresponsability):
    id: int = Field(...)

    class Config:
        from_attributes = True
