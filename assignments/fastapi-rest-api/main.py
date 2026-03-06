# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items_db = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, db_item in enumerate(items_db):
        if db_item.id == item_id:
            items_db[idx] = item
            return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    global items_db
    items_db = [item for item in items_db if item.id != item_id]
    return
