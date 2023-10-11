from tortoise import fields, Model

class Space(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
