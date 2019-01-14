# -*- coding: utf-8 -*-

# @File    : user.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')

@api.route('/<int:uid>',methods=['GET'])
@auth.login_required
def user_get(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/create',methods=['POST'])
def user_create():
    return 'create_uesr'