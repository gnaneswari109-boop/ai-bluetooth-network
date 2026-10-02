from fastapi import APIRouter
from pydantic import BaseModel

from app.services.session_service import create_session, get_session

router = APIRouter()


class SessionPairRequest(BaseModel):
    initiator_id: str
    target_id: str


@router.post("/pair")
async def pair_api(payload: SessionPairRequest):
    session = create_session(payload.initiator_id, payload.target_id)
    return {"status": "paired", "session": session}


@router.get("/{session_id}")
async def get_session_api(session_id: str):
    return {"session": get_session(session_id)}
