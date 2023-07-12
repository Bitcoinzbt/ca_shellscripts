"""Sur chacun d’entre eux"""


#Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste.
#
#
#Exemples d’utilisation :
#$> ruby exo.rb 1 2 3 4 5 “+2”
#3 4 5 6 7
#
#$> ruby exo.rb 10 11 12 20 “-5”
#5 6 7 15
#
#
#L’opération à appliquer sera toujours le dernier élément.
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

liste = sys.argv[1:-1]
operation = "".join(sys.argv[-1])

for element in liste:
    element = "".join(element)
    if operation[0] == "+":
        resultat = int(element) + int(operation[1])
    elif operation[0] == "-":
        resultat = int(element) - int(operation[1])
    print(resultat)

