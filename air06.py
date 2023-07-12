"""Controle de pass sanitaire"""


#Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.
#
#Utilisez une fonction de ce genre (selon votre langage) :
"""ma_fonction(array_de_strings, string) {
#	# votre algorithme
#	return (nouvel_array_de_strings)"""
#}
#
#
#Exemples d’utilisation :
#$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “t”
#Michel
#
#$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “a”
#Michel, Thérèse, Benoit
#
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""----------------------------------------------------------------------------------------------------------"""

import sys

def san_pass(liste,test):
    liste_triee = [arg for arg in liste if test.upper() in arg or test.lower() in arg]
    print(liste_triee)
    return liste_triee

liste = sys.argv[1:-1]
test = "".join(sys.argv[-1])

san_pass(liste,test)












