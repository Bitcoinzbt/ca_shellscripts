from sys import argv



a, b, c = int(argv[1]), int(argv[2]), int(argv[3])

if a == b == c:
    print("erreur")
elif a < b < c or c < b < a:
    print(b)
elif b < a < c or c < a < b:
    print(a)
else:
    print(c)


