from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated, List
from pydantic import BaseModel, Field
import json


# Data
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)


# Pydantic Schema
class Product(BaseModel):
    id:             Annotated[str, Field(..., description="Id of the product", examples=["P1", "P2"])]
    name:           Annotated[str, Field(..., description="Name of your Product", examples=["Water Bottle"])]
    price:          Annotated[float, Field(..., gt=0, description="Please Enter the price in decimal format", examples=[2500.00])]
    tax:            Annotated[float, Field(..., gt=0, lt=28, description="Tax is float field vary form 0-25", examples=[8.00])]
    units:          Annotated[int, Field(..., gt=0, description="Integer field having the count of product in stock")]
    available_on:   Annotated[List[str], Field(..., description="Name of the Platform wehre product is available in list format")]


# app
app = FastAPI()

# GET
@app.get("/Product")
def list_product():
    return load_data()

# Post
@app.post("/product/{product_id}")
def register_product(
    product: Product,
    product_id: str = Path(..., description="Id of the Product in DB", example=["P1"])
):
    # load all data
    data = load_data()

    # check if data existed
    if product_id in data:
        raise HTTPException(
            status_code=400, 
            detail="Product with this ID already exist"
        )

    # save data
    data[product_id] = product.model_dump(exclude=["id"])
    save_data(data)

    # return acknowledgement message
    return JSONResponse(
        status_code=201,
        content={
            "message": "Product registered Successfully",
            "data": data[product_id]
        }
    )