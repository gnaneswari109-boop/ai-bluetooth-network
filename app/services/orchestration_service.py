from app.services.discovery_service import find_agents_by_capability
from app.services.task_service import TASKS


def build_subtasks(task: dict):
    return [
        {
            "task_id": task["task_id"] + "-research",
            "parent_task_id": task["task_id"],
            "name": task["name"] + " - research",
            "capability": "research",
            "status": "pending",
        },
        {
            "task_id": task["task_id"] + "-code",
            "parent_task_id": task["task_id"],
            "name": task["name"] + " - implementation",
            "capability": "code",
            "status": "pending",
        },
        {
            "task_id": task["task_id"] + "-summary",
            "parent_task_id": task["task_id"],
            "name": task["name"] + " - summary",
            "capability": "summary",
            "status": "pending",
        },
    ]


def assign_subtasks(task: dict):
    subtasks = []
    for subtask in build_subtasks(task):
        matches = find_agents_by_capability(subtask["capability"])
        if matches:
            subtask["assigned_to"] = matches[0]["agent_id"]
            subtask["status"] = "assigned"
        else:
            subtask["status"] = "failed"
        subtasks.append(subtask)
    return subtasks
