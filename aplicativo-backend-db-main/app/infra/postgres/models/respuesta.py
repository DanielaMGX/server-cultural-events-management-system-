from tortoise import Model, fields
from tortoise.fields.base import SET_NULL


class Respuesta(Model):
    id = fields.IntField(pk=True)
    respuesta = fields.TextField()
    last_modified = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    pregunta = fields.ForeignKeyField(
        "models.Pregunta",
        related_name="preguntas",
        on_delete=SET_NULL,
        null=True,
    )
    