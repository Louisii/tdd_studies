from random import randint

class Dice:

    def __init__(self):
        pass

    def roll(self, faces):
        if (faces <= 0):
            raise BaseException()
        return randint(1, faces)
