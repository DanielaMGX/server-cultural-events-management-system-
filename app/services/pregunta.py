from app.infra.postgres.crud.pregunta import crud_pregunta
from app.services.base import BaseService


class ServicePreguntas(BaseService):
    ...


service_pregunta = ServicePreguntas(crud=crud_pregunta)
