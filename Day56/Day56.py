from flask import Flask, render_template

app = Flask(__name__)

# Dummy blog data
posts = [
    {"id": 1, "title": "First Post", "body": "This is my first blog"},
    {"id": 2, "title": "Second Post", "body": "Learning Flask is fun"},
    {"id": 3, "title": "Third Post", "body": "Jinja makes HTML dynamic"}
]

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for post in posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)