reddito = float(input("Inserisci il tuo reddito annuale: $"))
tasse = 0
if reddito > 60000:
    tasse += (reddito -60000) * 0.30
    reddito= 60000
if reddito > 30000:
    tasse += (reddito - 30000) * 0.20
    reddito = 30000
if reddito > 10000:
    tasse += (reddito -10000) * 0.10

print(f"Le tasse da pagare sono: ${tasse}")
