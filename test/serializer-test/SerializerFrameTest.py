__author__ = 'osvaldo'

import os
import unittest
import re

from src.operation.FrameSerializer import FrameSerializer
from src.model.Frame import Frame


class SerializerFrameTest(unittest.TestCase):
    def serializer(self, frame):
        return FrameSerializer().serializer(frame)

    def test_serializer_one_frame(self):
        frame = Frame("person")
        frame.add_frame("Name", "Paul Gasol")
        frame.add_frame("Birthday", "07/06/1980")
        frame.add_frame("Country", "Spain")
        self.assertEqual(read_resorce("PauGasol.json"), remove_space(self.serializer(frame)))


def get_directory():
    return os.path.dirname(os.path.abspath(__file__))


def remove_space(string):
    return re.sub("\s", "", string)


def get_directory():
    return os.path.dirname(os.path.dirname(__file__))


def read_resorce(json):
    return remove_space(open(os.path.join(get_directory(), "test-res/" + json)).read())