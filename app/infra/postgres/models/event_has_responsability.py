from tortoise import Model, fields


class EventHasResponsability(Model):
    accomplishment = fields.ForeignKeyField("models.Accomplishment")
    responsability_by_mode = fields.ForeignKeyField("models.ResponsabilityByMode")
    event = fields.ForeignKeyField("models.Event")
