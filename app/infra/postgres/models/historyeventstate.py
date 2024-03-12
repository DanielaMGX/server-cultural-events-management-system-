from tortoise import Model, fields

class HistoryEventState(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    time = fields.TimeField()
    state = fields.CharField(max_length=100)
    justification = fields.TextField(null=True)
    event = fields.ForeignKeyField('models.Event', related_name='history_event_states')
