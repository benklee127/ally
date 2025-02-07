from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.api.aws_helpers import ALLOWED_EXTENSIONS

# def file_ext(form, field):
#     # Checking if user exists
#     url = field.data
#     if not (url[-4:] == '.png' or  url[-4:] == '.jpg' or  url[-5:] == '.jpeg'  or  url[-4:] == '.gif') :
#         raise ValidationError('url must end in .png, .jpg, .jpeg, or .gif')

class FileForm(FlaskForm):
    file = FileField("File", validators=[FileRequired()])
    collection_id = StringField('collection_id', validators=[DataRequired(), Length(max=255)])
    chunk_size = StringField('chunk_size',default=4096)
    submit = SubmitField('submit')
