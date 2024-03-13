from tortoise import Model, fields

class EventState(Model):
    id_state = fields.IntField(pk=True)
    date_state = fields.CharField(max_length=45)
    hour_state = fields.CharField(max_length=45)
    type_state = fields.CharField(max_length=45)
    justification = fields.TextField()
    user_state = fields.CharField(max_length=255)
    event = fields.ForeignKeyField(
        "models.Event",
        related_name="event_states"
    )
