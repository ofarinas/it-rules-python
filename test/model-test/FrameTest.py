from collections import OrderedDict
import unittest
from datetime import date
from src.model.Frame import Frame


__author__ = 'osvaldo'


class FrameTest(unittest.TestCase):
    def test_type_Frame(self):
        frame = Frame("Person")
        self.assertFalse(frame.is_primitive())
        self.assertTrue(frame.get_type(), "Person")

    def get_date(self):
        return date(1990, 6, 13).strftime("%d/%m/%Y")

    def test_add_one_primitiveFrame(self):
        frame = Frame("Person")
        frame.add_frame("name", "Osvaldo")
        frame.add_frame("each", 24)
        frame.add_frame("birthday", self.get_date())
        self.assertFalse(frame.is_primitive())
        self.assertEquals(frame.get_type()[0], "Person")
        self.assertEqual(frame.get_frame("name")[0].value(), "Osvaldo")
        self.assertEqual(frame.get_frame("each")[0].value(), 24)
        self.assertEqual(frame.get_frame("birthday")[0].value(), self.get_date())

    def test_add_one_frame(self):

        frame = Frame("Person")
        frame.add_frame("name", "Paul Gasol")
        frame.add_frame("pet", Frame("Dog").add_frame("name", "Toby").add_frame("Age", 5))
        frame.add_frame("pet", Frame("Dog").add_frame("name", "Ruffo").add_frame("ID", "X204512"))
        frame.add_frame("pet", Frame("Cat").add_frame("name", "Missy").add_frame("ID", "y412221"))
        self.assertEqual(frame.get_type()[0], "Person")
        self.assertEqual(frame.get_type()[0], "Person")
        self.assertEqual(frame.get_slot(), ["name", "pet"])
        self.assertEqual(frame.get_frame("name")[0].value(), "Paul Gasol")
        self.assertEqual(frame.get_frame("pet")[0].get_type()[0], "Dog")
        self.assertEqual(frame.get_frame("pet")[0].get_slot(), ["name", "Age"])
        self.assertEqual(frame.get_frame("pet")[0].get_frame("name")[0].value(), "Toby")
        self.assertEqual(frame.get_frame("pet")[0].get_frame("Age")[0].value(), 5)
        self.assertEqual(frame.get_frame("pet")[1].get_type()[0], "Dog")
        self.assertEqual(frame.get_frame("pet")[1].get_slot(), ["name", "ID"])
        self.assertEqual(frame.get_frame("pet")[1].get_frame("name")[0].value(), "Ruffo")
        self.assertEqual(frame.get_frame("pet")[2].get_type()[0], "Cat")
        self.assertEqual(frame.get_frame("pet")[2].get_slot(), ["name", "ID"])
        self.assertEqual(frame.get_frame("pet")[2].get_frame("name")[0].value(), "Missy")
        self.assertEqual(frame.get_frame("pet")[2].get_frame("ID")[0].value(), "y412221")