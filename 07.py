# Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.
# attendu : python3 07.py "bonjour" > 7

# Traiter les exceptions : 
# python3 07.py > Erreur!
# python3 07.py 18 > Erreur!
# python3 07.py "bonjour" "Aurevoir" > Erreur!

from sys import argv


arg = argv[1:]

if arg == [] or (argv[1].isdigit() or len(argv[0:]) > 2):
    print("Erreur !")

else:
    print(len(argv[1]))

