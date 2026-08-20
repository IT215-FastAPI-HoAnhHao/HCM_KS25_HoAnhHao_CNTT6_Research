from datetime import datetime

from pydantic import BaseModel, Field


class ResearchTaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)

    description: str | None = None
    due_date: datetime | None = None

    priority: str = Field(default="MEDIUM", max_length=20)


class ResearchTaskCreate(ResearchTaskBase):
    assignee_id: int | None = None


class ResearchTaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)

    description: str | None = None
    assignee_id: int | None = None

    status: str | None = Field(default=None, max_length=20)

    priority: str | None = Field(default=None, max_length=20)

    due_date: datetime | None = None


class ResearchTaskResponse(ResearchTaskBase):
    id: int
    project_id: int
    assignee_id: int | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
