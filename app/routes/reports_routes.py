from fastapi import APIRouter
from app.services.report_service import generate_report

router = APIRouter(
    prefix="/api/reports",
    tags=["Reports"]
)

@router.get("/")
def get_report():
    return generate_report()
