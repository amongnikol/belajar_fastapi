from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from enums.enum_tipe import Tipe
from enums.enum_method import Method
from model.model_common import PyObjectId

class Transaction(BaseModel):
    id: PyObjectId = Field(alias="_id")
    tipe:Tipe
    amount:int
    notes:Optional[str] # biar gak required
    method:Method

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

        