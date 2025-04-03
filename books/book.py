from data.data import books

# Affichage de la liste des livres
# Cette fonction affiche la liste des livres disponibles dans la bibliothèque.
def display_books():
    print("📚 BOOKS 📚\n")
    for book in books:
        print(f"- {book['title_book'].upper()} \n  ✍️ Auteur : {book['author']}, 📅 {book['year']}" )
        print("")
    print("\n")  


# Recherche de livres par mot-clé
# Cette fonction permet à l'utilisateur de rechercher des livres en fonction de divers critères.
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
        

# Ajout d'un livre
# Cette fonction permet à l'utilisateur d'ajouter un livre à la bibliothèque.
def add_book(title, author, year, category):

    new_book = {
        'title_book': title,
        'author': author,
        'year': year,
        'category': category
    }
    
    books.append(new_book)
    print(f"\n✅ Le livre '{title}' a été ajouté avec succès à la bibliothèque !\n")
    
    

# Suppression d'un livre
# Cette fonction permet à l'utilisateur de supprimer un livre de la bibliothèque.
def delete_book(title, author):
    for book in books:
        if book['title_book'].lower() == title.lower() and book['author'].lower() == author.lower():
            books.remove(book)
            print(f"\n❌ Le livre '{title}' a été supprimé de la bibliothèque !\n")
            return
    print("\n⚠️ Aucun livre trouvé avec ce titre et cet auteur.\n")
    
    

# Modification d'un livre
# Cette fonction permet à l'utilisateur de modifier les informations d'un livre dans la bibliothèque.

def update_book(title, author, new_title=None, new_author=None, new_year=None, new_category=None):
    for book in books:
        if book['title_book'].lower() == title.lower() and book['author'].lower() == author.lower():
            if new_title:
                book['title_book'] = new_title
            if new_author:
                book['author'] = new_author
            if new_year:
                book['year'] = new_year
            if new_category:
                book['category'] = new_category
            print(f"\n✅ Le livre '{title}' a été modifié avec succès !\n")
            return
    print("\n⚠️ Aucun livre trouvé avec ce titre et cet auteur.\n")