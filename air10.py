""" Afficher le contenu"""

#Créez un programme qui affiche le contenu d’un fichier donné en argument.
#
#
#Exemples d’utilisation :
#$> cat a.txt
#Je danse le mia
#$> ruby exo.rb “a.txt”
#Je danse le mia
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible
"""----------------------------------------------------------------------------------------------------------"""
import subprocess

nom_fichier = "air09.py"


subprocess.run(["cat", "air09.py"])
print("\n")




