#Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.
#Exemples d’utilisation :
#$> python exo.py 5 2
#résultat: 2
#reste: 1
#$> python exo.py 10 0
#erreur.
#$> python exo.py 3 5
#erreur.

#====================================== DIVISIONS =========================================

from sys import argv

liste = []
for arg in argv[1:]:
    if arg.isdigit():
        liste.append(int(arg))
    else:
        print("Faut pas pousser !!")
        exit()


a = int(argv[1])
b = int(argv[2])

if a == 0 or b == 0:
    print("erreur !!")
else:
    if a >= b:
        result = int(a/b)     
        print(f"Résultat = {result}")

        rest = a % b
        print(f"Reste : {rest}")
    else:
        print("erreur !")
