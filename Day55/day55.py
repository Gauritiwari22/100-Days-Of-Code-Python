# Here we are building a dynamic website using Flask + HTML
# Final outcome:
# - Python generates data
# - HTML displays it
# - Website becomes dynamic

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)

if __name__ == "__main__":
    app.run(debug=True)