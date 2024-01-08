from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Item, SessionLocal, engine


class ItemRequest(BaseModel):
    id: int
    name: str
    description: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"result": "Hello World"}


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/")
def create_item(item: ItemRequest, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    existed = db.query(Item).filter(Item.id == item.id).first()
    if existed is None:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return {"status": "User is existed"}


@app.get("/items/")
def get_list_item(db: Session = Depends(get_db)):
    all_items = db.query(Item).all()
    if len(all_items) == 0:
        return {"users": []}
    else:
        return {"users": all_items}


@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
