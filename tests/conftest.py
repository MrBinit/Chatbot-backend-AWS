import pytest
from httpx import AsyncClient
from app.main import app

# async lets the test client run inside the same async event loop as FastAPI.
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
