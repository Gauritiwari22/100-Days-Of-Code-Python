from flask import Flask, render_template, request, redirect, url_for
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

        return redirect(url_for("users"))

    return render_template("index.html")


@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template("users.html", users=all_users)


@app.route("/delete/<int:id>")
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("users"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    user = User.query.get(id)

    if request.method == "POST":
        user.name = request.form.get("name")
        user.email = request.form.get("email")

        db.session.commit()
        return redirect(url_for("users"))

    return render_template("edit.html", user=user)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)