from pydantic import BaseModel, field_validator, model_validator, computed_field
from typing import Optional

class CustomerOrder(BaseModel):

    age: int
    # guardian: Optional[str] = None
    amount_to_pay: float
    amount_paid: float

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 1:
            raise ValueError("Not a Valid input")
        return value

    @model_validator(mode="after")
    @classmethod
    def validate_order(cls, model):
        if model.age < 18:
            # model.guardian = "Hariom"
            # return model.guardian
            model.amount_to_pay = 0.00
            model.amount_paid = 0.00
            return model.amount_to_pay, model.amount_paid
        return model.age

    @computed_field
    @property
    def amount_remaining(self) -> float:
        return self.amount_to_pay - self.amount_paid

data = {
    "age": 20,
    "amount_to_pay": 5000,
    "amount_paid": 2000
}

obj = CustomerOrder(**data)

print(obj)