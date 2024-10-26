import json
import os
from tsafe import StringList, safe
from colorxs import Color
from jsave.error import Error

class JData():
    """
    JData contains a variety of methods to use on JSON Data

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
        Returns JData with formating

        Args:
            indent (int) = 4

        Returns:
            JData as str with formmating
        """
        return json.dumps(self.data, indent=indent)
    
    def set_value(self, key: str, value: object):
        """
        The set_value method works in a similar way to setting keys for dicts with some added comfort featues

        Args:
            key (str)
            value (object)

        Returns:
            Previous JData modified
        
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
            except TypeError:
                break
        
        return self
    
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
                Error(1001, f"key '{k}'{Color.BLUE} could not be found", True)
        if type(latestValue) == dict:
            return JData(latestValue)
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

class JFile():
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def save(self, data: JData, indent: int = 4) -> JData:
        """
        Saves a python dict to filepath as JSON data

        Args:
            data (JData)
            indent (int) = 4
        
        Returns:
            JData that was written to file
        """
        jsonData = json.dumps(data.data, indent=indent)
        with open(self.filepath, "w") as f:
            f.write(jsonData)
        
        return JData(data.data)

    def read(self, keys: StringList = [], safe_mode: bool = True) -> JData:
        """
        Reads a JSON file.

        Args:
            keys (StringList) = []
            safe_mode (bool) = True

        Returns:
            JData from file
        """
        with open(self.filepath, "r") as f:
            
            if keys:
                loaded_dict = JData(f.read()).data
                
                return_dict = {}
                for key in keys:
                    
                    exp_message = f"'{key}' could not be loaded, please make sure it is in '{self.filepath}'"

                    try:
                        return_dict[key] = loaded_dict[key]
                    except KeyError:
                        if safe_mode:
                            Error(1002, exp_message + "\n(or set parameter 'safe_mode' to False)", True)
                        else:
                            Error(1003, exp_message + "\n(Skipping since 'safe_mode' is True)", False)

                    except TypeError:
                        if safe_mode:
                            Error(1002, exp_message + "\n(or set parameter 'safe_mode' to False)", True)
                        else:
                            Error(1003, exp_message + "\n(Skipping since 'safe_mode' is True)", False)

                return JData(return_dict)

            return JData(f.read())

    def delete(self):
        """
        Delete a file at the specified filepath.
        """
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
    
    def update(self, key: str, value: object):
        """
        Update value at key for specified filepath.

        Args:
            key (str)
            value (object)
        
        """

        self.save(self.read().set_value(key, value))

JSONData = JData
JSONFile = JFile