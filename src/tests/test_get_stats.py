import pytest
from unittest.mock import MagicMock, patch
from fastapi import status

@pytest.mark.asyncio
async def test_get_stats(client):
    mock_link = MagicMock()
    mock_link.count = 42

    with patch("src.app.routers.stats.get_original_url", return_value=mock_link):
        response = await client.get("/stats/abc12345")

    assert response.status_code == 200
    assert response.json()["count"] == 42

@pytest.mark.asyncio
async def test_get_stats_not_found(client):
    with patch("src.app.routers.stats.get_original_url", return_value=None):
        response = await client.get("/stats/notexist")

    assert response.status_code == status.HTTP_404_NOT_FOUND