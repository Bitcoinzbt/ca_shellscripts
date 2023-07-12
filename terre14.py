"""Créez un programme qui détermine si une liste d’entiers est triée ou pas.
Exemples d’utilisation :
$> ruby exo.rb 9 8 3
Pas triée !
$> ruby exo.rb 3 8 9 12
Triée !
$> ruby exo.rb “Salut”
erreur."""

from sys import argv

try:
    liste = [int(arg) for arg in argv[1:]]
except ValueError:
    print("Attention : veuillez saisir des entiers uniquement.")
    exit()

lenght = len(argv[1:])
counter = 0
#print(lenght)


for i in range(1, lenght):
    if int(argv[i]) < int(argv[i + 1]):
        #print((argv[i], argv[i + 1]), "triée")        
        counter += 1

#print(counter)
if counter == lenght - 1:
    print("Votre liste est triée")
else:
    print("Votre liste n'est pas triée")


