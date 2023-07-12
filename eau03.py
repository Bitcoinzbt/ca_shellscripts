"""Suite de FIBONACCI"""
#Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.
#
#
#Exemples d’utilisation :
#$> python exo.py 3
#2
#$>
#
#Afficher -1 si le paramètre est négatif ou mauvais.


from sys import argv

if len(argv) < 2 or int(argv[1]) <= 0:
    print("-1")
    exit()


suite = [0,1]
n = int(argv[1])
a = 0
b = 1

for i in range(2, n + 1):
    c = a + b
    #print(c)
    suite.append(c)
    a = b
    b = c

print(suite[n])





