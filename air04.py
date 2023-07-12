""" Un seul a la fois """


#Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.
#
#
#Exemples d’utilisation :
#$> python exo.py “Hello milady,   bien ou quoi ??”
#Helo milady, bien ou quoi ?
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

string = "".join(sys.argv[1:])
#print(string)

liste = []

def bla(string):
    for i in range(len(string) - 1):
        if string[i] != string[i+1]:    
            liste.append(string[i])
    return liste

bla(string)
liste += string[-1]
print("".join(liste))

    



