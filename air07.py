"""Insertion dans un tebleau trié"""


#Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.
#
#Utilisez une fonction de ce genre (selon votre langage) :
"""sorted_insert(array, new_element) {
	# your algo
	return (new_array)"""
#}
#Exemples d’utilisation :
#$> ruby exo.rb 1 3 4 2
#1 2 3 4
#
#$> ruby exo.rb 10 20 30 40 50 60 70 90 33
#10 20 30 33 40 50 60 70 90
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""----------------------------------------------------------------------------------------"""


import sys

array = [int(element) for element in sys.argv[1:-1]]
new_element = int(sys.argv[-1])
#print(array, type(array[0]), new_element, type(new_element))


def tri_selectif(array):
    n = len(array) - 1 # important de definir "n" dans la fonction car la longueur de new_list est plus longue d'un argument. Error si n definie ailleurs.
    for i in range(n):
        for j in range(0,n,1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array # Grrrr ! ces return mal indentés 

new_list = tri_selectif(array)
new_list.append(new_element)


final_list = tri_selectif(new_list)
print(*final_list)  # Cette synthaxe permet d'afficher les arguments séparés d'un espace sans nécessiter de boucle pour l'affichage ( merci Chat GPT pour cette astuce)!!










    
    






