from datetime import datetime

CONTEXTS = {}


def get_context(task_id: str):
    if task_id not in CONTEXTS:
        CONTEXTS[task_id] = {"version": 0, "data": {}}
    return CONTEXTS[task_id]


def update_context(task_id: str, updated_by: str, payload: dict):
    context = get_context(task_id)
    context["data"].update(payload)
    context["version"] += 1
    context["updated_by"] = updated_by
    context["updated_at"] = datetime.utcnow().isoformat()
    return context
