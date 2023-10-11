from tortoise import Model, fields
from tortoise.fields.base import SET_NULL


class Pregunta(Model):
    id = fields.IntField(pk=True)
    user = fields.CharField(max_length=255)
    pregunta = fields.TextField()
    last_modified = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    biblioteca = fields.ForeignKeyField(
        "models.Biblioteca",
        related_name="preguntas",
        on_delete=SET_NULL,
        null=True,
    )
    