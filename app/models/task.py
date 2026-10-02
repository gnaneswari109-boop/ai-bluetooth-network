from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

from app.database import Base


class TaskRecord(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    parent_task_id = Column(String, ForeignKey("tasks.id"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(String, default="")
    assigned_to = Column(String, ForeignKey("agents.id"), nullable=True)
    status = Column(String, default="pending")
    priority = Column(String, default="normal")
    dependencies = Column(JSON, default=list)
    input_data = Column(JSON, default=dict)
    output_data = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    agent = relationship("AgentRecord", foreign_keys=[assigned_to])
