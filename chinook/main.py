from random import random

import uvicorn
import time
import string
from dotenv import load_dotenv
import os
from controller import apis
from chinook.db.prisma import prisma
import logging
from os import path
from fastapi import FastAPI, Request, Response
from fastapi.middleware.gzip import GZipMiddleware

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
print(f'log_file_path: {log_file_path}')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger(__name__)


app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix="/controller")


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


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
#     logger.info(f"rid={idem} start request path={request.url.path}")
#     start_time = time.time()
#
#     response = await call_next(request)
#
#     process_time = (time.time() - start_time) * 1000
#     formatted_process_time = '{0:.2f}'.format(process_time)
#     logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
#
#     return response


if __name__ == "__main__":
    load_dotenv()
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="localhost", port=port, reload=True)
