from mio_modulo import *

def main():
    a = int(input("inserisci la variabile a:"))
    b = int(input("inserisci la variabile b:"))
    print(moltiplica(a, b))     # <- modulo. funzione
    
    nome = input("inserisci il nome della persona da salutare: ")
    print(saluta(nome))

if __name__ == "__main__":
    main()
