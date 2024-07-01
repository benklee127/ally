from flask import Blueprint, jsonify, render_template, request
from flask_login import login_required, current_user, logout_user
from app.models import User, Image, Dataset, Message
from ..models import db
from app.forms import UserDetailsForm, DatasetForm
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


#user profile photo edit route
@user_routes.route('/<int:user_id>/profile_photo', methods=["POST"])
def user_profile_photo(user_id):

    update_user = User.query.get(user_id)

    # print("in the edit user profile photo route~~~~~~~~~~~~~~~~~~")
    form = UserDetailsForm(user=update_user)
    form['csrf_token'].data = request.cookies['csrf_token']
    # print('form data in backend before submission',form.data[''])
    print("form data in profile route: ", form.data)

    # old_profile_photo = update_user.profile_photo
    # old_cover_photo = update_user.cover_photo

    new_profile_photo = form.data['profile_photo']
    # print("new profile photo in edit user profile photo route: ", new_profile_photo)
    new_profile_photo.filename = get_unique_filename(new_profile_photo.filename)
    upload_profile_photo = upload_file_to_s3(new_profile_photo)
    profile_photo_url = upload_profile_photo['url']
    # print("profile_photo_url: ", profile_photo_url)
    if update_user.id == current_user.id:
        remove_file_from_s3(update_user.profile_photo)

    if form.validate_on_submit():
        update_user.profile_photo = profile_photo_url

        # new_image = Image(title="profile photo title", description='profile photo description', img=profile_photo_url, view_count=0, user_id=user_id, uploaded_on=date.today())

        # db.session.add(new_image)
        db.session.commit()
        print("details updated")
        return update_user.to_dict()
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401



#user detail test edit route
@user_routes.route('/<int:user_id>/details')
def edit_user_details(user_id):
    form  = UserDetailsForm()

    return render_template("user_details_form.html", form=form)

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



#user info detail edit route
@user_routes.route('/<int:user_id>/details/<form_type>', methods=["POST"])
def user_details(user_id,form_type):
    update_user = User.query.get(user_id)

    form = UserDetailsForm(user=update_user)
    form['csrf_token'].data = request.cookies['csrf_token']
    # print('form data in backend before submission',form.data['occupation'])
    # print(form.data)

    if form.validate_on_submit():
        if (form_type == 'bio'):
            update_user.biography = form.data['biography']
        # if (form_type == 'profile_photo'):
        #     update_user.profile_photo = profile_photo_url
        # if (form_type == 'cover_photo'):
        #     update_user.cover_photo = cover_photo_url
        if (form_type == 'details'):
            update_user.occupation = form.data['occupation']
            update_user.hometown = form.data['hometown']
            update_user.city = form.data['city']
            update_user.country = form.data['country']
            update_user.website = form.data['website']
            update_user.facebook = form.data['facebook']
            update_user.twitter = form.data['twitter']
            update_user.instagram = form.data['instagram']
            update_user.pinterest = form.data['pinterest']
            update_user.tumblr = form.data['tumblr']
        db.session.commit()
        print("details updated")
        return update_user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401




#user cover photo edit route
@user_routes.route('/<int:user_id>/cover_photo', methods=["POST"])
def user_cover_photo(user_id):
    update_user = User.query.get(user_id)

    # print("in the edit user profile photo route~~~~~~~~~~~~~~~~~~")
    form = UserDetailsForm(user=update_user)
    form['csrf_token'].data = request.cookies['csrf_token']
    # print('form data in backend before submission',form.data[''])
    print("form data in profile route: ", form.data)

    # old_profile_photo = update_user.profile_photo
    # old_cover_photo = update_user.cover_photo

    new_cover_photo = form.data['cover_photo']
    print("new cover photo in edit user cover photo route: ", new_cover_photo)
    new_cover_photo.filename = get_unique_filename(new_cover_photo.filename)
    upload_cover_photo = upload_file_to_s3(new_cover_photo)
    cover_photo_url = upload_cover_photo['url']
    print("profile_photo_url: ", cover_photo_url)

    if update_user.id == current_user.id:
        remove_file_from_s3(update_user.cover_photo)

    if form.validate_on_submit():
        update_user.cover_photo = cover_photo_url

        # new_image = Image(title="cover photo title", description='cover photo description', img=cover_photo_url, view_count=0, user_id=user_id, uploaded_on=date.today())

        # db.session.add(new_image)
        db.session.commit()
        print("details updated")
        return update_user.to_dict()

@user_routes.route('/collections')
def get_user_collections():
    print("attempting to get user collections")
    datasets = Dataset.query.all()
    print("sending user collections",datasets)
    return jsonify({'datasets': [dataset.to_dict() for dataset in datasets]})

@user_routes.route('/collections/create', methods=["POST"])
def create_user_collection():
    print('create collection route hit')
    if current_user.is_authenticated:
        form = DatasetForm()
        form['csrf_token'].data = request.cookies['csrf_token']

        if form.validate_on_submit():
            title = form.data["title"]
            description = form.data["description"]
            newDataset = Dataset(title=title, description=description, user_id=current_user.id)
            db.session.add(newDataset)
            db.session.commit()
            return newDataset.to_dict()
