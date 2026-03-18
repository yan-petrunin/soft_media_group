import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from httpx import AsyncClient, ASGITransport
from fastapi import status
from src.app.main import app

@pytest.mark.asyncio
async def test_create_short_link(client):
    mock_link = MagicMock()
    mock_link.short_id = "abc12345"

    with patch("src.app.routers.shorten.insert_short_link", return_value=mock_link), \
         patch("src.app.routers.shorten.generate_short_id", return_value="abc12345"):

        response = await client.post("/shorten", json={"link": "https://vk.com"})

    assert response.status_code == 200
    assert response.json()["short_link"] == "abc12345"

@pytest.mark.asyncio
async def test_create_short_link_adds_https(client):
    mock_link = MagicMock()
    mock_link.short_id = "abc12345"

    with patch("src.app.routers.shorten.insert_short_link", return_value=mock_link) as mock_insert, \
         patch("src.app.routers.shorten.generate_short_id", return_value="abc12345"):

        await client.post("/shorten", json={"link": "vk.com"})

    call_args = mock_insert.call_args[0]
    assert call_args[1].startswith("https://")