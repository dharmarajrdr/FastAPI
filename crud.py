from fastapi import FastAPI, HTTPException
from product import Product

app = FastAPI()

id = 3
products = [
    Product(id=1, name="iphone13", price=69000.0),
    Product(id=2, name="Macbook M4", price=80000.0)
]

@app.get("/products")
def get_products():
    return products


@app.get("/products/search")
def search_product_by_name(name: str):
    result = []
    for product in products:
        if name.lower() in product.name.lower():
            result.append(product)
    return result


@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=404, detail={"error": "Product not found"})


@app.post("/products", status_code=201)
def create_product(product: dict):
    global id
    product = Product(id=id, name=product["name"], price=product["price"])
    products.append(product)
    id += 1
    return {"message": "Product created successfully"}

@app.put("/products/{id}", status_code=200)
def update_product(id: int, product: dict):
    for p in products:
        if p.id == id:
            p.set_product(product)
            return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail={"error": "Product not found"})

@app.delete("/products/{id}", status_code=204)
def delete_product(id: int):
    for p in products:
        if p.id == id:
            products.remove(p)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail={"error": "Product not found"})

@app.delete("/products", status_code=204)
def delete_all_products():
    products.clear()
    return {"message": "All products deleted successfully"}
