# -*- coding: utf-8 -*-

# @File    : client.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')

@api.route('/register', methods=['POST'])
def create_client():

    data = request.json
    form  = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.UESR_EMAIL:__register_client_by_email
        }
        promise[form.type]()

    return 'success'
    #注册 登录
    #参数 校验
    pass


#email 注册
def __register_client_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.account.data,form.account.data,form.secret.data)
