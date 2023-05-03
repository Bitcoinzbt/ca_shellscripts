#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.
#Exemples d’utilisation :
#$> python exo.py n
#nopqrstuvwxyz
#$>
#Attention : votre programme devra utiliser une boucle.


from sys import argv

alphabet = "abcdefghijklmnopqrstuvwxyz"
counter = 0

for letter in alphabet:
    counter += 1
    if letter == argv[1]:
        index = (counter-1)
        suite = alphabet[index:]
        print(f"Voici l'alphabet a partir de la lettre {letter} que vous avez choisi : \n{suite} ;-)", end = "")
print("\n")





    

        





