from pydantic import BaseModel


class AgentCreateRequest(BaseModel):
    agent_id: str
    name: str
    role: str
    capabilities: list[str]
    endpoint: str | None = None


class SessionPairRequest(BaseModel):
    initiator_id: str
    target_id: str


class TaskCreateRequest(BaseModel):
    name: str
    description: str
    capability: str = "research"
    input_data: dict | None = None
    priority: str = "normal"
