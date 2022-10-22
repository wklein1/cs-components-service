from pydantic import BaseModel,validator

class Component(BaseModel):
    id: int
    name: str
    vendor: str
    price: float
    description: str
    location: str
    manufacturer: str
    product_group: str
    weight: float
    status: str
    ean_number: str

    @validator('weight','price', pre=True)
    def empty_str_to_zero(cls, value):
        if value == '':
            return 0
        return value


