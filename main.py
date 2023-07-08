from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from db import db, Bookshelf
from sqlalchemy.exc import SQLAlchemyError
from forms import myForm

app = Flask(__name__)
app.secret_key = "ThisIsSECRET"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Library.db"
bootstrap = Bootstrap5(app)

db.init_app(app)

# Creates database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


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


if __name__ == "__main__":
    app.run(debug=True)
