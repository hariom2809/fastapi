"""
Why Pydantic

1. Type Validation
2. Data Validation
"""
# Type validation checking if the entered valye has correct type
def validate_age(age):
    if type(age) == int:
        return age
    raise ValueError("Age must be a number")

# data validation if the entered vlue is valid response or not 
def can_take_admission(age):
    if 3 < age < 20:
        return "Can take admission"
    return "No admission"

def my_age(age):
    return age
