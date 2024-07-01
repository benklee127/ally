from flask import Blueprint, jsonify, request
from flask import Flask, request, redirect, url_for
from flask_login import login_required, current_user
# from werkzeug.utils import allowed_file
from app.models import User, Dataset, Message, db
from app.forms import DatasetForm, MessageForm
from datetime import datetime
from ..models import Image, User, db, Comment, Dataset, Message, Datafile
import os

datafile_routes = Blueprint('datafiles', __name__)

upload_folder = '/uploads/'
def validation_errors_to_error_messages(validation_errors):
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@datafile_routes.route('/<int:dataset_id>')
@login_required
def get_datafiles(dataset_id):
    print("testing /api/datafiles/<int:dataset_id> GET")
    datafiles = Datafile.query.filter(Message.dataset_id == dataset_id).all()
    print(datafiles)
    return {'datafiles' : [datafile.to_dict() for datafile in datafiles]}

# @datafile_routes.route('/<int:dataset_id>', methods=["POST"])
# @login_required
# def post_datafile(dataset_id):

    #     return f'File uploaded successfully: {filename}'
    # else:
    #     return 'Invalid file format. Allowed extensions: {ALLOWED_EXTENSIONS}'


# @datafile_routes.route('/<int:dataset_id>', methods=["POST"])
# def post_datafile(dataset_id):
#     print("testing /api/datafiles/<int:dataset_id> POST")
#     if current_user.is_authenticated:
#         form = MessageForm()
#         content = form.data['content']
#         new_query = Message(
#             content = content,
#             dataset_id = dataset_id,
#             user_id=current_user.id
#             )
#         db.session.add(new_query)
#         db.session.commit()
#     updated_messages = Message.query.filter(Message.dataset_id == dataset_id).all()
#     return {'messages' : [message.to_dict() for message in updated_messages]}
