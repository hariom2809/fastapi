from pydantic import BaseModel, EmailStr

class Postal(BaseModel):
    house: str
    city: str
    state: str
    country: str
    pincode: int

class Contact(BaseModel):
    email: EmailStr
    phone: str
    fax: str
    postal_address: Postal

class User(BaseModel):
    name: str
    contact: Contact

data = {
    "name": "hariom", 
    "contact": {
        "email": "hariom@email.com",
        "phone": "+91 98964555000",
        "fax": "22937281124",
        "postal_address": {
            "house": "house no. 23",
            "city": "Noida",
            "state": "Maharastra",
            "country": "Australia",
            "pincode": 230221
        }
    }
}

user = User(**data)
# print(user)

# print(user.contact.postal_address.pincode)

# Export pydantic shema

# json
# dict

print(user.model_dump(), "\n\n")
print(user.model_dump_json())