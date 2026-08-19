"""
REST Methods

- GET
- POST
- PUT
- PATCH
_ DELETE
- Query
"""

"""
Parameter in FastAPI

- Path parameter  => Required and include in our API
- Query parameter => optionslas use din filterering and sorting or the data
"""

"""
HTTP Status Code

200, 300, 400, 500
Resources, Redirection, Client side, Server side

200: Successfully fetched ddata
201: Successfully created resource
202: Request accepted data will be return in a while

400: bad request 
401: unauthorized 
401: Forbidden 
404: Not found 

500 internal server error 
502: gateway error
503: Too many request or Server overload
"""

from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open("orders.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/order")
def list_order():
    data = load_data()
    return data

@app.get("/order/{order_id}")
def get_order(
    order_id: str = Path(..., description="Order Id in Db", example="O1")
):
    data = load_data()

    if order_id not in data:
        raise HTTPException(status_code=404, detail="Invalid Order id")
    return data[order_id]

@app.get("/filter-order")
def filter_order(
    price: int = Query(description="Price for the order in interger", example="2500")
):
    data = load_data()

    for order_id, oreder_data in data.items():
        if oreder_data["price"] == price:
            return oreder_data
        raise HTTPException(status_code=404, detail="NO item with this price")