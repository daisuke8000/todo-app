import logging
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from app.api import todo
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.todo"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

    application.include_router(todo.router, prefix="/todos", tags=["todos"])

    return application


app = create_application()

origins = [
    "*",
    "localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
