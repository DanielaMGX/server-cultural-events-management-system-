from typing import TypeVar, Type
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.subeventstate import SubEventState
from app.schemas.subeventstate import CreateSubEventState, UpdateSubEventState

ModelType = TypeVar('ModelType', bound=SubEventState)
CreateSchemaType = TypeVar('CreateSchemaType', bound=CreateSubEventState)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=UpdateSubEventState)

class CRUDSubEventState(CRUDBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    pass

crud_subeventstate = CRUDSubEventState(SubEventState)
