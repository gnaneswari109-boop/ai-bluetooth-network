from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Integer
from uuid import uuid4
from datetime import datetime

from app.database import Base


class ContextRecord(Base):
    __tablename__ = "contexts"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    task_id = Column(String, ForeignKey("tasks.id"), nullable=False)
    scope = Column(String, default="task")
    version = Column(Integer, default=0)
    data = Column(JSON, default=dict)
    updated_by = Column(String, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow)
