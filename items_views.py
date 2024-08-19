import uvicorn
from fastapi import APIRouter
from typing import Annotated
from fastapi import Path

router = APIRouter(prefix='/items', tags=["items"])


@router.get("/")
def list_items():
    return {
        "Item1": 1,
        "Item2": 2,
        "Item3": 3
    }


@router.get("/{item_id}/")
def list_items_id(item_id: int):
    return {
        'item': item_id
    }
