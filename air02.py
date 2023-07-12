"""Concat"""


#Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme.
#
#Utilisez une fonction de ce genre (selon votre langage) :

"""ma_fonction(array_de_strings, separateur) {
#	# votre algorithme
#	return (string)"""
#}
#
#
#Exemples d’utilisation :
#$> python exo.py “je” “teste” “des” “trucs” “ “
#Je teste des trucs
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""------------------------------------------------------------------------------------------------------------------------------"""

import sys

chaine = sys.argv[1:-1]
print(len(chaine))

if len(chaine) < 2:
    print("error")
    sys.exit()

separateur = sys.argv[-1]

def collage(chaine, separateur):
        liste = separateur.join(chaine)
        return liste

print(collage(chaine, separateur))