"""Split"""

#Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).
#
#Votre programme devra utiliser une fonction prototypée comme ceci :
#ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
#	# votre algorithme
#	return (tableau)
#}
#
#
#Exemples d’utilisation :
#$> python exo.py “Bonjour les gars”
#Bonjour
#les
#gars
#
#Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

if len(sys.argv) != 2:
    print("error")
    sys.exit()

chaine = [sys.argv[1]]
chaine = " ".join(chaine)
separateurs = [" ", "\t", "\n"]

def cutter(chaine, *separateurs):
    for separateur in separateurs:
        if separateur in chaine:
            resultat = chaine.split(separateur)
            cutted_list = [element for element in resultat]
    return cutted_list


for i in cutter(chaine, *separateurs):
    print(i)