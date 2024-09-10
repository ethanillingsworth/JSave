import sys
import json

sys.path.insert(0, './jsave')
from jsave import save, read, merge, delete

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
    assert read("save.json") == data

def test_save():
    test_data = {
        "Hello": "World"
    }
    save(test_data, "newsave.json")

    assert read("newsave.json") == test_data

def test_update():
    merge(["save.json", "newsave.json"], "output.json")

    save = read("save.json")

    newsave = read("newsave.json")

    merge_data = {}

    merge_data.update(save)
    merge_data.update(newsave)


    assert read("output.json") == merge_data

def test_delete():
    delete("output.json")

    try:
        read("output.json")
        assert False
    except FileNotFoundError:
        assert True
