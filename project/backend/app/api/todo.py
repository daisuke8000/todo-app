from typing import List
from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.models.todo import TodoSummarySchema
from app.models.pydantic import TodoSummaryPayloadSchema, TodoSummaryResponseSchema


router = APIRouter()


@router.post("/", response_model=TodoSummaryResponseSchema, status_code=201)
async def post_todo(payload: TodoSummaryPayloadSchema) -> TodoSummaryResponseSchema:
    todo_id = await crud.post(payload)
    response_object = {
        "id": todo_id,
        "todo": payload.todo,
    }
    return response_object


@router.get("/", response_model=List[TodoSummarySchema])
async def read_all_todo() -> List[TodoSummarySchema]:
    return await crud.get_all()


@router.put("/{id}/", response_model=TodoSummarySchema)
async def update_todo(payload: TodoSummaryPayloadSchema, id: int = Path(..., gt=0)) -> TodoSummarySchema:
    todo = await crud.put(id, payload)
    if not todo:
        raise HTTPException(status_code=404,detail="Todos not found")
    return todo


@router.delete("/{id}/", response_model=TodoSummaryResponseSchema)
async def delete_todo(id: int = Path(..., gt=0)) -> TodoSummaryResponseSchema:
    todo = await crud.get(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todos not found")
    await crud.delete(id)
    return todo
