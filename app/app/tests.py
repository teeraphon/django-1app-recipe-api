from django.test import SimpleTestCase
from app import calc

class CalTests(SimpleTestCase):
    
    def test_add_number(self):
        res = calc.add(5,6)
        self.assertEqual(res, 11)
    
    def test_substract_number(self):
        res = calc.substract(10,15)
        self.assertEqual(res, 5)