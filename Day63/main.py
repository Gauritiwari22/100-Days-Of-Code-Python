from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return "<h1>Data Saved!</h1>"

    return render_template("form.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)