import random
n = random.randint(1, 100)


while True:
    nU = int(input("Inserisci un numero prova ad indovinare il numero randomico tra 1 e 100: "))
    if nU > n :
        print("Troppo alto")
    elif nU < n:
        print("Troppo basso")
    else:
        print("indovinato")
        break

print(f"il numero generato randomicamente é {n}")

print(f"il numero inserito da te é{nU}")
