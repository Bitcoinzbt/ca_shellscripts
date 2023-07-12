# Combinaison de deux nombres

#Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.
#Exemples d’utilisation :
#$> python exo.py
#00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
#$>


import os
os.system('clear')


for i in range(100):
    for j in range(100):
        if i < j:
            print(f"{i}".zfill(2), f"{j}".zfill(2)," ", end = " ")


print("\n")