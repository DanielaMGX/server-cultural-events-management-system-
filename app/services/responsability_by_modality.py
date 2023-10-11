from app.infra.postgres.crud.responsability_by_modality import crud_responsability_by_mode
from app.services.base import BaseService

class ServiceresponsabilityByMode(BaseService):
    ...


service_responsability_by_mode = ServiceresponsabilityByMode(crud=crud_responsability_by_mode)
