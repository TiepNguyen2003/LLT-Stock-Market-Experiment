from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, PasswordField, validators, Form
from wtforms.validators import DataRequired, Email
from sqlalchemy.orm import sessionmaker


class SignoutForm(FlaskForm):
    submit = SubmitField('Sign out')

