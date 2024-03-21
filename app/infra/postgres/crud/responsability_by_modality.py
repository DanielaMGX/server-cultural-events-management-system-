from typing import Any, Dict, List, Optional

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.responsability_by_modality import ResponsabilityByMode
from app.schemas.responsability_by_modality import (
    CreateresponsabilityByMode,
    UpdateresponsabilityByMode,
)


class CRUDresponsabilityByMode(
    CRUDBase[
        ResponsabilityByMode, CreateresponsabilityByMode, UpdateresponsabilityByMode
    ]
):
    async def create(self, *, obj_in: CreateresponsabilityByMode) -> int:
        obj_in_data = obj_in.dict()

        model = self.model(
            applies=obj_in_data["applies"],
            responsability_id=obj_in_data["responsability"],
            space_id=obj_in_data["space"],
            mode_id=obj_in_data["mode"],
        )

        await model.save()
        return model

    async def get_applies_by_mode_and_space(
        self, *, mode: int, space_name: str
    ) -> list:
        model = await self.model.filter(
            applies=True, mode_id=mode, space__name=space_name
        ).all()
        if model is None:
            return []
        return model

    async def get_all(
        self,
        *,
        payload: Dict[str, Any] = {},
        skip: int = 0,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        query = self.model.filter(**payload) if payload else self.model
        model = (
            await query.all()
            .prefetch_related(
                "mode",
                "responsability",
                "space",
            )
            .offset(skip)
            .limit(limit)
            .all()
            .values(
                "id",
                "applies",
                "responsability_id",
                "space_id",
                "mode_id",
                "mode__name",
                "responsability__name",
                "space__name",
            )
        )
        return model

    async def get_by_id(self, *, _id: int) -> Optional[Dict[str, Any]]:
        if _id:
            model = (
                await self.model.filter(id=_id)
                .first()
                .values(
                    "id",
                    "applies",
                    "responsability_id",
                    "space_id",
                    "mode_id",
                    "mode__name",
                    "responsability__name",
                    "space__name",
                )
            )
            if model:
                return model
        return None


crud_responsability_by_mode = CRUDresponsabilityByMode(model=ResponsabilityByMode)
