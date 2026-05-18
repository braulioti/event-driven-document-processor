from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.api.routes import router
from app.config import get_settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging_config import setup_logging
from app.core.metrics import PrometheusMiddleware
from app.core.request_id import RequestIDMiddleware

settings = get_settings()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging(settings)
    logger.info(
        "Application started (env=%s, kafka=%s)",
        settings.app_env,
        settings.kafka_bootstrap_servers,
    )
    yield
    logger.info("Application shutdown")


app = FastAPI(
    title=settings.app_name,
    description="Mini enterprise backend with event-driven architecture.",
    version=settings.app_version,
    lifespan=lifespan,
)

register_exception_handlers(app)

app.add_middleware(PrometheusMiddleware)
app.add_middleware(RequestIDMiddleware)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload,
    )
