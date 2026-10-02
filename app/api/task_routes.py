from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from app.services.context_service import get_context, update_context
from app.services.session_service import create_session
from app.services.task_service import create_task, assign_task, complete_task

router = APIRouter()


class TaskCreateModel(BaseModel):
    name: str
    description: str
    capability: str = "research"
    input_data: dict | None = None
    priority: str = "normal"


@router.post("/create")
async def create_task_api(payload: TaskCreateModel):
    task = create_task(payload.name, payload.description, payload.input_data or {}, payload.priority)
    assigned = assign_task(task.id, payload.capability)
    return {"task_id": task.id, "status": assigned.status, "assigned_to": assigned.assigned_to}


@router.post("/complete")
async def complete_task_api(task_id: str, output_data: dict):
    task = complete_task(task_id, output_data)
    return {"task_id": task_id, "status": task.status, "output": task.output_data}


@router.get("/context/{task_id}")
async def get_context_api(task_id: str):
    return get_context(task_id)


@router.post("/context/{task_id}")
async def update_context_api(task_id: str, updated_by: str, payload: dict):
    return update_context(task_id, updated_by, payload)


@router.post("/pair")
async def create_session_api(initiator_id: str, target_id: str):
    session = create_session(initiator_id, target_id)
    return {"session_id": session.id, "status": session.status}
