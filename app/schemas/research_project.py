from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class ResearchProjectBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)

    description: str | None = None

class ResearchProjectCreate(ResearchProjectBase):
    pass

class ResearchProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)

    description: str | None = None


class ResearchProjectResponse(ResearchProjectBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True



class ResearchMemberBase(BaseModel):
    user_id : int

    role: str = Field(default="MEMBER", max_length=20)


class ResearchMemberCreate(ResearchMemberBase):
    pass 

class ResearchMemberUpdate(BaseModel):
    role: str | None = Field(default=None, max_length=20)


class ResearchMemberResponse(ResearchMemberBase):
    project_id: int
    joined_at: datetime

    class Config:
        from_attributes = True


