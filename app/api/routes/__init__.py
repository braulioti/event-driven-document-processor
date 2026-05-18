from fastapi import APIRouter

from app.api.routes.documents import router as documents_router
from app.api.routes.health import router as health_router
from app.api.routes.metrics import router as metrics_router

router = APIRouter()

router.include_router(documents_router)
router.include_router(health_router)
router.include_router(metrics_router)
