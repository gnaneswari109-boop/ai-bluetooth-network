from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root_api():
    return {"message": "AI Mesh MVP is running"}
