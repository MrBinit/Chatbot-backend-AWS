from fastapi import APIRouter, status
from app.schemas.auth import TokenReqest, LoginRequest
from app.core.config import settings
from app.core.error import api_error
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenReqest)
def login(payload: LoginRequest):
    if (
        payload.username != settings.AUTH_USERNAME or
        payload.password != settings.AUTH_PASSWORD
    ):
        api_error(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code="INVALID_CREDENTIALS",
            message="Invalid username or password",
        )
    token = create_access_token({"sub": payload.username})
    return {"access_token": token, "token_type": "bearer"}
