from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, PasswordField, validators, Form
from wtforms.validators import DataRequired, Email
from sqlalchemy.orm import sessionmaker


class idForm(FlaskForm):
    answer = IntegerField('Number', validators=[DataRequired(), validators.NumberRange(min=-2000, max=2000)])
    submit = SubmitField('Submit')

