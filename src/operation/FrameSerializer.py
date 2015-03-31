import json

from src.model.Frame import Frame

from src.operation.TypeMap import TypeMap
from src.structure.Dictionary import Dictionary


__author__ = 'Osvaldo'


class FrameSerializer:
    def add_type_of_Frame(self, dictionary, frame):
        dictionary.set_item(json.dumps("@types"), json.dumps(frame.get_type()))

    def add_frame(self, dictionary, frame, slot):
        dictionary.set_item(json.dumps(slot), self.serializer(frame.get_frame(slot)))

    def add_primitive_frame(self, dictionary, frame, slot):
        dictionary.set_item(json.dumps(slot), self.serialezer_primitive_frame(frame, slot))

    def add(self, dictionary, frame, slot):
        if isinstance(frame.get_frame(slot), Frame):
            self.add_frame(dictionary, frame, slot)
        else:
            self.add_primitive_frame(dictionary, frame, slot)

    def serializer(self, frame):
        dictionary = Dictionary()
        self.add_type_of_Frame(dictionary, frame)
        for slot in frame.get_slot():
            self.add(dictionary, frame, slot)
        return self.serializerJson(dictionary)


    def get_primitive_type(self, frame, slot):
        return TypeMap().get(frame.get_frame(slot).get_type())

    def get_primitive_value(self, frame, slot):
        return frame.get_frame(slot).value()

    def serialezer_primitive_frame(self, frame, slot):
        return Dictionary().set_item("@type", self.get_primitive_type(frame, slot)).set_item("@value",self.get_primitive_value(frame, slot)).get_json()

    def serializerJson(self, dictionary):
        json = "{"
        for key, value in dictionary.items():
            json += key + ":" + value + ","
        return json[:-1] + "}"

