# Scanner de Ports Docker

Ce projet démontre la conteneurisation d'une application Python (Scanner de ports - Nmap-Lowcost)


## Objectifs Techniques Validés

Ce projet met en œuvre les concepts suivants :
1. **Création d'image Docker** : Utilisation d'un `Dockerfile` optimisé (basé sur python:slim) avec utilisateur non-root.
2. **Orchestration Multi-services** : Utilisation de `compose.yaml` pour orchestrer le scanner et une cible (serveur Nginx).
3. **Gestion des Secrets** : Injection sécurisée d'une clé API via les *Docker Secrets*, sans passer par les variables d'environnement en clair.

## Structure du Projet

* `scanner.py` : Le script Python adapté pour lire les secrets dans `/run/secrets/` et la cible via les variables d'environnement.
* `Dockerfile` : Instructions pour construire l'image du scanner.
* `compose.yaml` : Fichier de définition des services (`mon-scanner` et `ma-victime`).
* `mon_secret.txt` : Fichier contenant le secret (Simulé pour l'exercice).

> **Note de sécurité** : Dans un environnement de production réel, le fichier `mon_secret.txt` ne serait **jamais** commité sur Git. Il est présent ici uniquement dans le cardre éducatif et du projet. 

## Installation et Lancement

### Prérequis
* Docker Desktop & Docker Compose installés.

### Instructions

1.  **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Funeralon/Nmap-lowcost-Docker-.git
    cd Nmap-lowcost-Docker-
    ```

2.  **Lancer l'application** :
    ```bash
    docker compose up --build
    ```
>(Il faut avoir Docker Desktop de lancer pour que )

## Vérification du fonctionnement

Une fois la commande lancée, observez les logs dans le terminal. Le scénario suivant va se dérouler :

1.  **Service `ma-victime`** : Un serveur Nginx démarre sur le port 80 (interne).
2.  **Service `mon-scanner`** : Le script Python démarre, attend la victime, puis lance l'audit.

**Résultat attendu dans les logs :**

```text
mon-scanner-1  | --------------------------------------------------
mon-scanner-1  | Secret chargé avec succès ! Clé utilisée : AZERTY1234
mon-scanner-1  | --------------------------------------------------
mon-scanner-1  | SCANNER DOCKERISÉ - Cible : ma-victime
mon-scanner-1  | --------------------------------------------------
mon-scanner-1  | Port 80 est OUVERT !
mon-scanner-1  | --------------------------------------------------
mon-scanner-1  | Fin du scan containerisé.
mon-scanner-1 exited with code 0

```

- Si vous voyez "Secret chargé", la gestion des secrets fonctionne.

- Si vous voyez "Port 80 OUVERT", la communication inter-services via le réseau Docker fonctionne.

## Détails de configuration

- Target : Le scanner cible le nom d'hôte ma-victime. Docker résout automatiquement ce nom DNS vers l'IP du conteneur Nginx grâce au réseau créé par Compose.

- Sécurité : Le conteneur Python s'exécute avec un utilisateur standard (monuser) défini dans le Dockerfile, et non en root.

# Auteur
Mathieu Dumas