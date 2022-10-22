from pydantic import BaseModel

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


