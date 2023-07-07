from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class myForm(FlaskForm):
    bookName = StringField(label="Book Name", validators=[DataRequired()])
    authorName = StringField(label="Author Name", validators=[DataRequired()])
    rating = StringField(label="Rating", validators=[DataRequired()])
    addBook = SubmitField(label="Add Book")


