from tortoise import Model, fields


class EventHasResponsability(Model):
    state = fields.CharField(max_length=255)
    deliverable = fields.CharField(max_length=255, null=True)
    responsability = fields.ForeignKeyField("models.Responsability")
    event = fields.ForeignKeyField("models.Event")
