class Rettangolo:
    def __init__(self, base, altezza):
        self.__base = base
        self.__altezza = altezza

    @property

    def area(self):
        return self.__base * self.__altezza
    
    #GETTER si occupano di prendere e restituirci dei valori
    @property #e comodo usarlo con property
    def get_altezza(self):
        return self.__altezza
    
    #SETTER si occupa di settare una variabile
    def set__altezza(self, h):
        self.__altezza = h
    
r = Rettangolo(6, 34)
print(r.area)

# i metodi privati sono definiti con __ doppio underscore
# i metodi protetti sono definiti con _ singolo underscore
