# -*- coding: utf-8 -*-

# @File    : user.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

#管理员操作
@api.route('/<int:uid>',methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


#管理员操作
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass



#普通用户操作接口
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

@api.route('',methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_of_404()
    return jsonify(user)