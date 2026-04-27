from flask import Flask, render_template

app = Flask(__name__)

# Dummy blog data
posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is my first blog post"
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is another post"
    }
]


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def show_post(id):
    for post in posts:
        if post["id"] == id:
            return render_template("post.html", post=post)

    return "Post not found"


if __name__ == "__main__":
    app.run(debug=True)