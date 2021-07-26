from tortoise import fields, models


class TodoSummary(models.Model):
    id = fields.IntField(pk=True)
    todo = fields.CharField(null=False, max_length=10)
    limit = fields.DateField(auto_now_add=False)
    summary = fields.TextField(null=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.id
