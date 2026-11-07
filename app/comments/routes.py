from flask import Blueprint, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Comment, Post

comments = Blueprint("comments", __name__)


@comments.route("/post/<int:post_id>/comment", methods=["POST"])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form.get("content", "").strip()

    if not content:
        flash("Comment cannot be empty.")
        return redirect(url_for("posts.post_detail", post_id=post.id))

    comment = Comment(
        content=content,
        user_id=current_user.id,
        post_id=post.id
    )

    db.session.add(comment)
    db.session.commit()

    flash("Comment added successfully!")
    return redirect(url_for("posts.post_detail", post_id=post.id))


@comments.route("/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != current_user.id:
        return "Unauthorized", 403

    post_id = comment.post_id
    db.session.delete(comment)
    db.session.commit()

    flash("Comment deleted.")
    return redirect(url_for("posts.post_detail", post_id=post_id))
