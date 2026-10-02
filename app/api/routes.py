from fastapi import APIRouter
from app.services.discovery_service import register_agent, list_agents, find_agents_by_capability
from app.services.session_service import create_session
from app.services.task_service import create_task, assign_task, complete_task, get_task
from app.services.context_service import get_context, update_context
from app.api.schemas import AgentCreateRequest, SessionPairRequest, TaskCreateRequest

router = APIRouter()


@router.post("/register")
async def register_agent_api(payload: AgentCreateRequest):
    agent = {
        "agent_id": payload.agent_id,
        "name": payload.name,
        "role": payload.role,
        "capabilities": payload.capabilities,
        "endpoint": payload.endpoint,
        "status": "online",
    }
    register_agent(agent)
    return {"status": "registered", "agent": agent}


@router.get("/")
async def list_agents_api():
    return {"agents": list_agents()}


@router.get("/capabilities/{capability}")
async def capability_lookup(capability: str):
    return {"matches": find_agents_by_capability(capability)}


@router.post("/pair")
async def create_session_api(payload: SessionPairRequest):
    session = create_session(payload.initiator_id, payload.target_id)
    return {"status": "paired", "session": session}


@router.post("/task/create")
async def create_task_api(payload: TaskCreateRequest):
    task = create_task(payload.name, payload.description, payload.input_data, payload.priority)
    assigned = assign_task(task["task_id"], payload.capability)
    return {"task": task, "assigned": assigned}


@router.get("/task/{task_id}")
async def get_task_api(task_id: str):
    return {"task": get_task(task_id)}


@router.get("/context/{task_id}")
async def get_context_api(task_id: str):
    return {"context": get_context(task_id)}


@router.post("/context/{task_id}")
async def update_context_api(task_id: str, updated_by: str, payload: dict):
    return {"context": update_context(task_id, updated_by, payload)}
