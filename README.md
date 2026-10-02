# AI Mesh MVP

This project is a minimal Python prototype for a Bluetooth-like AI mesh.

## Features
- Agent registration and discovery
- Session pairing across agents
- Task creation and delegation
- Shared context memory
- Parallel-style execution using a task broker
- Redis-backed event bus

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example flow

1. Register two agents
2. Create a task with a capability such as `research`
3. Retrieve assigned task and update context
4. Complete the task and inspect output
