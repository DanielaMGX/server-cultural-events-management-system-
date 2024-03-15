from tortoise import Model, fields


class SubEventHasResponsability(Model):
    state = fields.CharField(max_length=255)
    deliverable = fields.CharField(max_length=255, null=True)
    responsability = fields.ForeignKeyField("models.Responsability")
    sub_event = fields.ForeignKeyField("models.SubEvent")
