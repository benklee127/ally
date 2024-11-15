from flask import Blueprint, jsonify, render_template, request
from flask_login import login_required, current_user, logout_user
from app.models import User, Image, Dataset, Message
from ..models import db
from app.forms import  DatasetForm
from app.api.aws_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3
from datetime import date

user_routes = Blueprint('users', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        print("fields", field)
        print("validation", validation_errors)

        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})


@user_routes.route('/deleteuser/<int:id>')
@login_required
def delete_user(id):
    deleted_user = User.query.get(id)
    if deleted_user.id == current_user.id:
        logout_user()
        print(current_user)
        db.session.delete(deleted_user)
        db.session.commit()
    return 'User deleted'



@user_routes.route('/<int:id>')
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()



#get user showcase
@user_routes.route('/showcase/<int:userId>')
def get_user_showcase(userId):
    showcase_images = Image.query.filter(Image.user_id == userId).filter(Image.showcase == True)
    return {'showcase_images': [image.to_dict() for image in showcase_images]}

#set showcase helper
def set_showcase(imageId, val):
    # print(imageId)
    image = Image.query.get(imageId)
    if current_user.id == image.user_id:
        image.showcase = val
        db.session.commit()
        return 'showcase toggled'
    return 'not your image'

#update showcase form
@user_routes.route('/update/showcase', methods=["POST"])
def update_showcase_form():
    showcase_update = request.get_json()
    # print('showcase requestjson', showcase_update)
    for img in showcase_update:
        set_showcase(img, showcase_update[img])
    return get_user_showcase(current_user.id)



@user_routes.route('/collections')
def get_user_collections():
    print("attempting to get user collections")
    datasets = Dataset.query.all()
    print("sending user collections",datasets)
    return jsonify({'datasets': [dataset.to_dict() for dataset in datasets]})

@user_routes.route("/collections/get/<int:collection_id>")
def get_collection(collection_id):
    print("hit get collection by id route")
    dataset = Dataset.query.get(collection_id)
    return dataset.to_dict()

@user_routes.route('/collections/create', methods=["POST"])
def create_user_collection():
    print('create collection route hit')
    if current_user.is_authenticated:
        form = DatasetForm()
        form['csrf_token'].data = request.cookies['csrf_token']

        print("user authenticated in collection creation, form data: ", form.data)
        title = form.data["title"]
        description = form.data["description"]
        embedding = form.data["embedding"]
        newDataset = Dataset(title=title, description=description, user_id=current_user.id, embedding=embedding)
        db.session.add(newDataset)
        db.session.commit()
        first_message = Message(
            content = "Start by uploading a file!",
            dataset_id = newDataset.id,
            user_id=2
            )

        db.session.add(first_message)
        db.session.commit()
        return newDataset.to_dict()
    
@user_routes.route('/collections/update/<int:collection_id>', methods=["POST"])
def update_user_collection(collection_id):
    print('update collection route hit')
    if current_user.is_authenticated:
        form = DatasetForm()
        update_collection = Dataset.query.get(collection_id)
        update_collection.title = form.data['title']
        update_collection.description = form.data['description']
        update_collection.res_llm = form.data['res_llm']
        db.session.commit()

        return update_collection.to_dict()

