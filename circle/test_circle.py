import unittest
from circle import Circle
from math import pi

class TestCircleArea(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(1)
        return super().setUp()

    def test_area(self):
        self.assertEquals(self.circle.raio, 1)
        #with self.assertRaises(ValueError):
        #    self.circle.raio = 0
        self.assertEquals(self.circle.area(), pi)
        self.circle.raio = 2
        self.assertEqual(self.circle.area(), 4 * pi)

    '''
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def tast_values(self):
        self.assertRaises(ValueError, circle_area, -2)
    '''