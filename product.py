from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)  # must be greater than 0

    # def __init__(self, id: int, name: str, price: float):
    #     self.id = id
    #     self.name = name
    #     self.price = price

    def set_product(self, product: dict):
        self.name = product["name"]
        self.price = product["price"]