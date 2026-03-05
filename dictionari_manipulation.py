import json
import os

percorso = "/home/marco/Documenti/studenti.json"

# Caricamento file sicuro
if os.path.exists(percorso):
    print("Controllo file esistente...")
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            dati = json.load(file)
        print("Tipo dati caricati:", type(dati))
        if isinstance(dati, list):
            studenti = dati
        else:
            print("File non è lista: riparto vuoto")
            studenti = []
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Errore JSON: {e} → Riparto con lista vuota")
        studenti = []
else:
    studenti = []
    print("File non esiste: creo lista vuota")

print("Studenti attuali:", studenti)

# Funzione check duplicati (sicura)
def studente_esiste(nuovo_studente, lista_studenti):
    for s in lista_studenti:
        if isinstance(s, dict) and s.get("nome") == nuovo_studente["nome"]:
            return True
    return False

# Funzione input singolo studente con validazione
def input_nuovo_studente():
    """Chiede dati studente da terminale con validazione"""
    while True:
        nome = input("Inserisci nome studente: ").strip()
        if nome:
            break
        print("Nome non può essere vuoto!")
    
    while True:
        try:
            eta = int(input("Inserisci età: "))
            if 0 < eta < 150:
                break
            print("Età deve essere tra 1 e 149!")
        except ValueError:
            print("Età deve essere un numero!")
    
    citta = input("Inserisci città: ").strip()
    
    return {"nome": nome.capitalize(), "eta": eta, "citta": citta.capitalize()}

# Funzione aggiungi studenti interattivi
def aggiungi_studenti_interattivi(studenti):
    """Aggiunge studenti da input fino a 'q'"""
    while True:
        print("\n" + "="*40)
        print("STUDENTI ATTUALI:", len(studenti))
        print("="*40)
        
        nuovo = input_nuovo_studente()
        
        if studente_esiste(nuovo, studenti):
            print(f"⚠️  Studente '{nuovo['nome']}' esiste già!")
            continua = input("Aggiungere lo stesso? (s/n): ").lower().startswith('s')
            if not continua:
                print("Saltato.")
                scelta = input("Continuare? (s/n/q): ").lower()
                if scelta in ['n', 'q']:
                    break
                continue
        
        studenti.append(nuovo)
        print(f"✅ Aggiunto {nuovo['nome']} da {nuovo['citta']}!")
        
        scelta = input("Aggiungere altro? (s/n/q per quit): ").lower()
        if scelta in ['n', 'q']:
            break
    
    return studenti

# AVVIO PROGRAMMA
print("\n🚀 AVVIO GESTIONE STUDENTI")
print("Premi s per iniziare ad aggiungere studenti, q per uscire senza salvare")

# Studenti di esempio (opzionali - commenta se non vuoi)
studente1 = {"nome": "Franco", "eta": 76, "citta": "Catania"}
if not studente_esiste(studente1, studenti):
    studenti.append(studente1)
    print("📚 Aggiunto Franco (esempio)")

# Menu principale interattivo
while True:
    scelta = input("\n🔄 Cosa fare? (a=aggiungi, v=visualizza, s=salva, q=quit): ").lower()
    
    if scelta == 'a':
        studenti = aggiungi_studenti_interattivi(studenti)
    elif scelta == 'v':
        print("\n📋 LISTA STUDENTI:")
        if studenti:
            for i, s in enumerate(studenti, 1):
                print(f"{i}. {s['nome']} ({s['eta']} anni) - {s['citta']}")
        else:
            print("Nessuno studente!")
    elif scelta == 's':
        with open(percorso, "w", encoding="utf-8") as file:
            json.dump(studenti, file, indent=4, ensure_ascii=False)
        print(f"💾 Salvato {len(studenti)} studenti in {percorso}")
    elif scelta == 'q':
        print("👋 Arrivederci!")
        break
    else:
        print("❌ Scelta non valida!")

# Salva finale automatico
if studenti:
    with open(percorso, "w", encoding="utf-8") as file:
        json.dump(studenti, file, indent=4, ensure_ascii=False)
    print(f"✅ Salvataggio finale: {len(studenti)} studenti")
else:
    print("ℹ️ Nessun studente da salvare")
