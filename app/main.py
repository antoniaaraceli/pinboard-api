from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(
    title="PinBoard API",
    description="A Pinterest-inspired backend API",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")