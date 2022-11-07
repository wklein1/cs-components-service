from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import modules.csv.csv_reader as csv_reader
from models import component_models, error_models
from decouple import config
from deta import Deta, Base
import uuid

PROJECT_KEY = config("PROJECT_KEY")

deta = Deta(PROJECT_KEY)
componentsDB = deta.Base("componentsdb")

components = csv_reader.read_csv("hardware_components.csv")


def insert_components_to_db(components):
    for component in components:
        component["id"] = str(uuid.uuid1())
       
        try:
            componentsDB.insert(Component(**component).dict())
        except Exception as ex:
            print(f"{component['name']} is already in db!")
        

insert_components_to_db(components)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

@app.get(
    "/components",
    response_model=list[component_models.Component],
    response_description="Returns list of components.",
    description="Get all available components.", 
)
def get_components()->list[component_models.Component]:
    db_components_response = componentsDB.fetch()
    return db_components_response.items


@app.get(
    "/components/{component_id}/price",
    response_model=component_models.PriceResponseModel,
    response_description="Returns an object with the price of the component.",
    responses={404 :{
                "model": error_models.HTTPErrorModel,
                "description": "Error raised if the component can not be found."
        }},
    description="Get the price for a specific component.", 
)
def get_component_price(component_id)->component_models.PriceResponseModel:
    db_component_response = componentsDB.fetch({"id":component_id})
    if len(db_component_response.items) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Component not found")
    price_obj = {
        "price":db_component_response.items[0]["price"]
    }
    return price_obj