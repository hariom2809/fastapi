from pydantic import BaseModel, Field
from typing import Annotated, Optional
from datetime import date
from uuid import UUID

class ListTask(BaseModel):
    id:             UUID
    title:          str
    completed_at:   Optional[date] = None

    model_config = {
        "from_attributes": True
    }

class GetTask(BaseModel):
    id:             UUID
    title:          str
    description:    Optional[str]   = None
    created_at:     date
    completed_at:   Optional[date]  = None

    model_config = {
        "from_attributes": True
    }

class CreateTask(BaseModel):
    title:          Annotated[str, Field(...,min_length=2, max_length=50)]
    description:    Annotated[Optional[str], Field(default=None)]

class UpdateTask(BaseModel):
    description:    Annotated[Optional[str], Field(default=None)]
    completed_at:   Annotated[Optional[date], Field(default=None)]

class ReplaceTask(BaseModel):
    title:          Annotated[str, Field(..., min_length=2, max_length=50)]
    description:    Optional[str] = None
    completed_at:   Optional[date] = None