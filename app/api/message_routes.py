from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, Dataset, Message, db
from app.forms import DatasetForm, MessageForm
from datetime import datetime
from ..models import Image, User, db, Comment, Dataset, Message
import chromadb
from chromadb.utils import embedding_functions


message_routes = Blueprint('messages', __name__)

def validation_errors_to_error_messages(validation_errors):
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@message_routes.route('/<int:dataset_id>')
@login_required
def get_messages(dataset_id):
    print("testing /api/messages/<int:dataset_id>")
    messages = Message.query.filter(Message.dataset_id == dataset_id).all()
    print(messages)
    return {'messages' : [message.to_dict() for message in messages]}

@message_routes.route('/<int:dataset_id>', methods=["POST"])
def post_message(dataset_id):
    print("test /api/messages//<int:dataset_id> POST")
    if current_user.is_authenticated:
        form = MessageForm()
        content = form.data['content']
        new_query = Message(
            content = content,
            dataset_id = dataset_id,
            user_id=current_user.id
            )
        db.session.add(new_query)
        db.session.commit()

    updated_messages = Message.query.filter(Message.dataset_id == dataset_id).all()
    return {'messages' : [message.to_dict() for message in updated_messages]}

# @collection_routes.route('/<int:collection_id>')
# def load_collection(collection_id):
#     print("test /api/collections/<int:collection_id>")
#     collection = Collection.query.get(collection_id)
#     messages = Message.query.filter(Message.collection_id == collection_id).all()
#     return {'collection': collection.to_dict(),
#             'messages' : [message.to_dict() for message in messages]}

# @collection_routes.route('/create')
# def create_collection():
#     form = CollectionForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         new_collection = Collection(
#             title = form.data['title'],
#             description = form.data['description'],
#             user_id = current_user.id
#         )
#         db.session.add(new_collection)
#         db.session.commit()
#         return new_collection.to_dict()
#     return {'errors': validation_errors_to_error_messages(form.errors)}, 401
