from fastapi import APIRouter
from app.services.crop_service import recommend_crop

router = APIRouter(prefix="/api/crop", tags=["Crop"])

@router.post("/recommend")
def crop_recommendation(payload: dict):
    return recommend_crop(payload)


