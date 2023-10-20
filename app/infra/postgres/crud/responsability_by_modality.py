from typing import Any, Dict, List
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.responsability_by_modality import ResponsabilityByMode
from app.schemas.responsability_by_modality import CreateresponsabilityByMode, UpdateresponsabilityByMode


class CRUDresponsabilityByMode(CRUDBase[ResponsabilityByMode, CreateresponsabilityByMode, UpdateresponsabilityByMode]):
    
    async def create(self, *, obj_in: CreateresponsabilityByMode) -> int:
        
        obj_in_data = obj_in.dict()


        model = self.model(
            applies=obj_in_data['applies'],
            responsability_id=obj_in_data['responsability'],
            space_id=obj_in_data['space'],
            mode_id=obj_in_data['mode']
        )
        
        await model.save()
        return model
    async def get_all(
    self,
    *,
    payload: Dict[str, Any] = {},
    skip: int = 0,
    limit: int = 10,
) -> List[Dict[str, Any]]:
        
        query = self.model.filter(**payload) if payload else self.model
        models = await query.all().offset(skip).limit(limit).order_by("id")
        
        results = []
        for model in models:
            responsability = await model.responsability
            mode = await model.mode
            space = await model.space
            results.append({
                "id": model.id,
                "applies": model.applies,
                "responsability_id": model.responsability_id,
                "mode_id": model.mode_id,
                "space_id": model.space_id,
                "responsability_name": responsability.name,
                "mode_name": mode.name,
                "space_name": space.name,
            })

        return results





crud_responsability_by_mode = CRUDresponsabilityByMode(model=ResponsabilityByMode)
