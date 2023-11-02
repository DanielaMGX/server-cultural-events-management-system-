
from tortoise import Model, fields

class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    contractual_mode = fields.ForeignKeyField(
        "models.ContractualMode",
        related_name="events",
        null=True
    )
    space = fields.ForeignKeyField(
        "models.Space",
        related_name="events",
        null=True
    )
