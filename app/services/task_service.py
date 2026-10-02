from datetime import datetime
from uuid import uuid4

TASKS = {}


def create_task(name: str, description: str, input_data: dict | None = None, priority: str = "normal"):
    task_id = str(uuid4())
    task = {
        "task_id": task_id,
        "name": name,
        "description": description,
        "input_data": input_data or {},
        "priority": priority,
        "status": "queued",
        "assigned_to": None,
        "created_at": datetime.utcnow().isoformat(),
    }
    TASKS[task_id] = task
    return task


def assign_task(task_id: str, capability: str):
    from app.services.discovery_service import find_agents_by_capability

    task = TASKS[task_id]
    matches = find_agents_by_capability(capability)
    if not matches:
        raise ValueError("No matching agent found")

    selected = matches[0]
    task["assigned_to"] = selected["agent_id"]
    task["status"] = "assigned"
    return task


def complete_task(task_id: str, output_data: dict):
    task = TASKS[task_id]
    task["status"] = "completed"
    task["output_data"] = output_data
    return task


def get_task(task_id: str):
    return TASKS.get(task_id)
