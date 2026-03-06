# Starter code for FastAPI REST APIs assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items: Dict[int, Item] = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# Implement CRUD endpoints below
# ...
