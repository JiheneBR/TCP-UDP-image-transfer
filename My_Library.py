import os
import subprocess

def clear():

    # Détermination de la commande selon le système
    commande = 'cls' if os.name == 'nt' else 'clear'

    # Exécution de la commande
    subprocess.run(commande, shell=True)