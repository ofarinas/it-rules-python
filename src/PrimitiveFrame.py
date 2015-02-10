__author__ = 'osvaldo'


class PrimitiveFrame(object):
    __VALUE = "value"

    def __init__(self, value):
        self.__value = value

    def is_type(self):
        return type(self.__value)

    def is_primitive(self):
        return True

    def value(self):
        return self.__value


