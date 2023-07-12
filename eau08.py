"""Chiffres only"""

#Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.
#
#
#Exemples d’utilisation :
#$> python exo.py “4445353”
#true
#
#
#$> python exo.py 42
#true
#
#$> python exo.py “Bonjour 36”
#false
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

user_expr = str("".join(sys.argv[1:]))

if len(sys.argv) < 2:
    print("error")
    sys.exit()

def chiffre_ou_pas(user_expr):
    for element in user_expr:
        if element.isalpha():
            return False
    return True

print(chiffre_ou_pas(user_expr))




