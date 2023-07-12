#Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.
#
#Exemples d’utilisation :
#$> node exo.js “Hello world!”
#!dlrow olleH
#$> node exo.js “lehciM”
#Michel
#Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

#========================================== INVERSER UNE CHAINE ==========================================

from sys import argv

string = argv[1:]

if string == [] or argv[1].isdigit():
    print("Vous devez saisir une chaine de caracteres. \nUn mot par exemple.")
else:
    for i in string:
        print(i[::-1])
     








