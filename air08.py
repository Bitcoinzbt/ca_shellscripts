"""Mélanger deux tbaleau triés"""


#Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.
#
#Utilisez une fonction de ce genre (selon votre langage) :
#sorted_fusion(array1, array2) {
#	# your algo
#	return (split_array)
#}
#
#
#Exemples d’utilisation :
#$> ruby exo.rb 10 20 30 fusion 15 25 35
#10 15 20 25 30 35
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""----------------------------------------------------------------------------------------------------"""

import sys

array = " ".join(sys.argv[1:])

try: # Teste la présence de l'argument "fusion" dans la chaine de caracteres array constituée à l'aide de la methode "".join()
    if "fusion" not in array:
        raise ValueError
    split_array = array.split("fusion ")
    print(split_array)
    array1 = [element for element in split_array[0].split()]
    array2 = [element for element in split_array[-1].split()]
except ValueError:
    print("erreur, l'argument 'fusion' doit séparer vos deux listes d'entiers")
    sys.exit()

# Tri  + fusion des deux listes
def sorted_fusion(array1, array2):
    liste_triee = sorted(array1 + array2)
    return liste_triee

try: # Retourne une erreur si une lettre est saisie par erreur dans la liste de nombres avant "fusion"
    for element in array1:
        if not element.isdigit():
            raise ValueError
except ValueError:
        print("erreur, vous avez saisi une lettre en trop !")
        sys.exit()

try: # Retourne une erreur si une lettre est saisie par erreur dans la liste de nombres apres "fusion"
    for element in array2:
        if not element.isdigit():
            raise ValueError
except ValueError:
        print("erreur, vous avez saisi une lettre en trop !")
        sys.exit()

resultat = " ".join(sorted_fusion(array1, array2))
print(resultat)









   








