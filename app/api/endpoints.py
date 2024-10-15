from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import item_service
from app.schemas.item import Item, ItemCreate

router = APIRouter()

@router.post("/items", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, item)

@router.get("/items", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return item_service.get_items(db, skip=skip, limit=limit)
