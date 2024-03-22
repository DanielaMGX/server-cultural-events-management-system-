from tortoise import Model, fields


class EventHasResponsability(Model):
    accomplishment = fields.ForeignKeyField("models.Accomplishment")
    responsability_by_mode = fields.ForeignKeyField(
        "models.ResponsabilityByMode", null=True
    )
    event = fields.ForeignKeyField("models.Event")
    specific_responsability = fields.ForeignKeyField(
        "models.SpecificResponsability", null=True
    )
