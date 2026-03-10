import math

class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio
        pass
    
    def area(self):
        return math.pi * (self.raggio**2)
    
c = Cerchio(6)
print("l\'area è di :", c.area())