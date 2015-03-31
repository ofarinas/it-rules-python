import string
# coding=<encoding name>
from src.model.PrimitiveFrame import PrimitiveFrame
from src.structure.Dictionary import Dictionary


__author__ = 'osvaldo'

class Frame:

    def __init__(self, *type):
        self.__slots = Dictionary()
        self.__types = type

    def is_type(self, type):
        return self.__types.__contains__(self, type)

    def get_type(self):
        return self.__types

    def get_slot(self):
        return self.__slots.keys()

    def is_primitive(self):
        return False

    # devolver un iterador o con una lista?
    def get_frame(self, slot):
        return self.__slots.get(slot)[0]

    def add_slot(self, slot, value):
        if isinstance(value, Frame):
            self.__slots.get(slot).append(value)
        else:
            self.__slots.get(slot).append(PrimitiveFrame(value))

    def add_frame(self, slot, *values):
        if not self.__slots.constain(slot):
            self.__slots.set_item(slot, [])
        for value in values:
            self.add_slot(slot, value)
        return self

    def value(self):
        return None

    # por que se va por el 1 er frame que encuentra
    def find_frame(self, path):
        name = ""
        name = path[:str.index(path, ".")] if '.' in path else path
        if None == self.__slots[name]: return None
        slot = self.__slots[name]
        return slot[0] if len(name) >= len(path) else slot[0].findFrame(self, path[string.find('.', path):])

    def search_by_type(self, type):
        return self if self.is_type(self, type) else self.search_by_type(self, type, self.__slots.values())

    def search_by_type(self, type, deep, **slots):
        for slot in slots.values():
            for frame in slot:
                if not frame.isPrimitive() and frame.get_type(self, type) is not None:
                    return frame
                elif frame.isPrimitive() and deep:
                    found_frame = frame.deepSearchByType(self, type)
                if None != found_frame: return found_frame

    def deep_search_by_type(self, type):
        return self if self.isType(type)else self.searchByType(self, type, False, self.__slots.values())

    def search_by_name(self, name, deep, **slots):
        for slot in slots.values():
            for frame in slot:
                if not frame.isPrimitive() and None != frame.get_frame(self, name):
                    return frame
                elif frame.isPrimitive() and deep:
                    found_frame = frame.deepSearchByName(name)
                if None != found_frame: return found_frame

    def search_by_name(self, name):
        return self if self.get_frame(self, name) else self.search_by_name(self, name, self.__slots.values())

    def deep_search_by_name(self, name):
        return self if self.getFrame(name)else None
