from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from forms import myForm

app = Flask(__name__)
app.secret_key = "ThisIsSECRET"
bootstrap = Bootstrap5(app)


all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = myForm()
    if form.validate_on_submit():
        for value in form.data.items():
            print(value)
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

