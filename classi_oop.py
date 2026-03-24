import math #importo la libreria math per poter usare il phigreco

class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio
        pass
    
    def area(self):
        return math.pi * (self.raggio**2)
    
    def perimetro(self):
        return 2*math.pi*self.raggio
    
c = Cerchio(4)

print("l\'area è di:",round(c.area(), 2))
print("il perimetro è:", round(c.perimetro(), 2))