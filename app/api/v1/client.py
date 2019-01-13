# -*- coding: utf-8 -*-

# @File    : client.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')

@api.route('/register', methods=['POST'])

def create_client():
    form  = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.UESR_EMAIL:__register_client_by_email
    }
    promise[form.type.data]()
    return Success()


#email 注册
def __register_client_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
    return Success()