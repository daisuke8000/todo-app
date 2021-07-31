from app.models.pydantic import TodoSummaryPayloadSchema
from app.models.tortoise import TodoSummary


async def post(payload: TodoSummaryPayloadSchema) -> int:
    todo_summary = TodoSummary(
        todo=payload.todo,
        limit=payload.limit,
        summary=payload.summary,
    )
    await todo_summary.save()
    return todo_summary.id
