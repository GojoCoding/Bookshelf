from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from db import db, Bookshelf
from sqlalchemy.exc import SQLAlchemyError
from forms import myForm, ratingsForm

app = Flask(__name__)
app.secret_key = "ThisIsSECRET"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Library.db"
bootstrap = Bootstrap5(app)

db.init_app(app)

# Creates database and tables
with app.app_context():
    db.create_all()


@app.route('/', methods=["GET"])
def home():
    bookshelf_Data = Bookshelf.query.all()
    return render_template('index.html', bookshelf=bookshelf_Data)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = myForm()
    if form.validate_on_submit():
        # Add Form Input into Database -- Create
        with app.app_context():
            new_Entry = Bookshelf(title=form.bookName.data, author=form.authorName.data, rating=form.rating.data)
            # Validating if entry was successfully added to Database
            try:
                db.session.add(new_Entry)
                db.session.commit()
                print("Transaction Successful ")
            except SQLAlchemyError as error:
                db.session.rollback()
                print(f"Error occured during transaction: {error}")
                return redirect(url_for('add'))
        # End of new entry to Database
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit', methods=["GET","POST"])
def edit():
    # Update data in table
    if request.method == "POST":
        book_id = request.form["id"]
        # This is what actually searches and gets the row of data(book info) we need
        book_to_update = db.get_or_404(Bookshelf, book_id)
        # This is where the user data replaces the data in the actual database
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_ID = request.args.get('id')
    book_selected = db.get_or_404(Bookshelf, book_ID)
    return render_template('editRating.html', book=book_selected)


@app.route('/delete/<int:book_id>', methods=["POST"])
def delete(book_id):
    book_Selected = db.get_or_404(Bookshelf, book_id)
    db.session.delete(book_Selected)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
