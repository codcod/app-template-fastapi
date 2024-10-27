# https://fastapi.tiangolo.com/advanced/async-tests/#in-detail

from contextlib import asynccontextmanager

import httpx
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from fastapi import APIRouter, FastAPI
from msc.db import get_connection
from msc.views import routes as api_routes

repo1 = {
    'rowid': 1,
    'name': 'unsecured-small-business-loans',
    'team': 'dl-platinum',
    'org': 'backbase-rnd',
    'layer': 'backend',
    'type': 'flow',
    'lang': 'java',
}

repo8 = {
    'rowid': 8,
    'name': 'financials-spreading',
    'team': 'dl-platinum',
    'org': 'backbase-rnd',
    'layer': 'backend',
    'type': 'journey',
    'lang': 'java',
}

repo9 = {
    'rowid': 9,
    'name': 'unsecured-small-business-loans-ang',
    'team': 'dl-platinum',
    'org': 'backbase-rnd',
    'layer': 'frontend',
    'type': 'flow',
    'lang': 'angular',
}
repo36 = {
    'rowid': 36,
    'name': 'questionnaire',
    'team': 'dl-titane',
    'org': 'backbase-rnd',
    'layer': 'frontend',
    'type': 'journey',
    'lang': 'angular',
}


@pytest_asyncio.fixture
async def app():
    @asynccontextmanager
    async def lifespan(app):
        conn, _ = await get_connection('instance/test.sqlite3')
        app.state.DB = conn
        yield
        await conn.close()

    app = FastAPI(lifespan=lifespan)
    routes = APIRouter()
    app.include_router(api_routes, prefix='/api')
    app.include_router(routes)

    async with LifespanManager(app) as manager:
        yield manager.app


@pytest_asyncio.fixture
async def client(app):
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url='http://test'
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_get_team(client):
    response = await client.get('/api/team')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == ['dl-platinum', 'dl-titane']


@pytest.mark.asyncio
async def test_get_repo_1(client):
    response = await client.get('/api/repo')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == [repo1, repo8, repo9, repo36]


@pytest.mark.asyncio
async def test_get_repo_2(client):
    response = await client.get('/api/repo/search?name=unsecured')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == [repo1, repo9]


@pytest.mark.asyncio
async def test_get_repo_3(client):
    response = await client.get('/api/repo?name=financials-spreading')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == [repo8]


@pytest.mark.asyncio
async def test_get_repo_4(client):
    response = await client.get('/api/repo?name=financials')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == []


@pytest.mark.asyncio
async def test_get_repo_5(client):
    response = await client.get('/api/error')
    assert response.status_code == 404  # noqa: PLR2004
    assert response.json() == {
        'detail': 'Not Found',
    }


@pytest.mark.asyncio
async def test_get_repo_6(client):
    response = await client.get('/api/repo?wrongkey=XX')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == [repo1, repo8, repo9, repo36]
