from fastapi.testclient import TestClient
from main import app

def test_get_components_endpoint():
    test_client = TestClient(app)
    response = test_client.get("/components")
    assert response.status_code == 200
    assert response.json()[0] == {
        "id": "546c08d7-539d-11ed-a980-cd9f67f7363d",
        "name": "AMD Ryzen 9 5950X",
        "vendor": "notebooksbilliger.de",
        "price": 559.0,
        "description": "",
        "location": "Germany",
        "manufacturer": "100-100000059WOF",
        "productGroup": "CPU",
        "weight": 300.0,
        "status": "new",
        "eanNumber": "730143312745"
  }

def test_get_components_endpoint_ids():
    test_client = TestClient(app)
    response = test_client.get("/components")
    assert response.status_code == 200
    assert response.json()[0]["id"] == "546c08d7-539d-11ed-a980-cd9f67f7363d"
    assert response.json()[1]["id"] == "546c08da-539d-11ed-a980-cd9f67f7363d"
