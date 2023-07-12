


import time

ma_conclusion = "J'ai fini les épreuves de la Terre, et...\nJe me suis pris pour Dieu durant 10 jours !!"
chaine = ("".join(ma_conclusion))

for lettre in chaine:
    print(lettre, end="", flush=True)
    time.sleep(0.10)

print("\n")