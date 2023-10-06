from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.contractual_mode import ContractualMode
from app.schemas.contractual_mode import CreateContractualMode, UpdateContractualMode

class CRUDContractualMode(CRUDBase[ContractualMode, CreateContractualMode, UpdateContractualMode]):
    ...

crud_contractual_mode = CRUDContractualMode(model=ContractualMode)
