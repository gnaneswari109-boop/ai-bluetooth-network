from datetime import datetime, timedelta
from uuid import uuid4

from app.models.session import SessionRecord
from app.services.discovery_service import AGENTS
from app.services.message_bus import publish_event

SESSIONS = {}


def create_session(initiator_id: str, target_id: str):
    session_id = str(uuid4())
    key = f"session:{session_id}"
    session = SessionRecord(
        id=session_id,
        initiator_id=initiator_id,
        target_id=target_id,
        session_key=key,
        status="active",
        created_at=datetime.utcnow(),
        expires_at=datetime.utcnow() + timedelta(minutes=30),
        trusted=True,
    )
    SESSIONS[session_id] = session
    publish_event("agent.session", {"event": "paired", "session_id": session_id})
    return session


def get_session(session_id: str):
    return SESSIONS.get(session_id)
