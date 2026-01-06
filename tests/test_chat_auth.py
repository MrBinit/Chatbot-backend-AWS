import pytest
from unittest.mock import patch, AsyncMock
#made some new changes in this based on the experiences
#new changes
@pytest.mark.asyncio
async def test_chat_requires_auth(client):
    response = await client.post(
        "/api/v1/chat/",
        json={"message": "hello"},
    )
    assert response.status_code == 401
@pytest.mark.asyncio
async def test_chat_with_valid_token(client):
    login = await client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "admin123"},
    )

    token = login.json()["access_token"]

    with patch(
        "app.api.v1.chat.generate_reply",
        new_callable=AsyncMock,
        return_value="mocked response",
    ):
        response = await client.post(
            "/api/v1/chat/",
            headers={"Authorization": f"Bearer {token}"},
            json={"message": "hello"},
        )

    assert response.status_code == 200
    assert response.json()["reply"] == "mocked response"
