from collections import OrderedDict
import json

__author__ = 'Osvaldo'



class Dictionary():
    def __init__(self):
        self.__dictionary = OrderedDict()

    def clear(self):
        self.__dictionary.clear()

    def get_json(self):
        return json.dumps(self.__dictionary)

    def set_item(self, key, value):
        self.__dictionary.__setitem__(key, value)
        return self

    def values(self):
        return [value for value in self.__dictionary.values().__iter__()]

    def items(self):
        return self.__dictionary.items()

    def copy(self):
        self.__dictionary

    def constain(self, key):
        return key in self.get_list_of_key()

    def get(self, key):
       return self.__dictionary.get(key)


    def clear(self, key, default):
        self.__dictionary.pop(key, default)

    def format(self, *args, **kwargs):
        return self.__dictionary.__format__(*args, **kwargs)

    def ne(self, *args, **kwargs):
        return self.__dictionary.__ne__(*args, **kwargs)

    def repr(self, *args, **kwargs):
        return self.__dictionary.__repr__(*args, **kwargs)

    def ge(self, *args, **kwargs):
        return self.dictionary__ge__(*args, **kwargs)

    def __sizeof__(self):
        return self.__dictionary.__sizeof__()

    def setattr(self, *args, **kwargs):
        return self.__dictionary.__setattr__(*args, **kwargs)

    def dir(self):
        return self.__dictionary.__dir__()

    def le(self, *args, **kwargs):
        return self.__dictionary.__le__(*args, **kwargs)

    def delattr(self, *args, **kwargs):
        return self.__dictionary.__delattr__(*args, **kwargs)

    def hash(self, *args, **kwargs):
        return self.__dictionary.__hash__(*args, **kwargs)

    def gt(self, *args, **kwargs):
        return self.__dictionary.__gt__(*args, **kwargs)

    def eq(self, *args, **kwargs):
        return self.__dictionary.__eq__(*args, **kwargs)

    def getattribute(self, *args, **kwargs):
        return self.__dictionary.__getattribute__(*args, **kwargs)

    def str(self, *args, **kwargs):
        return self.__dictionary.__str__(*args, **kwargs)

    def reduce(self, *args, **kwargs):
        return self.__dictionary.__reduce__(*args, **kwargs)

    def reduce_ex(self, *args, **kwargs):
        return self.__dictionary.__reduce_ex__(*args, **kwargs)

    def lt(self, *args, **kwargs):
        return self.__dictionary.__lt__(*args, **kwargs)

    def keys(self):
        return self.get_list_of_key()

    def get_list_of_key(self):
        return [key for key in self.__dictionary.keys().__iter__()]
