from flask_wtf import FlaskForm
from wtforms import *


class loginForm(FlaskForm):
    username = StringField(label='用户名')
    password = PasswordField(label='密码')
    login = SubmitField(label='登录')


class AllInfo(FlaskForm):
    choice = StringField(label='请输入')
    search = SubmitField(label='查询')










