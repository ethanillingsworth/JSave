import sys
import json
import os

from jsave import JFile, JData

if not os.path.exists("jsons"):
    os.mkdir("jsons")
    
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

data2 = [
    "Hello",
    "World",
    0,
    213,
    21.23,
    None,
    {
        "Object": "Thingy"
    },
    True
]




with open("jsons/save.json", "w") as f:
    json.dump(data, f, indent=4)

with open("jsons/save2.json", "w") as f:
    json.dump(data2, f, indent=4)


def test_read():
    file = JFile("jsons/save.json")
    file2 = JFile("jsons/save2.json")

    assert file.read() == JData(data)

    assert file2.read() == JData(data2)

    assert file.read(["name", "age"]) == JData({
        "name": "John Doe",
        "age": 30
    })

    assert file2.read([0, 2]) == JData([
        "Hello",
        0
    ])

def test_save():
    test_data = {
        "Hello": "World"
    }
    file = JFile("jsons/output.json")

    file.save(JData(test_data))

    file2 = JFile("jsons/output2.json")

    file2.save(JData(["Hello", "World", 102]))


    assert file.read() == JData(test_data)
    assert file2.read() == JData(["Hello", "World", 102])


def test_update():
    file = JFile("jsons/output.json")

    data = file.read().set_value("Hello", "world")

    file.update("Hello", "World")

    assert file.read() == data

def test_delete():
    file = JFile("jsons/output.json")

    file.delete()

    try:
        file.read()
        assert False
    except FileNotFoundError:
        assert True
