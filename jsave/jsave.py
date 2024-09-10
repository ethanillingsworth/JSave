import json
import os

def save(data: dict, filepath: str):
    jsonData = json.dumps(data, indent=4)
    with open(filepath, "w") as f:
        f.write(jsonData)
    

def read(filepath: str) -> dict:
    with open(filepath, "r") as f:
        return json.loads(f.read())

def delete(filepath: str):
    if os.path.exists(filepath):
        os.remove(filepath)

def merge(files: [str], output_filepath: str):
    merged_data = {}

    for file in files:
        data = read(file)
        merged_data.update(data)
        
    save(merged_data, output_filepath)
