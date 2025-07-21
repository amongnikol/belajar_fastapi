from typing import Annotated, Optional
from fastapi import APIRouter, Depends

from dto.dto_transaction import InputTransaction
from enums.enum_tipe import Tipe
from dto.dto_common import TokenData
from service.service_common import get_current_user
from service.service_transaction import ServiceTransaction

router_transaction = APIRouter(prefix="/api/v1", tags=["transaction"])

@router_transaction.post("/transaction")
def insert_new_transaction(input_transaction: InputTransaction,
                           current_user: Annotated[TokenData, Depends(get_current_user)], 
                           service_transaction: ServiceTransaction = Depends()):
    print(current_user)
    service_transaction.insert_new_transaction(input_transaction)

    return input_transaction

@router_transaction.get("/transaction")
def get_list_transaction(current_user: Annotated[TokenData, Depends(get_current_user)],
                         tipe: Optional[Tipe] = None, 
                         service_transaction: ServiceTransaction = Depends()):

    return service_transaction.get_list_transaction(tipe, current_user)