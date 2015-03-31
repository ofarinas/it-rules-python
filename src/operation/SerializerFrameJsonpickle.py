import re
import jsonpickle
from jsonpickle import handlers
from src.model.PrimitiveFrame import PrimitiveFrame
from src.model.Frame import Frame
from src.structure.Dictionary import Dictionary


class SerializerFrameJsonpickle():
    def __init__(self):
        pass

    @staticmethod
    def serializer(frame):
        jsonpickle.handlers.registry.register(PrimitiveFrame, PrimitiveFrameHandle)
        jsonpickle.handlers.registry.register(Frame, FrameHandle)
        return jsonpickle.encode(frame, unpicklable=False)


class PrimitiveFrameHandle(handlers.BaseHandler):
    def flatten(self, obj, data, reset=True):
        data["@type"] = obj.get_type()
        data["@value"] = obj.value()
        return data

    def restore(self, obj):
        pass


class FrameHandle(handlers.BaseHandler):
    def writeFileExpression(self, dictionary):
        file = open("json.txt", "w")
        json = jsonpickle.encode(dictionary, unpicklable=False)
        json_regex = re.sub("\\\\","",json)
        file.write(json_regex)
        file.close()

    def flatten(self, obj, data):
        dictionary = Dictionary()
        dictionary.set_item("@types", jsonpickle.encode(obj.get_type(), unpicklable=False))
        for slot in obj.get_slot():
           dictionary.set_item(slot,jsonpickle.encode(obj.get_frame(slot), unpicklable=False))
        self.writeFileExpression(dictionary)
        return jsonpickle.encode(dictionary, unpicklable=False)

    def restore(self, obj):
        pass

