from .error import Error

class JFileList:
    """
    A list comprised of only JFile objects

    Args:
        list (list)
    """
    def __init__(self, list: list = []):
        for i, item in enumerate(list):
            if not isinstance(item, JFile):
                Error(4001, f"The list has an invalid item in it, index {i}", True)
        
        self.list = list
    
    def append(self, item: JFile):

        if not isinstance(item, JFile):
            Error(4002, f"The item you inputed is not a JFile", True)

        self.list.append(item)

    def insert(self, index: int, item: JFile):

        if not isinstance(item, JFile):
            Error(4002, f"The item you inputed is not a JFile", True)

        self.list.insert(index, item)

        
    
    def remove(self, item: JFile):

        if not isinstance(item, JFile):
            Error(4002, f"The item you inputed is not a JFile", True)

        self.list.remove(item)

    
    def pop(self, index: int = 0):
        self.list.pop(index)


    def sort(self):
        self.list.sort()
    
    def get(self, index: int = 0):
        return self.list[index]
    

    def reverse(self):
        self.list.reverse()

    def __repr__(self) -> str:
        return str(self.list)
    
    def __iter__(self):
        return iter(self.list)
    
    def __len__(self):
        return len(self.list)

