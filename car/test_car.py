import unittest
from car import Car

class test_car (unittest.TestCase):

    def setUp(self):
        self.car = Car('corsa', 'gm', 'wagon', 'green', 1.0, 2001, 4, 12500)
        return super().setUp()

    def test_carAge(self):
        self.setUp()
        self.assertEqual(self.car.carAge(),21)
        self.tearDown()

    def test_calcFipe(self):
        self.setUp()
        self.assertEqual(self.car.calcFipe(10900),1600)
        self.tearDown()