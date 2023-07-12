"""Index Wanted"""
#Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de tous les arguments sauf le dernier. L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.
#
#
#Exemples d’utilisation :
#$> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
#6
#
#
#$> python exo.py test test test
#0
#
#$> python exo.py test boom
#-1
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys



user_expr = sys.argv[1:-1]
last_arg = sys.argv[-1]

if len(sys.argv) == 1:
    print("vous devez saisir une phrase")

for element in user_expr:
    if element == last_arg:
        index = user_expr.index(element)
        print(index)
        break
    else:
        print("Aucune correspondance")
        break


    #else:
    #    last_arg = last_arg.upper()
    #    print(f"Désolé aucune correspondance dans votre pharse avec l'argument {last_arg} ;-)")
    #    sys.exit()
    
