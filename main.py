from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import modules.csv.csv_reader as csv_reader


components = csv_reader.read_csv("hardware_components.csv")


def set_ids(components):
    id = 0
    for component in components:
        component["id"]=id
        id+=1
        
set_ids(components)

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


@app.get("/components")
def get_components():
    return components