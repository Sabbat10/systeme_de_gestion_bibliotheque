from data.data import books


def display_books():
    print("📚 BOOKS 📚\n")
    for book in books:
        print(f"- {book['title_book'].upper()} \n  ✍️ Auteur : {book['author']}, 📅 {book['year']}" )
        print("")
    print("\n")  
