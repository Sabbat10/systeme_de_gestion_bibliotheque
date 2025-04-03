print("== Bienvenue chez Book Store ! == \n")

while True:
    print("📖 **Menu Principal** 📖\n")
    print("👉 Apuyez sur :  \n")
    print("1️⃣  Voir les livres 📚")
    print("2️⃣  Rechercher un livre 🔍")
    print("3️⃣  Autres options ⚙️")
    print("4️⃣  Quitter ❌\n")
    
    choix = input("👉 **Choisissez une option** : ")

    if choix == "1":
        print("\n📚 Voici la liste des livres disponibles : \n")
        # Afficher la liste des livres
        
    elif choix == "2":
        print("\n🔍 Rechercher un livre : \n")
        # Ajouter la recherche
        
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
