import asyncio
import logging
import boto3
from app.core.config import settings
from app.core.error import api_error

logger = logging.getLogger(__name__)

brt = boto3.client("bedrock-runtime", region_name=settings.AWS_REGION)

async def generate_reply(message: str) -> str:
    loop = asyncio.get_running_loop()
    try:
        response = await loop.run_in_executor(
            None,
            lambda: brt.converse(
                modelId=settings.MODEL_ID,
                messages=[
                    {
                        "role": "user",
                        "content": [{"text": message}],
                    }
                ],
                inferenceConfig={
                    "maxTokens": settings.MAXTOKEN,
                    "temperature": settings.TEMPERATURE,
                    "topP": settings.TOPP,
                },
            )
        )
        return response["output"]["message"]["content"][0]["text"]
    except Exception as e:
        logger.exception("bedrock inference failed. ")
        api_error(
            status_code=500,
            code="BEDROCK_INFERENCE_FAILED",
            message="Failed to generate response from model",
        )
