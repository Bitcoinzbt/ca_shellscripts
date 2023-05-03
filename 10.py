#Créez un programme qui affiche si un nombre est premier ou pas.
#
#
#Exemples d’utilisation :
#$> node exo.js 5
#Oui, 5 est un nombre premier.
#
#$> node exo.js 6
#Non, 6 n’est pas un nombre premier.
#
#Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.

from sys import argv

liste = []
for arg in argv[1:]:
    if arg.isdigit():
        liste.append(int(arg))
    else:
        print("Vous faites erreur tres cher(e) !!")
        exit()


if argv[1] == "0" or argv[1] == "1":
    print("Attention : ni 0, ni 1 ne peuvent etre considérés comme des nombres premiers.")
else:
    arg = int(argv[1])
    liste = []
    for i in range(2, arg):
        result = (arg % i)
        liste.append(result)
    occurences = liste.count(0)

    if occurences > 0:
        print("pas premier")
    else:
         print("premier")

    



        
    



    
    
    





    







