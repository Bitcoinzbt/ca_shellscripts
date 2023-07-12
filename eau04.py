"""Prochain nombre premier"""
# Ecrire un programme qui affiche le nombre premier immediatement consecutif a l'entrée de l'utilisateur

import sys


def test_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # n**0.5 revient a calculer la sqrt ( racine carrée de n )
        if n % i == 0:
            return False
    return True

def premier_sup(arg): # cette fonction teste tous les arguments apres "arg" jusqu'a True
    i = arg + 1
    while True:
        if test_premier(i):
            return i
        i += 1

if sys.argv[1:] == [] or int(sys.argv[1]) <= 0:
    print("-1")
    sys.exit(1)
arg = int(sys.argv[1])
resultat = premier_sup(arg)
print(resultat)



