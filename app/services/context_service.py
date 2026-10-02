from datetime import datetime
from typing import Dict
from uuid import uuid4

from app.models.task import TaskRecord
from app.services.discovery_service import find_agents_by_capability
from app.services.message_bus import publish_event

TASKS: Dict[str, TaskRecord] = {}


def create_task(name: str, description: str, input_data: dict = None, priority: str = "normal") -> TaskRecord:
    task = TaskRecord(
        id=str(uuid4()),
        name=name,
        description=description,
        input_data=input_data or {},
        priority=priority,
        status="queued",
        created_at=datetime.utcnow(),
    )
    TASKS[task.id] = task
    publish_event("agent.task", {"event": "created", "task_id": task.id, "name": name})
    return task


def assign_task(task_id: str, capability: str):
    task = TASKS.get(task_id)
    if not task:
        raise ValueError("Task not found")
    matches = find_agents_by_capability(capability)
    if not matches:
        raise ValueError("No suitable agent found")
    selected = matches[0]
    task.assigned_to = selected["agent_id"]
    task.status = "assigned"
    task.started_at = datetime.utcnow()
    publish_event("agent.task", {"event": "assigned", "task_id": task_id, "agent_id": selected["agent_id"]})
    return task


def complete_task(task_id: str, output_data: dict):
    task = TASKS.get(task_id)
    if not task:
        raise ValueError("Task not found")
    task.status = "completed"
    task.output_data = output_data
    task.completed_at = datetime.utcnow()
    publish_event("agent.task", {"event": "completed", "task_id": task_id})
    return task
