from fastapi.testclient import TestClient
from main import app

def test_get_components_endpoint():
    test_client = TestClient(app)
    response = test_client.get("/components")
    assert response.status_code == 200
    assert response.json()[0] == {
        "id": 0,
        "name": "EVGA SuperNOVA GT 850 850W",
        "vendor": "notebooksbilliger.de",
        "price": "89.90",
        "description": "",
        "location": "Germany",
        "manufacturer": "220-GT-0850-Y2",
        "product_group": "Power-supply",
        "weight": "",
        "status": "new",
        "ean_number": "4250812439109"
  }