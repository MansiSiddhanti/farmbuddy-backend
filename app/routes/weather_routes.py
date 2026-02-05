from fastapi import APIRouter
from app.services.weather_service import get_weather

router = APIRouter(prefix="/api/weather", tags=["Weather"])

@router.get("/")
def fetch_weather():
    # Pune default coordinates
    return get_weather(lat=18.5, lon=73.8)
