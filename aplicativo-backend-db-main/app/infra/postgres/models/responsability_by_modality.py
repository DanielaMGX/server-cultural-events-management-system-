from tortoise import Model, fields

class ResponsabilityByMode(Model):
    applies = fields.BooleanField() 
    responsability = fields.ForeignKeyField(
        "models.Responsability",
        related_name="responsibilities_by_mode"
    )
    space = fields.ForeignKeyField(
        "models.Space",
        related_name="responsibilities_by_mode"
    )
    mode = fields.ForeignKeyField(
        "models.ContractualMode",
        related_name="responsibilities_by_mode"
    )

class responsability(Model):
    pass

class Mode(Model):
    pass

class Space(Model):
    pass




