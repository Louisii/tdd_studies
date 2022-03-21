from math import pi

class Circle:

    def __init__(self, raio: int):
        self.raio = raio

    def area(self) -> float:
        return pi*(self.raio ** 2)






'''
def get_raio(self):
        return self.__raio

    def set_raio(self, raio:int):
        if raio <= 0:
            raise ValueError('the radius cannot be negative')
        self.__raio = raio
'''
    

'''
def circle_area(r):
   
    if r < 0:
        raise ValueError('the radius cannot be negative')
    return pi*(r**2)
'''
