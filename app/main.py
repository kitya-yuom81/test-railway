from fastapi import FastAPI
from .models import Product

app = FastAPI()

products = []

@app.post("/products")
def add_product(product: Product):
    products.append(product.dict())
    return product
