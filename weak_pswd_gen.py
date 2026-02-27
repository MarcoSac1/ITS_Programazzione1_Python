import string
import random

length = int(input("Inserisci la lunghezza desiderata della password: "))

print('''scegli il set di caratteri da usare nella password :
        1. Numeri
        2. Lettere
        3. Caratteri speciali
        4. Lettere maiuscole
        5. Exit''')

listadichar=""

while(True):
    scelta = int(input("scegli un numero oppure inserisci 5 per uscire e generare la password: "))
    if(scelta == 1):
        listadichar+=string.ascii_letters
        
    elif(scelta ==2):
        listadichar+= string.digits
        
    elif(scelta ==3):
        listadichar+= string.punctuation
        
    elif(scelta==4):
        listadichar+= string.ascii_uppercase
        
    elif(scelta==5):
        break
    
    else:
        print("Perfavore scegli un' opzione valida!")
        

pswd =[]

for i in range (length):
    
    char_random = random.choice(listadichar)
    
    pswd.append(char_random)

print("La tua password randomica e'" + "".join(pswd))