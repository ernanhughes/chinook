import logging.config
import os
from os import path

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from controller import apis
from db.prisma import prisma

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
print(f'log_file_path: {log_file_path}')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    await prisma.connect()
    logger.info("Application started")


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
    logger.info("Application shutdown")


@app.get("/")
def read_root():
    return {"version": "1.0.0"}


if __name__ == "__main__":
    load_dotenv()
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run("main:app", host="localhost", port=port, reload=True)
