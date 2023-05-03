#Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.
#
#
#Exemples d’utilisation :
#$> ruby exo.rb 11:40PM
#23:40
#
#Attention : midi et minuit.

#=============================== 12 to 24 ================================


from sys import argv

liste = []

#print(argv, len(argv), type(argv[1]))
for i in argv[1]:
    liste.append(i)
#print(liste[0:2])

lettres = str("".join(liste[5:]))
#print(lettres)
heures = int("".join(liste[0:2]))
#print(heures)
minutes = int("".join(liste[3:5]))
#print(french_minutes)

if heures == 12 and lettres == "PM":  # si l'on resprecte la norme internationnale, midi s'ecrit 12:00PM en notation anglosaxone
    print("midi précise !")
elif heures == 12 and lettres == "AM": # si l'on resprecte la norme internationnale, minuit s'ecrit 12:00AM en notation anglosaxone
    print("Minuit")
elif heures < 12 and lettres == "PM":
    french_hour = heures + 12
    print(french_hour,":","{:02d}".format(minutes))
elif heures < 12 and lettres == "AM":
    french_hour = heures
    print(french_hour,":","{:02d}".format(minutes))










