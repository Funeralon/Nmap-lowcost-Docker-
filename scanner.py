import socket
import sys
import os
from datetime import datetime

# 1. On récupère la cible depuis les variables d'environnement Docker
target = os.getenv('TARGET_HOST')

if not target:
    print("Erreur : Aucune cible spécifiée dans la variable TARGET_HOST")
    sys.exit(1)

# 2. GESTION DES SECRETS 
secret_path = "/run/secrets/mon_super_secret"
api_key = "Inconnu"

#3. Scan des ports
print("-" * 50)
try:
    with open(secret_path, 'r') as secret_file:
        api_key = secret_file.read().strip()
        print(f"Secret chargé avec succès ! Clé utilisée : {api_key}")
except FileNotFoundError:
    print(f"Attention : Le fichier secret n'a pas été trouvé dans {secret_path}")

print("-" * 50)
print(f"SCANNER DOCKER - Cible : {target}")
print("-" * 50)

try:
    for port in range(1, 85): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} est OUVERT !")
        s.close()

except socket.error:
    print("\nImpossible de se connecter au serveur.")
    sys.exit()

print("-" * 50)
print("Fin du scan.")