import sys
import os
os.system('clear')



def conversion(user_list):
    ascii_list = []
    for arg in user_list:
        key = arg[0]
        if key in ascii:
            value = ascii[key]
            ascii_list.append(value)
    return ascii_list


def tri(ascii_list):
     n = len(ascii_list)
     for i in range(n):
        for j in range(0, n - 1, 1):
            if ascii_list[j] > ascii_list[j + 1]:
                ascii_list[j], ascii_list[j + 1] = ascii_list[j + 1], ascii_list[j]
     return ascii_list

# Comprehension _list :
user_list = [element for element in sys.argv[1:] if not element.isdigit() and element.istitle()]

if len(sys.argv[1:]) < 2:
    print("Erreur.")
    sys.exit()

majuscules = [chr(n) for n in range(65, 91)]
numbers = [n for n in range(65, 91)]
ascii = {cle: valeur for cle, valeur in zip(majuscules, numbers)}

resultat = " ".join(tri(user_list))
print(resultat)