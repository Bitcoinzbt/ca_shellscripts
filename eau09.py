"""Entre Min et Max"""
#Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.

#$> python exo.py 20 25
#20 21 22 23 24
#
#
#$> python exo.py 25 20
#20 21 22 23 24
#
#$> python exo.py hello
#error


import sys
import os

os.system('clear')

if len(sys.argv) != 3 or str(sys.argv[1:]).isalpha():
    print("Erreur, vous devez saisir deux entiers")
    sys.exit()

    
user_args = str(sys.argv[1:])
user1 = int(sys.argv[1])
user2 = int(sys.argv[2])

liste = []
    
def min_max(user1,user2):
    a = min(user1, user2)
    b = max(user1, user2)
    for i in range(a, b):
        liste.append(i)
        resultat = ', '.join(map(str, liste))
    return resultat

print(min_max(user1, user2))








