from fastapi import APIRouter
from app.services.irrigation_service import calculate_irrigation

router = APIRouter(
    prefix="/api/irrigation",
    tags=["Irrigation"]
)

@router.post("/")
def irrigation_decision(payload: dict):
    return calculate_irrigation(payload)


