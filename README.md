# Checklist - Formation Administrateur Système & Réseau

Application web de checklist pour suivre la progression d’une formation de 6 mois en administration système et réseau.  
Cette application utilise FastAPI en backend avec authentification JWT, une base PostgreSQL pour stocker utilisateurs et tâches, et un frontend HTML/JS pour interagir.

---

## Fonctionnalités

- Inscription et connexion sécurisées (JWT)
- Gestion personnalisée des tâches/checklists par utilisateur
- Sauvegarde et récupération des progrès
- Export des données en fichier texte
- Interface simple, responsive et intuitive

---

## Prérequis

- Python 3.10+  
- PostgreSQL installé et accessible  
- [Poetry](https://python-poetry.org/) ou `pip` pour gérer les dépendances

---

## Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet
````

2. **Créer la base de données PostgreSQL :**

Se connecter à PostgreSQL et créer la base (exemple) :

```sql
CREATE DATABASE checklist_db;
```

3. **Configurer la connexion à la base** dans `app/database.py` (adapter `DATABASE_URL`) :

```python
DATABASE_URL = "postgresql://user:password@localhost:5432/checklist_db"
```

4. **Créer un environnement virtuel et installer les dépendances :**

```bash
python3 -m venv venv
source venv/bin/activate      # ou équivalent Windows
pip install -r requirements.txt
```

5. **Initialiser la base de données avec Alembic (migration) :**

```bash
alembic upgrade head
```

---

## Lancement de l’application

```bash
uvicorn app.main:app --reload
```

L’API sera accessible sur : `http://localhost:8000`

---

## Utilisation

* Ouvrir le fichier `index.html` dans un navigateur web
* Se connecter ou s’inscrire
* La checklist se charge automatiquement
* Cocher/décocher les tâches pour suivre la progression
* Exporter la progression au format texte
* Réinitialiser la checklist si besoin

---

## Sécurité

* Mot de passe stocké en hash sécurisé (bcrypt)
* Authentification par token JWT avec expiration
* Accès aux données protégés par token

---

## Contributions

Les contributions sont les bienvenues !
Forkez le projet, créez une branche, puis envoyez une pull request.

---

## Licence

Projet sous licence MIT — libre à vous de l’utiliser et modifier.

---

## Contact

Pour toute question, contactez-moi à : [pascalaurel589@gmail.com](mailto:ton.email@example.com)

---

*Bonne formation ! 🚀*
