# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm as Form
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import Required, DataRequired

class LoginForm(Form):
    """
    LoginForm.
    This class have two string fields for username and password,
    one for checkbox(remember me) and one for submit. All fields
    have render_kw attribute for rendering templates with MDB style
    """
    username = StringField('Username', validators=[DataRequired()],render_kw={"type":"text", "id":"defaultLoginFormEmail", "class":"form-control mb-4", "placeholder":"Имя пользователя"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"type":"text", "id":"defaultLoginFormPassword", "class":"form-control mb-4", "placeholder":"Пароль"})
    remember_me = BooleanField('Remember Me',render_kw={"class":"custom-control-input", "id":"defaultLoginFormRemember"})
    submit = SubmitField('Отправить',render_kw={"class":"btn btn-indigo btn-block my-4"})