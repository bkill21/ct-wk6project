from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class UserSearchForm(FlaskForm):
    user = StringField('Search Users', validators=[DataRequired()])
    submit = SubmitField('Search')

class CreateHeroForm(FlaskForm):
    hero = StringField('Hero', validators=[DataRequired()])
    power = StringField('Power', validators=[DataRequired()])
    lore = StringField('Lore', validators=[DataRequired()])
    submit = SubmitField('Create')