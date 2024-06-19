from fastapi import APIRouter, HTTPException
from app.models.item import Item, Result
from app.controllers.addition_controller import add_numbers
from datetime import datetime

router = APIRouter()

@router.post("/add", response_model=Result)
async def addition(item: Item):
    started_at = datetime.utcnow()
    try:
        result = add_numbers(item.payload)
        completed_at = datetime.utcnow()
        return Result(
            batched=item.batched,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
