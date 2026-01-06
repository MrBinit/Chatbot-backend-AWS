from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.bedrock_service import generate_reply
from app.core.auth_dependencies import get_current_user

router = APIRouter(prefix="/chat", tags=["Chat"], dependencies= [Depends(get_current_user)])

@router.post("/", response_model=ChatResponse)
async def chat(req: ChatRequest):
    reply = await generate_reply(req.message)
    return {"reply": reply}
