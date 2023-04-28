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

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

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
