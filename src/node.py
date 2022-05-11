""" Module Node """
class Node():
    """ Node class """
    def __init__(self, char):
        """ Init method """
        self.char = char
        self.stop = False
        self.children = {}

    def __getitem__(self, key):
        return self.children[key]

    def __setitem__(self, key, value):
        self.children.update({key: value})

    def __contains__(self, char):
        return char in self.children
