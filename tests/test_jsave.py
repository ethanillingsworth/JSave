import sys
import json

from jsave import JFile, JData

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
    file = JFile("save.json")
    assert file.read() == JData(data)

    assert file.read(["name", "age"]) == JData({
        "name": "John Doe",
        "age": 30
    })

def test_save():
    test_data = {
        "Hello": "World"
    }
    file = JFile("output.json")

    file.save(JData(test_data))

    assert file.read() == JData(test_data)

def test_update():
    file = JFile("output.json")

    data = file.read().set_value("Hello", "world")

    file.update("Hello", "World")

    assert file.read() == data

def test_delete():
    file = JFile("output.json")

    file.delete()

    try:
        file.read()
        assert False
    except FileNotFoundError:
        assert True
