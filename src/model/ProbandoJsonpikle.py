from jsonpickle import handlers
import jsonpickle


class Resultado:
    def __init__(self, tipo, date):
        self.tipo = tipo
        self.date = date


class Prueba:
    def __init__(self, name, each, resultado):
        self.name = name
        self.each = each
        self.resultado = resultado


type_of_data_map = {"<type 'str'>": "String"}


class PruebaHandle(handlers.BaseHandler):
    def flatten(self, obj, data, reset=True):
        type1 = str(type(obj.name))
        data["@type"] = type_of_data_map[type1]
        data["@value"] = obj.name
        jsonpickle_encode = jsonpickle.encode(obj.resultado, max_depth=2, unpicklable=False)
        print(jsonpickle_encode)
        data["@resultado"] = jsonpickle_encode
        return data


class ResultadoHandle(handlers.BaseHandler):
    def flatten(self, obj, data, reset=True):
        data["@type"] = "srt"
        data["@value"] = obj.tipo
        data["@date"] = obj.date
        return data


jsonpickle.handlers.registry.register(Prueba, PruebaHandle)
jsonpickle.handlers.registry.register(Prueba, PruebaHandle)
print(jsonpickle.encode(Prueba("osvaldo", 24, Resultado("otroResultado", "otraDate")), unpicklable=False, max_depth=1))
