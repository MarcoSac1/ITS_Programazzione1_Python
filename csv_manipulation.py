import csv

file_path = "/home/marco/Documenti/studenti.csv"
    
try:    
    righe_aggiornate = []
    with open(file_path, newline="") as csvfile:
        lettore = csv.reader(csvfile, delimiter=",")
        
        intestazione = next(lettore)
        intestazione.append("Esito")
        righe_aggiornate.append(intestazione)
        
        for riga in lettore:
            voto = int(riga[2])
            if voto >= 6:
                esito = "Approvato"
            else:
                esito = "Non approvato"
            riga.append(esito)
            righe_aggiornate.append(riga)
            
    with open(file_path, "w", newline="") as csvfile:
        scrittore = csv.writer(csvfile)
        scrittore.writerows(righe_aggiornate)
        
    print("File aggiornato")
    
except FileNotFoundError:
    print("Il non esiste")
    
print(righe_aggiornate)