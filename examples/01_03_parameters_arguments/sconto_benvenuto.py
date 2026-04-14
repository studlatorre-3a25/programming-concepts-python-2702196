def applica_sconto_benvenuto(prezzo_iniziale):
    return prezzo_iniziale - 5
prezzo_pantaloni = 30
prezzo_maglietta = 25
prezzo_scarpe = 80
oggetto= input("cosa vuoi comprare? ")
print("il prezzo iniziale dei prodotti è:", "pantaloni", prezzo_pantaloni, "maglietta", prezzo_maglietta, "scarpe", prezzo_scarpe)
if oggetto == "pantaloni":
    prezzo_finale = applica_sconto_benvenuto(prezzo_pantaloni)
elif oggetto == "maglietta":
    prezzo_finale = applica_sconto_benvenuto(prezzo_maglietta)
elif oggetto == "scarpe":
    prezzo_finale = applica_sconto_benvenuto(prezzo_scarpe)
print("il prezzo finale è:", prezzo_finale)
