from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional



# These all are required fields 
class Customer(BaseModel):

    name: str
    email: EmailStr
    website: AnyUrl
    age: int
    married: bool = False
    item: List[str]
    contact_info: Dict[str, str]


# These fields do have some optional values
class Customer2(BaseModel):

    name: str
    email: EmailStr
    website: Optional[AnyUrl] = None
    age: int
    married: bool = False
    item: List[str]
    contact_info: Dict[str, str]

# Comparing both the above classes schema

order_list = {
    "name": "Hariom",
    "email": "hariom@email.com",
    "website": "http://www.hario.com",
    "age": 23,
    "married": False,
    "item": ["gas", "stove", "pan"],
    "contact_info": {
        "phone": "1234567890",
        "fax": "55522255522"
    }
}

order_list2 = {
    "name": "Hariom",
    "email": "hariom@email.com",
    "age": 23,
    "item": ["gas", "stove", "pan"],
    "contact_info": {
        "phone": "1234567890",
        "fax": "55522255522"
    }
}


order = Customer(**order_list)
print(order)

print("\n", "======================", "\n")

order = Customer2(**order_list2)
print(order)

