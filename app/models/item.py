from pydantic import BaseModel
from typing import List
from datetime import datetime

class Item(BaseModel):
    batched: str
    payload: List[List[int]]

class Result(BaseModel):
    batched: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime
