#Créez un programme qui affiche le résultat d’une puissance.
#
#L’exposant ne pourra pas être négatif.
#
#Exemples d’utilisation :
#$> node exo.js 2 3
#8
#Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments

#=================================== PUISSANCE D'UN NOMBRE ==================================

from sys import argv


if len(argv) < 3 or not argv[2].isdigit():
    print("erreur !")
#elif sys.argv[1] == "0" or sys.argv[2] == "0":
#    print(f"Erreur ! \nVous ne pouvez pas élever {sys.argv[1]} à la puissance {sys.argv[2]}")
else: 
    nbre1, nbre2 = argv[1], argv[2]
    if int(nbre2) >= 0:  
        result = int(nbre1) ** int(nbre2)
        if result> 100000:
            print("{:e}".format(result))
        else:
            print(result)
    else:
        print("erreur!")



