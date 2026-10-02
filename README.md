# AI Mesh MVP

A minimal multi-agent AI mesh prototype inspired by Bluetooth discovery and pairing.

## Features
- Agent registry and capability discovery
- Session pairing between agents
- Task creation and assignment
- Shared context memory
- Multi-agent orchestration via subtasks
- Redis event bus support

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example workflow

1. Register agents
2. Create task
3. Assign to matching capability
4. Update shared context
5. Complete task
