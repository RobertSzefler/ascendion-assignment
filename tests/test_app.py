from unittest.mock import AsyncMock

import pytest
from httpx import ASGITransport, AsyncClient

from app import app
from db import get_session


mock_get_session = AsyncMock()
app.dependency_overrides[get_session] = mock_get_session


@pytest.mark.asyncio
async def test_get_by_salary():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/employees_by_salary")
    assert response.status_code == 422
    # TODO expand tests
