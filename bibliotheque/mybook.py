from bibliotheque.books.book import display_books, search_book, add_book, delete_book, update_book, borrow_book, return_book
from bibliotheque.data.data import books
from user.utilisateur.utilisateurs import add_user, display_users

def mybooks():
    print("== Bienvenue chez Book Store ! == \n")

    while True:
        print("📖 **Menu Principal** 📖\n")
        print("👉 Apuyez sur :  \n")
        print("1️⃣  Voir les livres 📚")
        print("2️⃣  Rechercher un livre 🔍")
        print("3️⃣  Autres options ⚙️")
        print("4️⃣  Quitter ❌\n")
        
        print("=="*40)
        
        choix = input("👉 **Choisissez une option** : ")

        if choix == "1":
            print("\n📚 Voici la liste des livres disponibles : \n")
            # Afficher la liste des livres
            display_books()
                    
        elif choix == "2":
            search_book() 
            
        elif choix == "3":
            while True:
                print("\n⚙️ **Autres options** ⚙️\n")
                # Ajouter d'autres options
                print("Appuyer sur :  \n")
                print("1️⃣  Retour au menu principal 🔙")
                print("2️⃣  A️Jouter un livre 📚")
                print("3️⃣  Supprimer un livre 🗑️")
                print("4️⃣  Modifier un livre ✏️")
                print("5️⃣  Enprunter un livre 📖")
                print("6️⃣  Retourner un livre 📚")
                
                
                choix_autre = input("👉 **Choisissez une option** : ")
                if choix_autre == "1":
                    break
                
                
                elif choix_autre == "2":
                    print("\n📚 Ajouter un livre : \n")
                    # Ajouter un livre
                    
                    title = input("Titre du livre : ")
                    author = input("Auteur du livre : ")
                    
                    if title == "" or author == "":
                        print("\n⚠️ **Erreur : Veuillez entrer des informations valide !** ⚠️\n")
                        continue
                    # Vérifier si l'année est valide
                    try:
                        year = int(input("Année de publication : "))
                        
                    except ValueError:
                        print("\n⚠️ **Erreur : Veuillez entrer des informations valide !** ⚠️\n")
                        continue
                    
                    # Vérifier si la catégorie est valide
                    category = input("Catégorie du livre : ")
                    if category == "":
                        print("\n⚠️ **Erreur : Veuillez entrer des informations valide !** ⚠️\n")
                        continue
                    # Ajouter le livre
                    add_book(title, author, year, category)
        
                    
                elif choix_autre == "3":
                    print("\n🗑️ Supprimer un livre : \n")
                    # Supprimer un livre
                    
                    title = input("Titre du livre à supprimer : ")
                    author = input("Auteur du livre à supprimer : ")
                    
                    while True:
                        print("\n⚠️ **Attention : Cette action est irréversible !** ⚠️\n")
                        print("Êtes-vous sûr de vouloir supprimer ce livre ? Appuer sur  : \n1. Supprimer\n2. Annuler")
                        confirmation = input("👉 **Choisissez une option** : ").strip().lower()
                    
                        if confirmation == "1":
                            delete_book(title, author)
                            
                        elif confirmation == "2":
                            print("\n🔙 **Retour au menu principal...**\n")
                            break
                        else:
                            print("\n⚠️ **Option invalide, veuillez réessayer !** ⚠️\n")
                            continue
                        break
        
                    
                elif choix_autre == "4":
                    print("\n✏️ Modifier un livre : \n")
                    
                    title = input("🔹 Titre du livre à modifier : ").strip()
                    author = input("🔹 Auteur du livre à modifier : ").strip()
                    
                    # Vérifier si le livre existe avant de demander les modifications
                    book_exists = any(book['title_book'].lower() == title.lower() and book['author'].lower() == author.lower() for book in books)

                    if not book_exists:
                        print("\n⚠️ Aucun livre trouvé avec ce titre et cet auteur. ❌\n")
                    else:
                        print("\n👉 Laissez vide si vous ne voulez pas modifier une information.\n")
                        new_title = input("📖 Nouveau titre du livre : ").strip() or None
                        new_author = input("✍️ Nouvel auteur : ").strip() or None
                        
                        # Vérifier si l'année est un nombre valide ou vide
                        new_year = input("📅 Nouvelle année de publication : ").strip()
                        new_year = int(new_year) if new_year.isdigit() else None  # Garde None si vide
                        
                        new_category = input("🗂️ Nouvelle catégorie : ").strip() or None

                        print("\n⚠️ **Attention : Cette action est irréversible !** ⚠️")
                        print("Êtes-vous sûr de vouloir modifier ce livre ?")
                        confirmation = input("👉 Tapez 'oui' pour confirmer, 'non' pour annuler : ").strip().lower()

                        if confirmation == "oui":
                            update_book(title, author, new_title, new_author, new_year, new_category)
                        else:
                            print("\n🔙 **Modification annulée. Retour au menu principal...**\n")
                            
                elif choix_autre == "5":
                    print("\n📖 Enprunter un livre : \n")
                    print("")
                    print("👉 Inscrivez-vous avant d'empruter le Livre !\n")
                    
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
                    
                    # Ajouter l'utilisateur
                    add_user(name, first_name, age, email, password)
            
                    # Emprunter un livre
                    title = input("Titre du livre à emprunter : ")
                    author = input("Auteur du livre à emprunter : ")
                    
                    borrow_book(title, author, name, first_name)
                    
                elif choix_autre == "6":
                    print("\n📚 Retourner un livre : \n")
                    # Retourner un livre
                    
                    name = input("🧑 Votre Nom: ")
                    first_name = input("👶 Votre Prénom: ")
                    
                    
                    title = input("Titre du livre à retourner : ")
                    author = input("Auteur du livre à retourner : ")
                    
                    return_book(title, author, name, first_name)
                    
                else:
                    print("\n⚠️ **Option invalide, veuillez réessayer !** ⚠️\n")
        
        
        elif choix == "4":
            print("\n❌ **Fermeture du programme...** À bientôt ! 👋\n")
            break  

        else:
            print("\n⚠️ **Option invalide, veuillez réessayer !** ⚠️\n")