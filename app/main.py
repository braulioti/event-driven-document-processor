from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Event-Driven Document Processor",
    description="Mini enterprise backend with event-driven architecture.",
    version="0.1.0",
)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
