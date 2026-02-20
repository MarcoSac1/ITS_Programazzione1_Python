import math
def somma(a, b):
    return a + b

def quad(c):
    return c*c

def area(base, altezza):
    return(base*altezza)/2

def even(a):
    if a%2 == 0:
        return("True")
    else:
        return("False")

def conta_v(parola):
    c = 0
    for a in parola:
        if(a in ("a","e","i","o","u")):
            c += 1
    return c

def equaz_2(a, b, c):
    x1 = (-b+math.sqrt((b * b)- 4 *a *c))/(2 * a)
    x2 = (-b-math.sqrt((b * b)- 4 *a *c))/(2 * a)
    return x1, x2

#def primi(n):
    primi = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primi[p]:
            for i in range( p * p, n + 1, p):
                primi[i] = False
        p += 1
    return [ p for p in range (2, n + 1) if primi[p]]

def primi():        #simone 
    yield 1
    new = 2
    while new < 1000:
        trovato = True
        for i in range (2, new):
            if(new % i == 0 and i != new):
                trovato = False
                break
        if trovato:
            yield new
        new += 1
try:
    gen = primi()
    for i in range(1, 1000):
        print(next(gen))
except StopIteration:
    print("Fine")
    


print("La tua somma e", somma(2, 4))
print("il quadrato e", quad(2))
print("l area e", area(4, 6))
print("il tuo numero e",even(3))
print("la parola inserita ha:", conta_v("australopiteco"), "vocali")
print("la soluzione della tua equazione e:", equaz_2(6, 8, 2))
#print("i numeri primi fino a mille sono:", primi(1000))