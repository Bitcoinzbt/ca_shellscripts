"""Tri à bulles"""

#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.
#
#Vous utiliserez une fonction de cette forme (selon votre langage) :
#my_bubble_sort(array) {
#	# votre algorithme
#	return (new_array)
#}
#
#Exemples d’utilisation :
#$> python exo.py 6 5 4 3 2 1
#1 2 3 4 5 6
#
#$> python exo.py test test test
#error
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.



import sys
import os
os.system('clear')

#Gère l'erreur quand l'utilisateur saisi autre chose que des entiers.
try:
    liste = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("Erreur : Vous devez saisir uniquement des nombres entiers.") 
    sys.exit()


def mon_tri_a_bulles(liste):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
                
    return liste

#Gère l'erreur quand l'utilisateur saisi un seul argument.
if len(liste) < 2:
    print("Erreur, vous devez saisir au moins deux nombres entiers.\nPour que je puisse les trier")
    sys.exit()

n = len(liste)
resultat = mon_tri_a_bulles(liste)
print(resultat)
