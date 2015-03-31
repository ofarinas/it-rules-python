import collections
from src.structure.Dictionary import Dictionary

__author__ = 'Osvaldo'
d = Dictionary()
d.set_item("hola",1)
d.set_item("hola2",2)
d.set_item("hola3",3)

h="{"
for k, v in d.items():
    h+="llave:"+ k +"valor:" + v
print(h)