from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, PasswordField, validators, Form
from wtforms.validators import DataRequired, Email


class idForm(FlaskForm):
    answer = IntegerField('Number', validators=[DataRequired(), validators.NumberRange(min=-2000, max=2000)])
    submit = SubmitField('Submit')

