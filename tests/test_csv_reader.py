from io import StringIO
from modules.csv import csv_reader

def test_parse_csv_mock_file():
    csv_mock = StringIO("name,vendor,price,description,location,manufacturer,product_group,weight,status,ean_number\n"
    "EVGA SuperNOVA GT 850 850W,notebooksbilliger.de,89.90,,Germany,220-GT-0850-Y2,Power-supply,,new,4250812439109")
    csv_list = csv_reader.parse_csv(csv_mock)
    assert csv_list[0]["name"] == "EVGA SuperNOVA GT 850 850W"