from fastapi import FastAPI
from app.api.v1.routes import router
from app.api.v1.user_routes import router as user_router

app = FastAPI(
    title="PinBoard API",
    description="Pinterest-inspired backend API",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")