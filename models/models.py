import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from database.database import Base
from datetime import datetime


class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TodoItem(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, index=True)

    priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM, nullable=False)
    due_date = Column(DateTime, nullable=True)