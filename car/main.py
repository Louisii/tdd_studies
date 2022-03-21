from car import Car

corsaFofo = Car('corsa', 'chevrolet', 'wagon', 'green', 1.0, 2001, 4, 12500)
renegade = Car('renegade', 'jeep', 'suv', 'white', 1.8, 2021, 4, 110000)

print(corsaFofo.style)
print(renegade.style)

print(corsaFofo.calcFipe(10900))