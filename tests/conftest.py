import asyncio
import logging

import pytest
from dotenv import load_dotenv
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.middleware.gzip import GZipMiddleware

from chinook.controller import apis
from chinook.db.prisma import prisma

load_dotenv()
app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix="/api/v1")
logger = logging.getLogger(__name__)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        print("Client is ready")
        await prisma.connect()
        yield async_client
