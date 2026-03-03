import mio_modulo

def main():
    a = int(input("inserisci la variabile a:"))
    b = int(input("inserisci la variabile b:"))
    print(mio_modulo.moltiplica(a, b))     # <- modulo. funzione
    
    nome = input("inserisci il nome della persona da salutare: ")
    print(mio_modulo.saluta(nome))

if __name__ == "__main__":
    main()
