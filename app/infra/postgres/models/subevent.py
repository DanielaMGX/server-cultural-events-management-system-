
from tortoise import Model, fields

class SubEvent(Model):
    id = fields.IntField(pk=True)
    applies = fields.BooleanField()
    responsability = fields.ForeignKeyField(
        "models.Responsability",
        related_name="subevents"
    )
    mode = fields.ForeignKeyField(
        "models.ContractualMode",
        related_name="subevents"
    )
    space = fields.ForeignKeyField(
        "models.Space",
        related_name="subevents"
    )
    event = fields.ForeignKeyField(
        "models.Event",
        related_name="subevents",
        null=True
    )
