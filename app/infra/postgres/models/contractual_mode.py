from tortoise import fields, Model

class ContractualMode(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
