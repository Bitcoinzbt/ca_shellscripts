#Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.
#
#Exemples d’utilisation :
#$> node exo.js “Hello world!”
#!dlrow olleH
#$> node exo.js “lehciM”
#Michel
#Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

#========================================== INVERSER UNE CHAINE ==========================================

import sys

string = sys.argv[1:]

if string == [] or sys.argv[1].isdigit():
    print("Vous devez saisir une chaine de caracteres")
else:
    for i in string:
        print(i[::-1])






