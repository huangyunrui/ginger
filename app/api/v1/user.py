# -*- coding: utf-8 -*-

# @File    : user.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import Blueprint

from app.libs.redprint import Redprint
from app.libs.token_auth import auth

user = Blueprint('user',__name__)

api = Redprint('user')

@api.route('',methods=['GET'])
@auth.login_required
def user_get():
    return 'hello'


@api.route('/create',methods=['POST'])
def user_create():
    return 'create_uesr'