from tortoise import Model, fields


class Responsability(Model):
    name = fields.CharField(max_length=255)
    description = fields.TextField()
