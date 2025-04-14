from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, PasswordField, validators, Form, HiddenField


class SignoutForm(FlaskForm):
    submit = SubmitField('Sign out')
    hidden = HiddenField("Signout")
