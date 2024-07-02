from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

class Cart(BaseModel):
    items: List[Item] = []

cart = Cart()

@app.post("/api/v1/add-to-cart")
async def add_to_cart(item: Item):
    cart.items.append(item)
    return {"message": "Item added to cart"}

@app.delete("/api/v1/remove-from-cart/{item_name}")
async def remove_from_cart(item_name: str):
    for i, item in enumerate(cart.items):
        if item.name == item_name:
            del cart.items[i]
            return {"message": f"{item_name} removed from cart"}
    raise HTTPException(status_code=404, detail="Item not found in cart")

@app.get("/api/v1/view-cart")
async def view_cart():
    return cart

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
