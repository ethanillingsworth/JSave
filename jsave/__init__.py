import json
import os
from tsafe import safe, StringList

class JSONData():
    """
    JSONData contains a variety of methods to use on JSON Data

    Args:
        data (str || dict)
    """
    def __init__(self, data: object):
        if (type(data) == dict):
            self.data = data
        else:
            self.data = json.loads(data)

    def prettify(self, indent: int = 4) -> str:
        """
        Returns JSONData with formating

        Args:
            indent (int) = 4

        Returns:
            JSONData as str with formmating
        """
        return json.dumps(self.data, indent=indent)
        
    def set_value(self, key: str, value: object):
        """
        The set_value method works in a similar way to setting keys for dicts with some added comfort featues

        Args:
            key (str)
            value (object)
        
        """
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
        """
        The get_value method works in a similar way to getting keys from a dict

        Args:
            key (str)

        Returns:
            Value at key
        
        """
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
    
    def keys(self) -> StringList:
        """
        Returns:
            keys from data
        """
        return self.data.keys()
    
    def values(self) -> list:
        """
        Returns:
            values from data
        """
        return self.data.values()
            

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, o: object) -> bool:
        return self.data == o

    def __iter__(self):
        return iter(self.data)

    def __len__(self) -> int:
        return len(self.data)

@safe
def save(data: dict, filepath: str, indent: int = 4) -> JSONData:
    """
    Saves a python dict to a filepath as JSON data

    Args:
        data (dict)
        filepath (string)
        indent (int) = 4
    
    Returns:
        JSONData that was written to file
    """
    jsonData = json.dumps(data, indent=indent)
    with open(filepath, "w") as f:
        f.write(jsonData)
    
    return JSONData(data)
    
@safe
def read(filepath: str, keys: StringList = [], safe_mode: bool = True) -> JSONData:
    """
    Reads a JSON file.

    Args:
        filepath (string)
        keys (list) = []
        safe_mode (bool) = True

    Returns:
        JSONData from file
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

@safe
def delete(filepath: str):
    """
    Delete a file at the specified filepath.

    Args:
        filepath (string)

    """
    if os.path.exists(filepath):
        os.remove(filepath)
