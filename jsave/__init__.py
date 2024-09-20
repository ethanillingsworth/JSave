import json
import os

def save(data: dict, filepath: str):
    """
    Saves a python dict to a filepath as JSON data

    Args:
        data (dict)
        filepath (string)
    """
    jsonData = json.dumps(data, indent=4)
    with open(filepath, "w") as f:
        f.write(jsonData)
    

def read(filepath: str, keys: [str] = [], safe_mode: bool = True) -> dict:
    """
    Reads a JSON file an return it as a python dict.

    Args:
        filepath (string)
        keys ([str]) = []
        safe_mode (bool) = True

    Returns:
        Dict with JSON data
    """
    with open(filepath, "r") as f:
        if keys:
            loaded_dict = json.loads(f.read())
            print(loaded_dict)
            return_dict = {}
            for key in keys:
                try:
                    return_dict[key] = loaded_dict[key]
                except KeyError:
                    if safe_mode:
                        raise Exception(f"'{key}' could not be loaded, please make sure it is in '{filepath}'\n(or set parameter 'safe_mode' to False)")
                    else:
                        continue
            return return_dict

        return json.loads(f.read())

def delete(filepath: str):
    """
    Delete a file at the specified filepath.

    Args:
        filepath (string)

    """
    if os.path.exists(filepath):
        os.remove(filepath)

def merge(files: [str], output_filepath: str):
    """
    Merge 2 or more JSON files and combine them into one.

    Args:
        files ([str])
        output_filepath (str)

    """
    merged_data = {}

    for file in files:
        data = read(file)
        merged_data.update(data)
        
    save(merged_data, output_filepath)