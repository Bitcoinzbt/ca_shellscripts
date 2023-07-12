"""Tri par selection"""

#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.
#
#Vous utiliserez une fonction de cette forme (selon votre langage) :
#my_select_sort(array) {
#	# votre algorithme
#	return (new_array)
#}
#
#
#Exemples d’utilisation :
#$> python exo.py 6 5 4 3 2 1
#1 2 3 4 5 6
#
#
#$> python exo.py test test test
#error
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys
import os
os.system('clear')

# Traitement des erreurs d'arguments
try:
    liste = [int(arg) for arg in sys.argv[1:]]    
except ValueError:
    print("ATTENTION ! Seuls les nombres entiers seront traités.")
    sys.exit()

if len(liste) < 2:
    print("Erreur, saisissez au moins deux entiers.")
    sys.exit()


liste_triee = []

# Cette fonction procède au tri des arguments saisis par l'utilisateur.
def tri_selectif(liste):
    n = len(liste) - 1
    for i in range(n):
        for j in range(0,n,1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                print(liste) # Facultatif // Afiche les étapes du tri
    return liste

print(tri_selectif(liste))


