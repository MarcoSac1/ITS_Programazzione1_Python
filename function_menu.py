tentativi = 0
max_tentativi = 2
max_scelte = 3

def menu():
    print("""
        1)Segui la lezione
        2)Quitta la lezione
        3)pausa
    """)
    try: 
        if tentativi > max_tentativi:
            print("Troppi tentativi effettuati")
            return None
        scelta = int(input("Inserisci la tua opzione:"))
        if scelta <= 0 or scelta > 3:
            raise  ValueError
        tentativi = 0
        return scelta
    except ValueError:
        print("Scelta non valida")
        return menu()
    
scelta = menu()
print("Hai scelto", scelta)