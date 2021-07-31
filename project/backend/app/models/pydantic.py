from datetime import date
from pydantic import BaseModel
from typing import Optional


class TodoSummaryPayloadSchema(BaseModel):
    todo: str
    limit: Optional[date]
    summary: str


class TodoSummaryResponseSchema(TodoSummaryPayloadSchema):
    id: int
