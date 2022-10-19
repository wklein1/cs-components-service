from csv import DictReader

def readCSV(file: str)->list:
    csv_file = open(file,'r', encoding="utf8")
    csv_reader = DictReader(csv_file)

    table = []

    for row in csv_reader:
        table.append(row)

    csv_file.close()

    return table