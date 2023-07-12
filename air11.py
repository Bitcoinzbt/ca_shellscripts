"""Afficher une pyramide"""


#Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.
#
#
#Exemples d’utilisation :
#$> ruby exo.rb O 5
#    O
#   OOO
#  OOOOO
# OOOOOOO
#OOOOOOOOO
#
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
"""-----------------------------------------------------------------------------------------"""

import sys

motif_choisi = sys.argv[1]
loop = int(sys.argv[2])
nombre_de_motifs_max = (loop*2) - 1


for i in range(1, nombre_de_motifs_max + 1, 2):
        count_int = (nombre_de_motifs_max - i) // 2
        print(" " * count_int + motif_choisi * i)

        



               










