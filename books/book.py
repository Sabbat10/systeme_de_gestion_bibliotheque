from data.data import books


def display_books():
    print("📚 BOOKS 📚\n")
    for book in books:
        print(f"- {book['title_book'].upper()} \n  ✍️ Auteur : {book['author']}, 📅 {book['year']}" )
        print("")
    print("\n")  


def search_book():
    keyword = input("\n🔍 Entrez un mot-clé (titre, auteur, catégorie ou année) : ").strip().lower()
    
    found = False
    for book in books:
        # Vérifier si le mot-clé est présent dans n'importe quel champ
        if (keyword in book['title_book'].lower() or
            keyword in book['author'].lower() or
            keyword in book['category'].lower() or
            keyword == str(book['year'])):  
            
            print(f"\n📖 **{book['title_book'].upper()}**")
            print(f"   ✍️ Auteur : {book['author']}, 📅 {book['year']}, 🗂️ Catégorie : {book['category']}\n")
            found = True

    if not found:
        print("\n⚠️ Aucun livre trouvé avec ce mot-clé. Essayez un autre !\n")