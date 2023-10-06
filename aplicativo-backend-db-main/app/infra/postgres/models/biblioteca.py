from tortoise import Model, fields
from tortoise.fields.base import SET_NULL


class Biblioteca(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)
    last_modified = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)