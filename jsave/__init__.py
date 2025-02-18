import json
import os
from colorxs import Color
from .error import Error
from .utils import clear

from cryptography.fernet import Fernet

key = None

if (os.path.exists(".key")):
    with open('.key', 'rb') as file:
        key = file.read()


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
    
    def keys(self) -> list:
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

    def read(self, keys: list = [], safe_mode: bool = True) -> JData:
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
                    except (KeyError, TypeError):
                        if safe_mode:
                            Error(1002, exp_message + "\n(or set parameter 'safe_mode' to False)", True)
                        else:
                            Error(1003, exp_message + "\n(Skipping since 'safe_mode' is True)", False)

                return JData(return_dict)

            return JData(f.read())
    
    def read_bytes(self) -> bytes:
        """
        Read data from file as bytes

        Returns:
            bytes from file
        """
        with open(self.filepath, "rb") as f:
            return f.read()
        return bytes("None", "utf-8")
    
    def save_bytes(self, data: bytes):
        """
        Write data to file as bytes

        Args:
            data (bytes)
        """
        with open(self.filepath, "wb") as f:
            f.write(data)

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

    def encyrpt(self):
        """
        Encyrpt the current file
        """
        # gen key if it dosent exist
        global key
        if key is None:
            key = Fernet.generate_key()
            with open('.key','wb') as file:
                file.write(key)
        fer = Fernet(key)
        encrypted = fer.encrypt(self.read_bytes())

        self.save_bytes(encrypted)
    
    def decyrpt(self) -> JData:
        """
        Decyrpt the current file
        """
        # gen key if it dosent exist
        global key
        if key is None:
            Error(3001, ".key file dosent exist, meaning you wont be able to decrypt this file unless you have the asocciated .key file", True)
        
        fer = Fernet(key)
        decrypted = fer.decrypt(self.read_bytes())

        self.save_bytes(decrypted)

        return JData(decrypted)

    
JSONData = JData
JSONFile = JFile