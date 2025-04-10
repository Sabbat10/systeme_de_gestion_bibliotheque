from ..data.data import list_users


# Fonction pour afficher la liste des utilisateurs
def display_users():

    if not list_users:
        print("Aucun utilisateur trouvé.")
        return
    
    print("")
    print("📋 Voici la liste des utilisateurs enregistrés :")
    for user in list_users:
        print(f"👤 Nom : {user['name']}")
        print(f"🧒 Prénom : {user['first_name']}")
        print(f"🎂 Âge : {user['age']} ans")
        print(f"📧 Email : {user['email']}")
        print("—" * 40)


# Fonction pour Ajouter un utilisateur à la liste des utilisateurs
def add_user():
    
    name = input("🧑 Votre Nom: ")
    first_name = input("👶 Votre Prénom: ")
    # Vérification de l'âge
    try:
        age = int(input("🎂 Votre Age : ")  )
    except ValueError:
        print("L'âge doit être un nombre entier.")
        return
    email = input("📧 Email: ")
    password = input("🔒 Votre Mot de passe: ")

    # Vérification de l'âge
    if age < 0:
        print("L'âge ne peut pas être négatif.")
        return
    user = {
        "name": name,
        "first_name": first_name,
        "age": age,
        "email": email,
        "password": password,
    }
    
    list_users.append(user)
    
    print(f"Utilisateur {name} {first_name} ajouté avec succès !")
    