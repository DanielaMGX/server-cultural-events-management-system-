from app.infra.postgres.crud.contractual_mode import crud_contractual_mode
from app.services.base import BaseService


class ServiceContractualMode(BaseService):
    ...


service_contractual_mode = ServiceContractualMode(crud=crud_contractual_mode)
