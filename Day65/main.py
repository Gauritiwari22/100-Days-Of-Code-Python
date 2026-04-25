from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


# 🔹 DATABASE MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


# 🔹 FORM PAGE
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("show_users"))

    return render_template("form.html")


# 🔹 SHOW USERS (UI)
@app.route("/users")
def show_users():
    users = User.query.all()
    return render_template("users.html", users=users)


# 🔹 DELETE USER (UI)
@app.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get(id)

    if user:
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for("show_users"))


# 🔹 EDIT USER
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    user = User.query.get(id)

    if request.method == "POST":
        user.name = request.form.get("name")
        user.email = request.form.get("email")
        db.session.commit()
        return redirect(url_for("show_users"))

    return render_template("edit.html", user=user)


# 🔹 API - GET ALL USERS
@app.route("/api/users")
def get_users():
    users = User.query.all()

    data = []
    for user in users:
        data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

    return jsonify(data)


# 🔹 API - GET SINGLE USER
@app.route("/api/user/<int:id>")
def get_user(id):
    user = User.query.get(id)

    if not user:
        return {"error": "User not found"}

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


# 🔹 API - ADD USER
@app.route("/api/add", methods=["POST"])
def add_user():
    name = request.json.get("name")
    email = request.json.get("email")

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added"})


# 🔹 API - DELETE USER
@app.route("/api/delete/<int:id>")
def api_delete(id):
    user = User.query.get(id)

    if not user:
        return {"error": "User not found"}

    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted"}


# 🔹 RUN APP
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)