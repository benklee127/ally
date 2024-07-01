from flask import Blueprint, jsonify, redirect, render_template
from flask_login import login_required, current_user
from ..models import Comment, User, Image, db
from app.forms import CommentForm
from datetime import date

comment_routes = Blueprint("comments", __name__)

#Get comment by id
@comment_routes.route('/<int:comment_id>')
def get_comment_by_image_id(comment_id):
    comment = Comment.query.get(comment_id)
    print(comment)
    return comment.to_dict()


@comment_routes.route('/<int:image_id>/<int:user_id>')
def post_comment_form(image_id,user_id):
    form = CommentForm()
    return render_template("comment_form.html", form=form)

#POST a comment by image id
@comment_routes.route('/<int:image_id>/<int:user_id>', methods=["POST"])
def post_comment(image_id, user_id):
    if current_user.is_authenticated:
        form = CommentForm()
        # if form.validate_on_submit():
        description = form.data['description']
        comment = Comment(description=description, user_id=user_id,
                            image_id=image_id, created_at= date.today(),
                            updated_at = date.today())
        db.session.add(comment)
        db.session.commit()
        return comment.to_dict()
        # return 'Bad Data'

@comment_routes.route('/update/<int:comment_id>')
def update_comment_form(comment_id):
    form = CommentForm()
    return render_template("comment_form.html", form=form)

# Edit a comment by comment id, PUT doesn't work with flask???
@comment_routes.route('/update/<int:comment_id>', methods=['POST'])
def edit_comment(comment_id):
    if current_user.is_authenticated:
        form = CommentForm()
        target_comment = Comment.query.get(comment_id)
        if target_comment.user.id == current_user.id:
            # if form.validate_on_submit():

            target_comment.description = form.data['description']
            target_comment.updated_at = date.today()
            db.session.add(target_comment)
            db.session.commit()
            return target_comment.to_dict()
        # return 'bad data'

# Delete a comment by comment id
@comment_routes.route('/<int:comment_id>/delete', methods=['DELETE'])
def delete_comment(comment_id):
    if current_user.is_authenticated:
        comment_to_delete = Comment.query.get(comment_id)
        if comment_to_delete.user_id == current_user.id:
            db.session.delete(comment_to_delete)
            db.session.commit()
        return {'comment': 'comment has been deleted'}
