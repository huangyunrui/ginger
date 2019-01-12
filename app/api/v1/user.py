# -*- coding: utf-8 -*-

# @File    : user.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import Blueprint

from app.libs.redprint import Redprint

user = Blueprint('user',__name__)

api = Redprint('user')

@api.route('',methods=['GET'])
def user_get():
    return 'hel'


@api.route('/create',methods=['POST'])
def user_create():
    return 'create_uesr'