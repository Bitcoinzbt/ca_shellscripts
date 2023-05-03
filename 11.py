#Créez un programme qui transforme une heure affichée en format 24h en une heure affichée au format 12h.
#
#
#Exemples d’utilisation :
#$> ruby exo.rb 23:40
#11:40PM
#
#Attention : midi et minuit.

#============================= 24 to 12 ==================================

from sys import argv
import os

#os.system('clear')

#print(argv, len(argv), type(argv[1]))

heure = []

for i in argv[1]:
    heure.append(i)
#print(heure[0:2])
heures = int("".join(heure[0:2]))
#print(heures)

if heures >= 12 and heures < 24:
    english_hour = heures - 12
    print(english_hour,":",int("".join(heure[3:5])),"PM")
elif heures < 12:
    english_hour = heures
    print(english_hour,":",int("".join(heure[3:5])),"AM")

    






    
