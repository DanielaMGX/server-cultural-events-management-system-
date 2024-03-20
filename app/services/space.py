from app.infra.postgres.crud.space import crud_space
from app.services.base import BaseService


class ServiceSpace(BaseService):
    ...


service_space = ServiceSpace(crud=crud_space)
