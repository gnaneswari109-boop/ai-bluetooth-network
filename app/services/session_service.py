from datetime import datetime, timedelta
from uuid import uuid4

SESSIONS = {}


def create_session(initiator_id: str, target_id: str):
    session_id = str(uuid4())
    session = {
        "session_id": session_id,
        "initiator_id": initiator_id,
        "target_id": target_id,
        "session_key": f"session:{session_id}",
        "status": "active",
        "trusted": True,
        "created_at": datetime.utcnow().isoformat(),
        "expires_at": (datetime.utcnow() + timedelta(minutes=30)).isoformat(),
    }
    SESSIONS[session_id] = session
    return session


def get_session(session_id: str):
    return SESSIONS.get(session_id)
