import json
import os
from colorxs import Color
from .error import Error
from .utils import clear
from cryptography.fernet import Fernet
from listtypes import TypeList, StringList

key = None

if (os.path.exists(".key")):
    with open('.key', 'rb') as file:
        key = file.read()

# use for type hints
JFileList = None

class JData():
    """
    JData contains a variety of methods to use on JSON Data

    Args:
        data: dict or list or str
    """
    def __init__(self, data: dict or list or str):
        if (type(data) == dict or type(data) == list):
            self.data = data
        elif (data == "" or data is None) :
            self.data = {}
        else:
            self.data = json.loads(data)
    
    def prettify(self, indent: int = 4) -> str:
        """
        Returns JData with formating

        Args:
            indent: int = 4

        Returns:
            JData as str with formmating
        """
        if (indent == -1):
            return self.data

        return json.dumps(self.data, indent=indent)
    
    def set_value(self, key: str or int, value: object):
        """
        The set_value method works in a similar way to setting keys for dicts with some added comfort featues

        Args:
            key: str or int
            value: object

        Returns:
            Previous JData modified
        
        """

        if (isinstance(key, int)):
            self.data[key] = value
            return self
        
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
    
    def get_value(self, key: str or int) -> object:
        """
        The get_value method works in a similar way to getting keys from a dict

        Args:
            key: str

        Returns:
            Value at key
        
        """

        if (isinstance(key, int)):
            return self.data[key]
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
            Keys from data
        """
        return self.data.keys()
    
    def values(self) -> list:
        """
        Returns:
            Values from data
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
    """
    All your JSON file needs in one class

    Args:
        filepath: str
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def create(self):
        """
        Creates a blank file
        """
        with open(self.filepath, "w") as f:
            f.write("{}")

    def save(self, data: JData, indent: int = 4) -> JData:
        """
        Saves a python dict to filepath as JSON data

        Args:
            data: JData
            indent: int = 4
        
        Returns:
            JData that was written to file
        """

        with open(self.filepath, "w") as f:
            json.dump(data.data, f, indent=indent)
        
        return JData(data.data)

    def read(self, keys: StringList = StringList(), safe_mode: bool = True) -> JData:
        """
        Reads a JSON file.

        Args:
            keys: StringList = []
            safe_mode: bool = True

        Returns:
            JData from file
        """
        with open(self.filepath, "r") as f:
            
            if keys:
                loaded_dict = JData(f.read()).data
                
                return_dict = {}

                if (isinstance(loaded_dict, list)):
                    return_dict = []

                for key in keys:
                    
                    exp_message = f"'{key}' could not be loaded, please make sure it is in '{self.filepath}'"

                    try:
                        
                        if (isinstance(return_dict, list)):
                            return_dict.append(loaded_dict[key])
                        else:
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
            data: bytes
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
            key: str
            value: object
        
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
            Error(1011, ".key file dosent exist, meaning you wont be able to decrypt this file unless you have the asocciated .key file", True)
        
        fer = Fernet(key)
        decrypted = fer.decrypt(self.read_bytes())

        self.save_bytes(decrypted)

        return JData(decrypted)

    def combine(self, files: JFileList):
        """
        Combine JSON files into 1 file.

        Args:
            files: JFileList
        """

        merged = {}

        for f in files:
            data = f.read()

            merged = {**merged, **data.data}

    
        self.save(JData(merged))
        
    def combine_paths(self, paths: StringList):
        """
        Combine JSON paths into 1 file.

        Args:
            paths: StringList
        """

        file_list = []

        for path in paths:
            file_list.append(JFile(path))

        self.combine(file_list)

class JFileList(TypeList):
    """
    A list comprised of only JFile objects

    Args:
        l: list
    """
    def __init__(self, l: list = []):
        super().__init__(JFile, l)

class JDataList(TypeList):
    """
    A list comprised of only JData objects

    Args:
        l: list
    """
    def __init__(self, l: list = []):
        super().__init__(JData, l)