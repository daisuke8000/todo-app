import os


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.todo", "aerich.models"],
            "default_connection": "default",
        },
    },
}