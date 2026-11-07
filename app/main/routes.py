from flask import Blueprint, render_template
from app.models import Post

main = Blueprint("main", __name__)


@main.route("/")
def home():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("main/home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("main/about.html")
