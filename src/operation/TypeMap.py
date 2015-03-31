__author__ = 'Osvaldo'


class TypeMap:
    def __init__(self):
        self.__map = {"str": "String"}

    def get(self, key):
        return self.__map.get(key)