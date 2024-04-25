from flask import Blueprint, render_template, current_app #, session

from app.models.book import Book

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books")
def books():
    books = Book.all()
    return render_template("books.html", books=books)
