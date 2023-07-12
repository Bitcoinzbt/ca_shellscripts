import os
import subprocess

args_user = {
    "air00.py": ["Bonjour les gars"],
    "air01.py": ['Crevette magique dans la mer des étoiles', 'la'],
    "air02.py": ["Je", "teste", "des", "trucs", " "],
    "air03.py": ["1 2 3 4 5 4 3 2 1"],
    "air04.py": ["Hello milady,   bien ou quoi ??"],
    "air05.py": ["1 2 3 4 5" "+2"],
    "air06.py": ["Michel", "Albert", "Therese", "Benoit", "a"],
    "air07.py": ["1" "3" "4" "2"],
    "air08.py": ["10 20 30 fusion 15 25 35"],
    "air09.py": ["Michel", "Albert", "Therese", "Benoit"],
    "air10.py": ['air06.py'],
    "air11.py": ["0", "5"],
    "air12.py": ["6" "5" "4" "3" "2" "1"],
}

nbre_de_test = 0
compteur_success = 0
final_success = 0

def test_run(args_user):
    global final_success
    for item in args_user.items():
        script, args = item
        if script in os.listdir('.'):
            total_sucess = f"{(compteur_success + 1)} / {(nbre_de_test + 1)}"
            final_success += 1

            try:
                subprocess.run(['python', script] + args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                total_success2 = f"{(compteur_success + 2)}/{(nbre_de_test + 2)}"
                print(script, total_success2, " = Success")
                final_success += 1
            except subprocess.CalledProcessError:
                total_success3 = f"{compteur_success + 1}/{compteur_success + 2}"
                print(script, total_success3, " = Failure")
        else:
            print("Fichier non trouvé.")
    return final_success
    
resultat = test_run(args_user)
print(f"final success = {final_success}/26")

