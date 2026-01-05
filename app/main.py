from fastapi import FastAPI
from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router
from app.core.logger import setup_logger

setup_logger()

app = FastAPI(title="Bedrock Chat API")

app.include_router(health_router, prefix= "/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(chat_router, prefix="/api/v1")