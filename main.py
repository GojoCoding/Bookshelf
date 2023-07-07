from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from forms import myForm

app = Flask(__name__)
app.secret_key = "ThisIsSECRET"
bootstrap = Bootstrap5(app)


all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = myForm()
    form_Dict = {}
    if form.validate_on_submit():
        for value in form.data.items():
            if value[0] != "csrf_token" and value[0] != "addBook":
                form_Dict[value[0]] = value[1]
        all_books.append(form_Dict)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

