from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy credentials
VALID_EMAIL = "test@gmail.com"
VALID_PASSWORD = "123456"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == VALID_EMAIL and password == VALID_PASSWORD:
            return render_template("success.html", user=email)
        else:
            return render_template("fail.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)