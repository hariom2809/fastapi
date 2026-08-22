# import pydantic module
from pydantic import BaseModel

# Pydantic class
class Order(BaseModel):

    product: str
    price: float
    available_on: list


order_list = {"product": "laptop", "price": 399.99, "available_on": ["Amazon"]}
order = Order(**order_list)

print(order.product)
print(order.price)
print(order.available_on)

