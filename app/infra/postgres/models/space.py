from tortoise import Model, fields


class Space(Model):
    name = fields.CharField(max_length=255)
