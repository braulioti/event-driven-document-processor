from pydantic import BaseModel


class DefaultResponse(BaseModel):
    success: bool
    message: str
    request_id: str
