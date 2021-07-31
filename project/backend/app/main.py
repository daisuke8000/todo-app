import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from app.api import todo


def create_application() -> FastAPI:
    application = FastAPI()
    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.todo"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

    application.include_router(todo.router)

    return application


app = create_application()
origins = [
    "*",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
