from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, Form
from wtforms.validators import DataRequired, Email
from sqlalchemy.orm import sessionmaker


class QuestionForm(FlaskForm):
    answer = StringField('answer', [validators.Length(min=1, max=25)])

    '''def __init__(self, question_text=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if question_text:
            self.questionText = question_text'''

