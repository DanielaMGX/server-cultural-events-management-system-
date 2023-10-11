from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.biblioteca import Biblioteca
from app.schemas.biblioteca import CreateBiblioteca, UpdateBiblioteca


class CRUDBiblioteca(CRUDBase[Biblioteca, CreateBiblioteca, UpdateBiblioteca]):
    ...
    """
    Basic CRUD of the Biblioteca model, inherits crud base methods
    """


crud_biblioteca = CRUDBiblioteca(model=Biblioteca)
