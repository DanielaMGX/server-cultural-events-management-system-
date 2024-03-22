from typing import Any, Dict, Generic, List, Optional, Type

from app.schemas.general import CreateSchemaType, ModelType, UpdateSchemaType


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):  # type: ignore
    def __init__(self, *, model: Type[ModelType]) -> None:
        self.model = model

    async def get_all(
        self,
        *,
        payload: Dict[str, Any] = {},
        skip: int = 0,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        query = self.model.filter(**payload) if payload else self.model
        model = await query.all().order_by("id").offset(skip).limit(limit).all()
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> int:
        obj_in_data = obj_in.dict()
        model = self.model(**obj_in_data)
        await model.save()
        return model.id

    async def update(self, *, _id: int, obj_in: UpdateSchemaType) -> bool:
        await self.model.filter(id=_id).update(**obj_in.model_dump(exclude_unset=True))
        return True

    async def delete(self, *, _id: int) -> int:
        deletes = await self.model.filter(id=_id).first().delete()
        return deletes

    async def get_by_id(self, *, _id: int) -> Optional[Dict[str, Any]]:
        if _id:
            model = await self.model.filter(id=_id).first()
            if model:
                return model
        return None

    async def count(self, *, payload: Dict[str, Any] = {}) -> int:
        count = await self.model.filter(**payload).all().count()
        return count
