"""Majuscules"""
#Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.
#
#
#Exemples d’utilisation :
#$> python exo.py “bonjour mathilde, comment vas-tu ?!”
#Bonjour Mathilde, Comment Vas-tu ?!
#
#
#$> python exo.py 42
#error
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

user_expr = sys.argv[1:]

if sys.argv[1].isdigit() or len(sys.argv) < 2:
    print("error")
    sys.exit()

test = str("".join(user_expr))
test2 = test.title(); print(test2)


