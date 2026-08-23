from pydantic import BaseModel, EmailStr,  Field
from typing import Annotated

# Field 
class User(BaseModel):

    name: str = Field(max_length=10)
    email: EmailStr
    age: int = Field(gt=0, lt=120)

user_data = {
    "name": "Hariom",
    "email": "hariom@email.com",
    "age": 23
}

user = User(**user_data)

# Annotated

class User2(BaseModel):

    name: Annotated[str, Field(max_length=25)]
    age: Annotated[int, Field(gt=0, lt=120)]

user_data = {
    "name": "Hariom",
    "age": 23
}

user = User2(**user_data)

print(user)