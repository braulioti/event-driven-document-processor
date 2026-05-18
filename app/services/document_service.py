from app.models import DefaultResponse, DocumentRequest


def create_document(request: DocumentRequest, request_id: str) -> DefaultResponse:
    return DefaultResponse(
        success=True,
        message="Document request accepted",
        request_id=request_id,
    )
