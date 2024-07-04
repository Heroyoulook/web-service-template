from flask import Flask, send_from_directory
from flask_restx import Api
from app.main.controllers.book_controller import book_ns

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')

    api = Api(app, title='My Flask API', version='1.0', description='A simple demonstration API', doc='/api')

    # Register namespaces with the prefix /api
    api.add_namespace(book_ns, path='/api/books')

    # Serve the frontend
    @app.route('/')
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')

    # Serve static files
    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory(app.static_folder, path)

    # Catch-all route to serve the index.html for any other path (for SPA routing)
    @app.errorhandler(404)
    def not_found(e):
        return send_from_directory(app.static_folder, 'index.html')

    return app
