def menu():
    print("""
        1)Segui la lezione
        2)Quitta la lezione
        3)pausa
    """)
    try:
        scelta = int(input("Inserisci la tua opzione:"))
        return scelta
    except ValueError:
        print("Scelta non valida")
        return menu()
scelta = menu()
print("Hai scelto", scelta)