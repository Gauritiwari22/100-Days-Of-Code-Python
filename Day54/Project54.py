from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "Contact me here"

if __name__ == "__main__":
    app.run(debug=True)