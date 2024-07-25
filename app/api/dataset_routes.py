from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, Dataset, Message, db
from app.forms import DatasetForm, MessageForm
from datetime import datetime
from ..models import Image, User, db, Comment, Dataset

dataset_routes = Blueprint('datasets', __name__)

def validation_errors_to_error_messages(validation_errors):
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@dataset_routes.route('/')
@login_required
def get_datasets():
    print("testing /api/dataset")
    datasets = Dataset.query.filter(Dataset.user_id == current_user.id).all()
    return {'datasets' : [dataset.to_dict() for dataset in datasets]}

@dataset_routes.route('/test')
def test_dataset():
    print("test /api/dataset/test")
    datasets = Dataset.query.all()
    return {'datasets' : [dataset.to_dict() for dataset in datasets]}

@dataset_routes.route('/<int:dataset_id>')
def get_dataset(dataset_id):
    dataset = Dataset.query.get(dataset_id)
    return dataset.to_dict()

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
