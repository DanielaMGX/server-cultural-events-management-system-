from tortoise import Model, fields

class SubEventState(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    status = fields.CharField(max_length=100)
    subevent = fields.ForeignKeyField("models.SubEvent", related_name="states")
