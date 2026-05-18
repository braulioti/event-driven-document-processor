from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.exceptions import DocumentProcessingException


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DocumentProcessingException)
    async def document_exception_handler(request, exc):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(exc),
            },
        )
