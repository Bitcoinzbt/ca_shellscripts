#Créez un programme qui affiche la racine carrée d’un entier positif.
#
#
#Exemples d’utilisation :
#$> node exo.js 9
#3
#
#Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

#=================================== RACINE CAREE =======================================


from sys import argv

from math import sqrt


     
if len(argv) > 2 or not argv[1].isdigit():
    print("Erreur !!")
elif argv[1] == "0" or int(argv[1]) < 0:
        print("Cet argument n'est pas recevable")
else:
    arg = int(argv[1])
    racine = sqrt(arg)
    print(racine)




