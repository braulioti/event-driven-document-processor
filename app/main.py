from fastapi import FastAPI

from app.api.routes import router
from app.core.exception_handlers import register_exception_handlers
from app.core.metrics import PrometheusMiddleware
from app.core.request_id import RequestIDMiddleware

app = FastAPI(
    title="Event-Driven Document Processor",
    description="Mini enterprise backend with event-driven architecture.",
    version="0.1.0",
)

register_exception_handlers(app)

app.add_middleware(PrometheusMiddleware)
app.add_middleware(RequestIDMiddleware)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
