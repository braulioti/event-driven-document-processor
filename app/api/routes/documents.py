from fastapi import APIRouter, Request

from app.models import DefaultResponse, DocumentRequest
from app.services.document_service import create_document as create_document_service

router = APIRouter()


@router.post("/documents", response_model=DefaultResponse)
def create_document(payload: DocumentRequest, request: Request) -> DefaultResponse:
    return create_document_service(payload, request_id=request.state.request_id)
