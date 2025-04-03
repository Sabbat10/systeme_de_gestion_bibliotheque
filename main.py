from books.book import display_books, search_book, add_book

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
                
            elif choix_autre == "4":
                print("\n✏️ Modifier un livre : \n")
                # Modifier un livre
                
            else:
                print("\n⚠️ **Option invalide, veuillez réessayer !** ⚠️\n")
    
    elif choix == "4":
        print("\n❌ **Fermeture du programme...** À bientôt ! 👋\n")
        break  

    else:
        print("\n⚠️ **Option invalide, veuillez réessayer !** ⚠️\n")
