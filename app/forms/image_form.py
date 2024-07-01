from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.api.aws_helpers import ALLOWED_EXTENSIONS

def img_ext(form, field):
    # Checking if user exists
    url = field.data
    if not (url[-4:] == '.png' or  url[-4:] == '.jpg' or  url[-5:] == '.jpeg'  or  url[-4:] == '.gif') :
        raise ValidationError('url must end in .png, .jpg, .jpeg, or .gif')

class ImageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=250)])
    description = StringField('Description', validators=[DataRequired(), Length(max=255)])
    # img = StringField('Image Url', validators=[DataRequired(),Length(max=255)])
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField('submit')
