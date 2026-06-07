from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    id: int
    name: str
    price: float


items = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    items.append(item)
    return item


# TODO: Implement GET /items/{item_id}
# TODO: Implement PUT /items/{item_id}
# TODO: Implement DELETE /items/{item_id}
