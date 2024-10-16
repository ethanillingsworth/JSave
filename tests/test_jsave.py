import sys
import json

sys.path.insert(0, './')
from jsave import save, read, delete, JSONData

data = {
    "name": "John Doe",
    "age": 30,
    "is_employee": True,
    "departments": ["Sales", "Marketing", "Development"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "postal_code": "10001"
    },
    "projects": [
        {"name": "Website Redesign", "status": "completed"},
        {"name": "Mobile App Development", "status": "in progress"}
    ],
    "hire_date": None
}

jsonData = json.dumps(data, indent=4)
with open("save.json", "w") as f:
    f.write(jsonData)


def test_read():
    assert read("save.json") == JSONData(data)

    assert read("save.json", {"name", "age"}) == JSONData({
        "name": "John Doe",
        "age": 30
    })

def test_save():
    test_data = {
        "Hello": "World"
    }
    save(test_data, "newsave.json")

    assert read("newsave.json") == JSONData(test_data)

def test_delete():
    delete("output.json")

    try:
        read("output.json")
        assert False
    except FileNotFoundError:
        assert True
