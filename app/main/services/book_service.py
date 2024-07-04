books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

def get_all_books():
    return books

def get_a_book(id):
    return next((book for book in books if book['id'] == id), None)

def save_new_book(data):
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return new_book
