from app.models.pydantic import TodoSummaryPayloadSchema
from app.models.todo import TodoSummary
from typing import Union, List


async def post(payload: TodoSummaryPayloadSchema) -> int:
    todo_summary = TodoSummary(
        todo=payload.todo
    )
    await todo_summary.save()
    return todo_summary.id


async def get_all() -> List:
    todos = await TodoSummary.all().values()
    return todos


async def get(id: int) -> Union[dict, None]:
    task = await TodoSummary.filter(id=id).first().values()
    if task:
        return task[0]
    return None


async def put(id: int, payload: TodoSummaryPayloadSchema) -> Union[dict, None]:
    task = await TodoSummary.filter(id=id).update(
        todo=payload.todo
    )
    if task:
        update_task = await TodoSummary.filter(id=id).first().values()
        return update_task[0]
    return None


async def delete(id: int) -> int:
    task = await TodoSummary.filter(id=id).first().delete()
    return task
