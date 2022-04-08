import unittest
from emplyee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.eu = Employee('Kelvin','quida',2300)

    def test_give_default_raise(self):
        self.eu.give_raise(self)

    def test_give_custom_raise(self):
        
        if self.eu.payment:
            print("Tá rico n")

unittest.main()