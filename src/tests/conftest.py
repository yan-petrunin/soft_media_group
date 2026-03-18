from unittest.mock import AsyncMock
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from src.app.main import app

@pytest_asyncio.fixture(scope="module")
def mock_session():
    return AsyncMock()

@pytest_asyncio.fixture(scope="module")
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client