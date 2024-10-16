import json
import os


class JSONData():
    """
    Create JSONData

    Args:
        data (str || dict)
    """
    def __init__(self, data):
        if (type(data) == dict):
            self.data = data
        else:
            self.data = json.loads(data)

    def prettify(self, indent: int = 4) -> str:
        """
        Returns JSONData with formating

        Args:
            indent (int) = 4
        """
        return json.dumps(self.data, indent=indent)

    def set_value(self, key: str, value):
        keyPath = key.split("/")
        latestValue = self.data
        for index, k in enumerate(keyPath):
            try:
                latestValue = latestValue[k]
            except KeyError:
                latestValue[k] = {}
                if index == len(keyPath) - 1:
                    latestValue[k] = value
                
                latestValue = latestValue[k]

    def get_value(self, key: str) -> object:
        keyPath = key.split("/")
        latestValue = self.data
        for index, k in enumerate(keyPath):
            try:
                latestValue = latestValue[k]
            except TypeError:
                raise Exception(f"key '{k}' could not be found")
        if type(latestValue) == dict:
            return JSONData(latestValue)
        return latestValue
            

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, o: object) -> bool:
        return self.data == o

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)





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
    

def read(filepath: str, keys: [str] = [], safe_mode: bool = True) -> JSONData:
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
            loaded_dict = JSONData(f.read())
            print(loaded_dict)
            return_dict = {}
            for key in keys:
                try:
                    return_dict[key] = loaded_dict.data[key]
                except KeyError:
                    if safe_mode:
                        raise Exception(f"'{key}' could not be loaded, please make sure it is in '{filepath}'\n(or set parameter 'safe_mode' to False)")
                    else:
                        continue
            return JSONData(return_dict)

        return JSONData(f.read())

def delete(filepath: str):
    """
    Delete a file at the specified filepath.

    Args:
        filepath (string)

    """
    if os.path.exists(filepath):
        os.remove(filepath)
