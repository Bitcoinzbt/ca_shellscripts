"""Chercher l'intrus"""

#Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.
#
#
#Exemples d’utilisation :
#$> python exo.py 1 2 3 4 5 4 3 2 1
#5
#
#$> python exo.py bonjour monsieur bonjour
#monsieur
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

liste = sys.argv[1:]

if len(liste) < 3:
    print("error")
    sys.exit()

chaine = [arg for arg in liste if not liste.count(arg) >= 2]

print("".join(chaine))