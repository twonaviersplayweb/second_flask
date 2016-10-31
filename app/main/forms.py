from flask.ext.wtf import Form
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class RegisterForm(Form):
    username = StringField('name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log in')


class LoginForm(Form):
    username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')