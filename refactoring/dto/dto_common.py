from pydantic import BaseModel


class StandardResponse(BaseModel):
    detail: str