# 📚 Système de Gestion de Bibliothèque - Book Store

Bienvenue dans l'application **Book Store** !  
Cette application permet de gérer des livres, utilisateurs, emprunts et retours dans une bibliothèque virtuelle.

---

## ⚙️ Installation de l’environnement virtuel

```bash
# 1. Créer l'environnement virtuel
python3 -m venv env

# 2. Activer l'environnement
# Sur Linux/macOS :
source env/bin/activate

# Sur Windows :
env\Scripts\activate

# 3. Installer les dépendances (si vous avez un fichier requirements.txt)
pip install -r requirements.txt
```

▶️ Lancer le programme

```bash
python main.py
```

### 🔍 Fonctionnalités

    📖 Voir les livres disponibles

    🔍 Rechercher un livre

    ⚙️ Ajouter / Supprimer / Modifier des livres

    👤 Ajouter un utilisateur

    📥 Emprunter un livre (avec validation utilisateur)

    📤 Retourner un livre

    📋 Afficher les utilisateurs enregistrés

### 📁 Structure du projet

```bash
    systeme_de_gestion_bibliotheque/
│
├── main.py
├── bibliotheque/
│   ├── books/
│   │   └── book.py
│   ├── data/
│   │   └── data.py
├── user/
│   ├── myUser.py
│   └── utilisateur/
│       └── utilisateurs.py
├── env/
└── README.md
```

Auteur :

```bash
Sabbat Lumpantshia
```
