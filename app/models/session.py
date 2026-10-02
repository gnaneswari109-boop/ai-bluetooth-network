from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

from app.database import Base


class SessionRecord(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    initiator_id = Column(String, ForeignKey("agents.id"), nullable=False)
    target_id = Column(String, ForeignKey("agents.id"), nullable=False)
    session_key = Column(String, nullable=False)
    status = Column(String, default="active")
    trusted = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)

    initiator = relationship("AgentRecord", foreign_keys=[initiator_id])
    target = relationship("AgentRecord", foreign_keys=[target_id])
