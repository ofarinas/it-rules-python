__author__ = 'osvaldo'


class PrimitiveFrame:
    def __init__(self, value):
        self.__value = value

    def get_type(self):
        return type(self.__value).__name__

    def is_primitive(self):
        return True

    def value(self):
        return self.__value


