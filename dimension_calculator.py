frase_da_aggiungere = "ciao file io ti ho appena modificato\n"  # La tua stringa + \n

file = open("/home/marco/Documenti/esercizio.txt", "r+")

# Vai all'inizio e leggi tutto
file.seek(0)
contenuto = file.read()

# Controlla se la frase esiste già (case-sensitive, ignora spazi finali)
if frase_da_aggiungere.strip() not in contenuto:
    print("Frase non trovata: la aggiungo.")
    
    # Vai in fondo al file
    file.seek(0, 2)
    
    # Scrivi la frase
    file.write(frase_da_aggiungere)
    
    print("File modificato con successo!")
else:
    print("File già modificato: frase già presente.")

# Debug: rileggi e mostra
file.seek(0)
file_modificato = file.read()
print("Contenuto finale:",(file_modificato))  # repr() mostra \n e spazi

# Dimensione file in byte
file.seek(0, 2)
dimensione = file.tell()
print("Dimensione file:", dimensione, "byte")

file.close()
