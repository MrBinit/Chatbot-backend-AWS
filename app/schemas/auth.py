from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenReqest(BaseModel):
    access_token: str
    token_type: str = "bearer"