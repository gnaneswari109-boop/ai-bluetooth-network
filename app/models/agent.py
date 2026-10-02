from sqlalchemy import Column, String, DateTime, JSON, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

from app.database import Base


class AgentRecord(Base):
    __tablename__ = "agents"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    capabilities = Column(JSON, default=list)
    endpoint = Column(String, nullable=True)
    status = Column(String, default="online")
    public_key = Column(String, nullable=True)
    heartbeat = Column(DateTime, default=datetime.utcnow)
    metadata = Column(JSON, default=dict)

    sessions = relationship("SessionRecord", foreign_keys="SessionRecord.initiator_id")
    tasks = relationship("TaskRecord", foreign_keys="TaskRecord.assigned_to")
