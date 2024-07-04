from flask import request
from flask_restx import Namespace, Resource, fields
from ..services.book_service import get_all_books, get_a_book, save_new_book

book_ns = Namespace('books', description='Book related operations')

book_model = book_ns.model('Book', {
    'id': fields.Integer(required=True, description='The book identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author')
})

@book_ns.route('/')
class BookList(Resource):
    @book_ns.doc('list_books')
    @book_ns.marshal_list_with(book_model)
    def get(self):
        """List all books"""
        return get_all_books()

    @book_ns.doc('create_book')
    @book_ns.expect(book_model, validate=True)
    def post(self):
        """Create a new book"""
        data = request.json
        return save_new_book(data)

@book_ns.route('/<int:id>')
@book_ns.response(404, 'Book not found')
@book_ns.param('id', 'The book identifier')
class Book(Resource):
    @book_ns.doc('get_book')
    @book_ns.marshal_with(book_model)
    def get(self, id):
        """Fetch a book given its identifier"""
        book = get_a_book(id)
        if not book:
            book_ns.abort(404)
        else:
            return book
