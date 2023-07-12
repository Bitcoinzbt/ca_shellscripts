"""Rotation vers la gauche"""


#Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.
#
#Utilisez une fonction de ce genre (selon votre langage) :
"""ma_rotation(array) {
#	# votre algorithme
#	return (new_array)
#}"""
#
#
#Exemples d’utilisation :
#$> python exo.py “Michel” “Albert” “Thérèse” “Benoit”
#Albert, Thérèse, Benoit, Michel
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""----------------------------------------------------------------------------------------------------"""

import sys

array = sys.argv[1:]


if len(array) < 2:
    print("error")
    sys.exit()
for element in array:
    if element.isdigit():
        print("error")
        sys.exit(1)

def rotation(array):
    n = len(array)
    pop = array.pop(0)
    array.insert(n, pop)
    print(array)
    return array
   
rotation(array)
rotation(array)
rotation(array) # ca tourne bien ;-)