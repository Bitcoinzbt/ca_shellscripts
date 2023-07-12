"""String in string"""

#Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.
#
#
#Exemples d’utilisation :
#$> python exo.py bonjour jour
#true
#
#
#$> python exo.py bonjour joure
#false
#
#
#$> python exo.py 42
#error
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys


if len(sys.argv) <= 2:
    print("error")
    sys.exit()

def find_str(arg1, arg2):
    if arg1.find(arg2) != -1: # la methode .find() renvoie -1 quand il n'y a pas de concordance et l'index de la premiere occurence trouvée sinon.
        return True
    return False

arg1 = sys.argv[1]
arg2 = sys.argv[2]
result = find_str(arg1, arg2)
print(result)
