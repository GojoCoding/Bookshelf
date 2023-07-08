from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Defines a table called 'bookshelf' in database BUT does not create it in actual database yet
class Bookshelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
