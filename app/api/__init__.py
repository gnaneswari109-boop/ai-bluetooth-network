from app.api.agent_routes import router as agent_router
from app.api.task_routes import router as task_router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(agent_router, prefix="/agents")
api_router.include_router(task_router, prefix="/tasks")

router = api_router
