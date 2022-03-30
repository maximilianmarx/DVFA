from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AddCommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')