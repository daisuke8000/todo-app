from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import TodoSummaryPayloadSchema, TodoSummaryResponseSchema


router = APIRouter()

todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]

# @router.post("/", response_model=TodoSummaryResponseSchema, tags=["root"], status_code=201)
# async def read_root(payload: TodoSummaryPayloadSchema) -> TodoSummaryResponseSchema:
#     todo_id = await crud.post(payload)
#     response_object = {
#         "id": todo_id,
#         "todo": payload.text,
#         "limit": payload.date,
#         "summary": payload.summary,
#     }
#     return response_object



@router.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@router.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return { "data": todos }


@router.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": { "Todo added." }
    }


@router.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


@router.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }
