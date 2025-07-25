from typing import List
from pydantic import parse_obj_as
from pymongo.database import Database
from fastapi import Depends
from config.config import get_db_connection
from dto.dto_transaction import InputTransaction
from model.model_transaction import Transaction

class RepositoryTransaction:
    def __init__(self, db:Database = Depends(get_db_connection)):
        self.repository = db.get_collection("transaction")

    def insert_new_transaction(self, new_transaction: InputTransaction):
        return self.repository.insert_one(new_transaction.dict())
    
    def get_list_transaction(self, match_filter: dict):
        result = self.repository.find(match_filter)
        result = list(result)
        
        return parse_obj_as(List[Transaction], result)