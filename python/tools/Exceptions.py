
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to access an element from an full container"""
    pass
