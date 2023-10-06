from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.respuesta import Respuesta
from app.schemas.respuesta import CreateRespuesta, UpdateRespuesta


class CRUDrespuesta(CRUDBase[Respuesta, CreateRespuesta, UpdateRespuesta]):
    ...
    """
    Basic CRUD of the respuesta model, inherits crud base methods
    """


crud_respuesta = CRUDrespuesta(model=Respuesta)
