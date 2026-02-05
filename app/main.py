from fastapi import FastAPI

from app.routes.crops_routes import router as crop_router
from app.routes.auth_routes import router as auth_router
from app.routes.weather_routes import router as weather_router
from app.routes.irrigation_routes import router as irrigation_router
from app.routes.reports_routes import router as reports_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.settings_routes import router as settings_router

app = FastAPI(title="FarmBuddy Backend")

app.include_router(auth_router)
app.include_router(crop_router)
app.include_router(weather_router)
app.include_router(irrigation_router)
app.include_router(reports_router)
app.include_router(dashboard_router)
app.include_router(settings_router)

@app.get("/")
def root():
    return {"status": "FarmBuddy backend running successfully"}

