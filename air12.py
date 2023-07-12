"""Le roi des tris"""


#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).
#
#Vous utiliserez une fonction de cette forme (selon votre langage) :
#my_quick_sort(array) {
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
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
#
#
#Wikipedia vous présentera une belle description de cet algorithme de tri.
"""---------------------------------------------------------------------------------------------------------"""

import sys

def quicksort(liste):

    if len(liste) <= 1:
        return liste
    
    pivot = liste.pop()

    front_list = []
    back_list = [pivot]

    for element in liste:
        if element < pivot:
            front_list.append(element)
        elif element >= pivot:
            back_list.append(element)
    return quicksort(front_list) + quicksort(back_list)


liste = [int(arg) for arg in sys.argv[1:]]
print(quicksort(liste))