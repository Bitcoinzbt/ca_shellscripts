"""Difference minimum absolue"""

#Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.
#
#
#Exemples d’utilisation :
#$> python exo.py 5 1 19 21
#2
#
#
#$> python exo.py 20 5 1 19 21
#1
#
#$> python exo.py -8 -6 4
#2
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

if len(sys.argv) < 3:
    print("erreur, veuillez saisir au moins deux nombres.")
    sys.exit()

nbrs = [abs(int(element)) for element in sys.argv[1:]]

def tri(nbrs):
    liste_triee = sorted(nbrs)
    return liste_triee

liste_resultats = []

liste_triee = tri(nbrs)
for idx in range(len(sys.argv)):
    for i in range(idx + 1, (len(sys.argv) - 1)):
        result = abs(liste_triee[idx] - liste_triee[i])
        liste_resultats.append(result)
        #print(f"{liste_triee[idx]} - {liste_triee[i]} = {result}")

print(min(liste_resultats))
        



    







