from pydantic import BaseModel


class DocumentRequest(BaseModel):
    document_id: str
    document_type: str
