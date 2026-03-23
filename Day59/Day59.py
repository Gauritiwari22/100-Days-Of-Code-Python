from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = next((post for post in all_posts if post["id"] == post_id), None)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)