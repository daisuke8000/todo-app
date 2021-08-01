from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TodoSummary(models.Model):
    todo = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.todo


TodoSummarySchema = pydantic_model_creator(TodoSummary)
