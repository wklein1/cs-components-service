from pydantic import BaseModel,Field,Extra,validator

class Component(BaseModel):
    id: int
    name: str
    vendor: str
    price: float
    description: str
    location: str
    manufacturer: str
    product_group: str = Field(alias="productGroup")
    weight: float
    status: str
    ean_number: str = Field(alias="eanNumber")

    @validator('weight','price', pre=True)
    def empty_str_to_zero(cls, value):
        if value == '':
            return 0
        return value

    class Config:
        allow_population_by_field_name = True
        extra = Extra.forbid


