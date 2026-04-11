from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = "secret123"  # required for forms

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")


@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == "test@gmail.com" and password == "123456":
            return "<h1>Login Successful</h1>"
        else:
            return "<h1>Invalid Credentials</h1>"

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)