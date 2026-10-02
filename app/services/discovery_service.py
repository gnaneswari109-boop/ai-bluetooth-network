from typing import Dict, List, Optional
from uuid import uuid4

from app.models.agent import AgentRecord
from app.services.message_bus import publish_event

AGENTS: Dict[str, AgentRecord] = {}


def register_agent(record: AgentRecord):
    AGENTS[record.id] = record
    publish_event("agent.discovery", {"event": "register", "agent_id": record.id})
    return record


def list_agents() -> List[dict]:
    return [
        {
            "agent_id": agent.id,
            "name": agent.name,
            "role": agent.role,
            "capabilities": agent.capabilities,
            "status": agent.status,
            "endpoint": agent.endpoint,
        }
        for agent in AGENTS.values()
    ]


def find_agents_by_capability(capability: str) -> List[dict]:
    matches = []
    for agent in AGENTS.values():
        if capability in (agent.capabilities or []):
            matches.append({
                "agent_id": agent.id,
                "name": agent.name,
                "role": agent.role,
                "capabilities": agent.capabilities,
            })
    return matches
