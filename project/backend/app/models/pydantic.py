from pydantic import BaseModel


class TodoSummaryPayloadSchema(BaseModel):
    todo: str


class TodoSummaryResponseSchema(TodoSummaryPayloadSchema):
    id: int
