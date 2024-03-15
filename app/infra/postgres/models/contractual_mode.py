from tortoise import Model, fields


class ContractualMode(Model):
    name = fields.CharField(max_length=255)
