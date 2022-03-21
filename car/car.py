import datetime

class Car:

    #initializer
    def __init__(self, model, manufacturer, style, color, engine, year, doors, price):
        self.model = model
        self.manufacturer = manufacturer
        self.style = style #Sedan, SUV, Coupe...
        self.color = color
        self.engine = engine
        self.year = year
        self.doors = doors
        self.price = price

    # função para calcular idade do carro
    def carAge(self):
        today = datetime.datetime.now() 
        return (today.year - self.year)

    
    #função retorna a diferença do valor do carro com a fipe
    def calcFipe(self, fipePrice):
        return (self.price - fipePrice)
    

        
    
      