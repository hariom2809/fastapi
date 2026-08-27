from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated, List, Optional
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


class UpdateProduct(BaseModel):
    price:          Annotated[Optional[float], Field(default=None, gt=0, description="Please Enter the price in decimal format", examples=[2500.00])]
    tax:            Annotated[Optional[float], Field(default=None, gt=0, lt=28, description="Tax is float field vary form 0-25", examples=[8.00])]
    units:          Annotated[Optional[int], Field(default=None, gt=0, description="Integer field having the count of product in stock")]
    available_on:   Annotated[Optional[List[str]], Field(default=None, description="Name of the Platform wehre product is available in list format")]

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

# PUT / UPDATE
@app.put("/product/{product_id}")
def update_product(
    product: UpdateProduct,
    product_id: str = Path(..., description="Id of the Product in DB", example=["P1"])
):
    # Load Datq
    data = load_data()

    # Check whether the Resouce is in the Data or not
    if product_id not in data:
        raise HTTPException(status_code=404, detail="Product Not Found")

    # Get the required data form the whole data to update it
    old_data = data[product_id]    

    # Convert new data into dictionary obect so that we cna have the oeration perform on it
    new_data = product.model_dump(exclude_unset=True)
    """
    If I have only changed the price of the prodcut the dictionary will become like
    {
        "price": 1400
    }

    Instead of 
    {
        "price": 140,
        "tax": NOne,
        "units": None,
        "available_ON: None"
    }
    """

    for key, value in new_data.items():
        old_data[key] = value
        # data[product_id][price] = 140

    # SAve Data
    data[product_id] = old_data
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Product Updated Successfully",
            "data": data[product_id]
        }
    )

# DELETE
@app.delete("/product/{product_id}")
def delete_product(product_id: str):

    data = load_data()

    if product_id not in data:
        raise HTTPException(status_code=404, detail="Product Not Found")

    del data[product_id]
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Product Deleted Successfully"})