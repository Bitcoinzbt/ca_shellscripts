#Combinaisons de 3 chiffres
"""Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant,
   dans l’ordre croissant. La répétition est volontaire."""




for i in range(10):
    for j in range(10):
        for k in range(10):        
            if i >= j or j >= k:  # Seulement deux conditions.
                continue 
            else:
                print(f"{i}{j}{k}", end = " ")  # Affiche cette fois la solution.
            
print("\n")