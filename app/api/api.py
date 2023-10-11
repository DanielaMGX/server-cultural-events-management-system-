from fastapi import APIRouter
from app.api.routers import responsability_by_modality, responsability, contractual_mode, space, root


api_router = APIRouter()
api_router.include_router(root.router, prefix="/health-check", tags=["Health Check"])
api_router.include_router(responsability_by_modality.router, prefix="/responsability-by-mode", tags=["responsabilityByMode"])
api_router.include_router(responsability.router, prefix="/responsability", tags=["responsability"])
api_router.include_router(contractual_mode.router, prefix="/contractual-modes", tags=["Contractual Modes"])
api_router.include_router(space.router, prefix="/spaces", tags=["Spaces"])