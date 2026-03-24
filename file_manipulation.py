import os
"""
r -> legge e se non esiste eccezione(cursore all'inizio del fine)
r+ -> legge o scrive e se non esiste eccezione (cursore all'inizio del file)
w -> scrive e se non esiste crea, se esiste sovrascrive(cursore all'inizio del file)
w+ -> scrive/legge e se non esiste crea, se esiste sovrascrive(cursore al inizio del file)
a -> scrive e se non esiste crea, se esiste NON sovrascrive (cursore alla fine del file)
a+ -> scrive / legge e se non esiste crea, se esiste NON sovrascrive (cursore alla fine del file)
"""
d = dict ()#cosi' crea un dizionario (json)

#with open("test.ini", 'w') as f:
#    a = ""
#    while a != "EOF":
#        a = input ("Inserisci il testo: ")
#        if a != "EOF":
#            f.write(a)
#    f.close()

with open("test.ini", "r") as f:
    l = f.readlines()
    section = []
    
    for line in l:
        line = line.strip()
        if len(line) <= 0:
            continue
        if line[0] == '#' or line[0] == ";":
            continue
        if line == "\n":
            continue
        if "=" in line:
            v = line.split("=")
            if section:
                d[section][v[0]] ="".join(v[1:])
            else:
                d[v[0]] ="".join(v[1:])
        if line[0] == "[" and line [-1] == "]": 
            d[line[1:-1]] = dict()
            section = line [1:-1]
    f.close()

exit()