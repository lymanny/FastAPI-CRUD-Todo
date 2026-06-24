from datetime import datetime

from pydantic import BaseModel
from typing import Optional

from models.models import TaskPriority


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"
    priority: Optional[TaskPriority] = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None


class TodoOut(TodoCreate):
    id: int
    class Config:
        orm_mode = True
