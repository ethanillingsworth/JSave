import json

def save(data: dict, filepath: str):
    jsonData = json.dumps(data, indent=4)
    with open(filepath, "w") as f:
        f.write(jsonData)
    

def read(filepath: str) -> dict:
    with open(filepath, "r") as f:
        return json.loads(f.read())
