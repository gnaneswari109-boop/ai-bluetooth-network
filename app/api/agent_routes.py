from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from app.models.agent import AgentRecord
from app.services.discovery_service import AGENTS, register_agent, list_agents, find_agents_by_capability

router = APIRouter()


class AgentCreateRequest(BaseModel):
    name: str
    role: str
    capabilities: list[str]
    endpoint: str | None = None
    metadata: dict | None = None


@router.post("/register")
async def register_agent_api(payload: AgentCreateRequest):
    agent_id = str(uuid4())
    record = AgentRecord(
        id=agent_id,
        name=payload.name,
        role=payload.role,
        capabilities=payload.capabilities,
        endpoint=payload.endpoint,
        status="online",
        metadata=payload.metadata or {},
    )
    register_agent(record)
    return {"agent_id": agent_id, "status": "registered"}


@router.get("/")
async def list_agents_api():
    return {"agents": list_agents()}


@router.get("/capabilities/{capability}")
async def find_agents_by_capability_api(capability: str):
    return {"matches": find_agents_by_capability(capability)}
