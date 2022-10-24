from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import modules.csv.csv_reader as csv_reader
from models.component_model import Component
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


@app.get("/components", response_model = list[Component])
def get_components()->list[Component]:
    db_components_response = componentsDB.fetch()
    return db_components_response.items