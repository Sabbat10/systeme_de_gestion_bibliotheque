from ..data.data import list_users

# Ajouter un utilisateur à la liste des utilisateurs
def add_user():
    
    name = input("Entrez le nom de l'utilisateur : ")
    first_name = input("Entrez le prénom de l'utilisateur : ")
    age = int(input("Entrez l'âge de l'utilisateur : "))
    email = input("Entrez l'email de l'utilisateur : ")
    password = input("Entrez le mot de passe de l'utilisateur : ")
    
    
    user = {
        "name": name,
        "first_name": first_name,
        "age": age,
        "email": email,
        "password": password,
    }
    
    list_users.append(user)
    