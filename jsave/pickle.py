import pickle


class PickleFile:
    """
    All your pickling in one class

    Args:
        filepath: str
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def pickle(self, data: object):
        """
        Pickle data into the filepath

        Args:
            data: object
        """
        with open(self.filepath, "wb") as f:
            pickle.dump(data, f)
        
    def unpickle(self) -> object:
        """
        Unpickle data from the filepath

        Returns:
            data from the file
        """
        with open(self.filepath, "rb") as f:
            return pickle.load(f)
    

    def __eq__(self, o: object):
        if type(o) is not PickleFile:
            return False

        return o.filepath == self.filepath