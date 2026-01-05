# It extracts the JWT from the request, verifies it, and blocks the request if the token is invalid or expired.
from fastapi import Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import verify_access_token
from app.core.error import api_error

security = HTTPBearer(auto_error=False)

def get_current_user(
    creds: HTTPAuthorizationCredentials | None = Depends(security),
):
    if creds is None or not creds.credentials:
        api_error(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code="MISSING_TOKEN",
            message="Authorization token is required",
        )

    payload = verify_access_token(creds.credentials)
    if not payload:
        api_error(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code="INVALID_OR_EXPIRED_TOKEN",
            message="Token is invalid or expired",
        )

    return payload
