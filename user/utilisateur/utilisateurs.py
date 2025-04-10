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
    
    name = input("🧑 Entrez le nom de l'utilisateur : ")
    first_name = input("👶 Entrez le prénom de l'utilisateur : ")
    # Vérification de l'âge
    try:
        age = int(input("🎂 Entrez l'âge de l'utilisateur : ")  )
    except ValueError:
        print("L'âge doit être un nombre entier.")
        return
    email = input("📧 Entrez l'email de l'utilisateur : ")
    password = input("🔒 Entrez le mot de passe de l'utilisateur : ")

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
    