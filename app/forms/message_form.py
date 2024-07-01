from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

class MessageForm(FlaskForm):
    content = StringField('description', validators=[DataRequired(), Length(min=1,max=255)])
    collection_id = IntegerField('collection_id')
    # key = StringField('key', validators=[Length(max=20)])
    user_id  = IntegerField('user_id', validators=[DataRequired()])
    submit = SubmitField('submit')
