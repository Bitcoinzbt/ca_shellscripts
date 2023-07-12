"""Split en fonction de"""


#Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.
#
#Votre programme devra intégrer une fonction prototypée comme ceci :

"""ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
#	# votre algorithme
#	return (tableau)"""
#}
#
#
#Exemples d’utilisation :
#$> python exo.py “Crevette magique dans la mer des étoiles” “la”
#Crevette magique dans 
# mer des étoiles
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""----------------------------------------------------------------------------------------------------------------"""

import sys


string = sys.argv[1]
separateur = sys.argv[2]


if len(sys.argv) < 2:
    print("error")
    sys.exit()

def en_fonction_de(string, separateur):
    if separateur in string:
        result = string.split(separateur)
    return result
    
result = en_fonction_de(string, separateur)
for element in result:
    print(element)


