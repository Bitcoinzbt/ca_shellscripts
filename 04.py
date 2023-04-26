#Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
#Exemples d’utilisation :
#$> ruby exo.rb 2
#pair
#$> ruby exo.rb 5
#impair
#$> ruby exo.rb Bonjour
#Tu ne me la mettras pas à l’envers.
#
#$> ruby exo.rb
#Tu ne me la mettras pas à l’envers!
#Attention : gérez aussi les entiers négatifs.

#===================================== PAIR OU IMPAIR =========================================

import sys

argument = sys.argv[1]

if argument.isdigit():
    test = (int(sys.argv[1]) % 2)
    if test == 0:
        print("pair")
    else:
        print("impair")
else:
    print("Tu ne me la mettras pas à l’envers !")
    






    





    








#
#if type(sys.argv[1]) == str:
#    print("erreur !")
#test = int(sys.argv[1])
#
#resultat = test % 2
#
#if type(resultat) == str:
#    print("erreur, recommencez")
#elif resultat == 0:
#    print("pair")
#else:
#    print("impair")
#
#print(type(resultat))
#









     













    
    



#if usr_number != int():
#    print("Erreur de saisie, je vous demande un nombre !")
#elif usr_number % 2 == 0:
#    print("pair")
#else:
#    print("impair")



  
    

