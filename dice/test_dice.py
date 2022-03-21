import unittest
from dice import Dice

class test_dice (unittest.TestCase):

    def setUp(self):
        self.dice = Dice()
        return super().setUp()

    def checkRandomness(self, aDice: Dice):
        loop = 0
        value = 3
        while (loop < value):
            loop = loop + 1
            if (aDice.roll(6) != aDice.roll(6)):
                return True
        return False

    def test_roll(self):
        self.setUp()
  
        self.assertLessEqual(self.dice.roll(6),6)
        self.assertLessEqual(self.dice.roll(4),4)
        self.assertGreaterEqual(self.dice.roll(6),1)
        self.assertGreaterEqual(self.dice.roll(1),1)
        with self.assertRaises(BaseException):
            self.dice.roll(0)

        self.assertTrue(self.checkRandomness(self.dice))

        self.tearDown()
