from typing import List
from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.todo import TodoSummarySchema
from app.models.pydantic import TodoSummaryPayloadSchema, TodoSummaryResponseSchema


router = APIRouter()


@router.post("/", response_model=TodoSummaryResponseSchema, status_code=201)
async def read_root(payload: TodoSummaryPayloadSchema) -> TodoSummaryResponseSchema:
    todo_id = await crud.post(payload)
    response_object = {
        "id": todo_id,
        "todo": payload.todo,
    }
    return response_object


@router.get("/", response_model=List[TodoSummarySchema])
async def read_all() -> List[TodoSummarySchema]:
    return await crud.get_all()
