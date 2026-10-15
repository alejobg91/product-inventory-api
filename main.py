from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ProductModel(BaseModel):
    name: str
    price: int

products = [
    {"id":1, "name": "madera", "price": 400},
    {"id":2, "name": "tornillos", "price": 15}
]

@app.get("/")
def health_check():
    return {
        "status":"ok"
    }
@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
        
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def create_product(product: ProductModel):
    new_product = product.model_dump()

    ids = []

    for i in products:
        ids.append(i["id"])

    new_id = max(ids) + 1
    new_product["id"] = new_id

    products.append(new_product)
    return new_product

@app.put("/products/{product_id}")
def modificate_product(product_id: int, product: ProductModel):
    for item in products:
        if item["id"] == product_id:
            item.update(product.model_dump())
            return item
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for item in products:
        if item["id"] == product_id:
            products.remove(item)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
