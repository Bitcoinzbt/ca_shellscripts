"""Majuscule sur deux"""

#Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.
#
#
#Exemples d’utilisation :
#$> python exo.py “Hello world !”
#HeLlO wOrLd !
#
#
#$> python exo.py 42
#error
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys



def une_maj_sur_deux(user_str):
    new_str = ""
    for i in range(0, len(user_str)):
        if i % 2 == 0:
            new_str = new_str + user_str[i].lower()
        else:
            new_str = new_str + user_str[i].upper()
    print(new_str)


arg = sys.argv[len(sys.argv[1:])]

if len(sys.argv) > 1 and not arg.isdigit():
    user_str = " ".join(sys.argv[1:])
    une_maj_sur_deux(user_str)
else:
    print("error")
    sys.exit()






    








