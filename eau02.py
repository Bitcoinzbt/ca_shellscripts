"""Parametres  à l'envers"""
#Créez un programme qui affiche ses arguments reçus à l’envers.
#
#Exemples d’utilisation :
#$> python exo.py “Suis” “Je” “Drôle”
#Drôle
#Je
#Suis
#$> python exo.py ha ho
#ho
#ha
#
#$> python exo.py “Bonjour 36”
#Bonjour 36
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.

from sys import argv

arg = argv[1:]
if arg == [] or len(arg) < 2:
    print("Error")
    exit()

arg.reverse() # Pas sur d'avoir droit a rev
print(str(" \n".join(arg)))






