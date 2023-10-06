from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.pregunta import Pregunta
from app.schemas.pregunta import CreatePregunta, UpdatePregunta


class CRUDPregunta(CRUDBase[Pregunta, CreatePregunta, UpdatePregunta]):
    ...
    """
    Basic CRUD of the Pregunta model, inherits crud base methods
    """


crud_pregunta = CRUDPregunta(model=Pregunta)
