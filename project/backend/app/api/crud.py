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
    summaries = await TodoSummary.all().values()
    return summaries
