from tortoise import Model, fields

class HistorySubEventState(Model):
    id = fields.IntField(pk=True)
    change_date = fields.DateTimeField()
    state = fields.CharField(max_length=100)
    reason = fields.TextField(null=True)
    changed_by = fields.CharField(max_length=255)
    subevent = fields.ForeignKeyField("models.SubEvent", related_name="history_subevent_states")
