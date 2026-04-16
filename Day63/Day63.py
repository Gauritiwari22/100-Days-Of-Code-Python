# Setting up Database
# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# db = SQLAlchemy(app)

# Creating a Model (VERY IMPORTANT)
# Model = Table

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))

# Creating Database

# Run once in Python shell:

# db.create_all()
# This creates users.db

# Adding Data
# new_user = User(name="Gauri", email="gauri@gmail.com")
# db.session.add(new_user)
# db.session.commit()

# Reading Data
# users = User.query.all()